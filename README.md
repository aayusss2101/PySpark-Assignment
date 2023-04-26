# PySpark-Assignment

## Files
- api.py: Contains the code for Flask-based API.
- process.py: Contains code to process the data.

<br/>

Before using you will need to set the environment variable

```API_KEY=<your-api-key>```

<br/>

The API will start running on http://127.0.0.1:5000/.

## Routes
The API provides the following routes:

- /affected/most - Get the most affected state.
- /affected/least - Get the least affected state.
- /total/most - Get the state with the most COVID-19 cases.
- /total/least - Get the state with the least COVID-19 cases.
- /total - Get the total number of COVID-19 cases in India.
- /handled/most - Get the state that has handled the most COVID-19 cases.
- /handled/least - Get the state that has handled the least COVID-19 cases.
- /data - Get all the COVID-19 data for India.
