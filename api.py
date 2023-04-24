from process import Process
from flask import Flask, jsonify

# Flask app
app = Flask(__name__)


# Route for Most Affected
@app.route('/affected/most', methods=['GET'])
def get_most_affected():
    try:
        global p
        state = p.get_most_affected()[0]["State"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})

    
# Route for Least Affected
@app.route('/affected/least', methods=['GET'])
def get_least_affected():
    try:
        global p
        state = p.get_least_affected()[0]["State"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})

    
# Route for Most Cases
@app.route('/total/most', methods=['GET'])
def get_most_total():
    try:
        global p
        state = p.get_most_total()[0]["State"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})


# Route for Least Cases
@app.route('/total/least', methods=['GET'])
def get_least_total():
    try:
        global p
        state = p.get_least_total()[0]["State"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})

    
# Route for Total Cases
@app.route('/total', methods=['GET'])
def get_total():
    try:
        global p
        state = p.get_total()[0]["Total Covid Cases"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})

    
# Route for Most Handled
@app.route('/handled/most', methods=['GET'])
def get_most_handled():
    try:
        global p
        state = p.get_most_handled()[0]["State"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})

    
# Route for Least Handled
@app.route('/handled/least', methods=['GET'])
def get_least_handled():
    try:
        global p
        state = p.get_least_handled()[0]["State"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})

    
# Route for Data
@app.route('/data', methods=['GET'])
def get_data():
    try:
        global p
        data = p.get_data()
        return jsonify({'data': data})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    global p
    p = Process()
    app.run(debug=True)
