import requests
import json
import os
from dotenv import load_dotenv
from pyspark.sql.session import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *


class Process:

    dataDF = None
    affectedDF = None
    handleDF = None

    '''
    Sanitises the data
    
    Parameters:
    state: State name
    Returns:
    Cleaned Name
    '''
    def __sanitise(self, state):
        try:
            idx = state.index("*")
            return state[:idx]
        except:
            return state

    '''
    Loads Dataset
    
    Parameters:
    key: API Key
    Returns:
    List of data
    '''
    def __load_dataset(self, key):

        url = "https://covid-19-india2.p.rapidapi.com/details.php"

        headers = {
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "covid-19-india2.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        data = response.text
        data = json.loads(data)

        dataList = []

        for key in data:
            if type(data[key]) is not dict:
                continue
            l = []
            for val in data[key].values():
                l.append(val)
            if l[1] == "":
                continue
            l[1] = self.__sanitise(l[1])
            for i in range(2, len(l)):
                l[i] = int(l[i])
            dataList.append(l)

        return dataList

    
    '''
    Create Dataframe
    
    Parameters:
    dataList: List of data
    '''
    def __create_dataframe(self, dataList):
        self.spark = SparkSession.builder.master(
            'local[2]').appName('Assignment').getOrCreate()

        schema = StructType([StructField('SNo', StringType()), StructField('State', StringType()), StructField(
            'Confirm', LongType()), StructField('Cured', LongType()), StructField('Death', LongType()), StructField('Total', LongType())])
        self.dataDF = self.spark.createDataFrame(data=dataList, schema=schema)
    
    '''
    Loads dataframe
    '''
    def __load_dataframe(self):
        load_dotenv()
        key = os.getenv("API_KEY")
        dataList = self.__load_dataset(key)
        self.__create_dataframe(dataList)

    def __init__(self):
        self.__load_dataframe()

    def __create_affected_df(self):
        if self.affectedDF is not None:
            return
        self.affectedDF = self.dataDF.withColumn(
            "Affected", col("Death")/col("Total"))

    def __create_handled_df(self):
        if self.handleDF is not None:
            return
        self.handleDF = self.dataDF.withColumn(
            "Handled", col("Cured")/col("Total"))

    def get_most_affected(self):
        self.__create_affected_df()
        return self.affectedDF.orderBy(col('Affected').desc()).limit(1).select(col("State")).collect()

    def get_least_affected(self):
        self.__create_affected_df()
        return self.affectedDF.orderBy(col('Affected')).limit(1).select(col("State")).collect()

    def get_most_total(self):
        return self.dataDF.orderBy(col("Total").desc()).limit(1).select("State").collect()

    def get_least_total(self):
        return self.dataDF.orderBy(col("Total")).limit(1).select("State").collect()

    def get_total(self):
        return self.dataDF.select(col("Total")).agg(sum(col("Total")).alias("Total Covid Cases")).collect()

    def get_most_handled(self):
        self.__create_handled_df()
        return self.handleDF.orderBy(col("Handled").desc()).limit(1).select("State").collect()

    def get_least_handled(self):
        self.__create_handled_df()
        return self.handleDF.orderBy(col("Handled")).limit(1).select("State").collect()

    def get_data(self):
        data = self.dataDF.collect()
        return [{'State': r['State'], 'Confirm': r['Confirm'], 'Cured': r['Cured'], 'Death': r['Death'], 'Total': r['Total']}
                for r in data]
