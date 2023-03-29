from process import Process
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/affected/most', methods=['GET'])
def get_most_affected():
    try:
        global p
        state = p.get_most_affected()[0]["State"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/affected/least', methods=['GET'])
def get_least_affected():
    try:
        global p
        state = p.get_least_affected()[0]["State"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/total/most', methods=['GET'])
def get_most_total():
    try:
        global p
        state = p.get_most_total()[0]["State"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/total/least', methods=['GET'])
def get_least_total():
    try:
        global p
        state = p.get_least_total()[0]["State"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/total', methods=['GET'])
def get_total():
    try:
        global p
        state = p.get_total()[0]["Total Covid Cases"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/handled/most', methods=['GET'])
def get_most_handled():
    try:
        global p
        state = p.get_most_handled()[0]["State"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/handled/least', methods=['GET'])
def get_least_handled():
    try:
        global p
        state = p.get_least_handled()[0]["State"]
        return jsonify({'data': state})
    except Exception as e:
        return jsonify({'error': str(e)})


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
