from db import db
from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/metrics', methods=['GET'])
def getMetrics():
    return jsonify({"metrics": db, "message": "Metric's List"})


@app.route('/metrics/<int:id>', methods=['GET'])
def getMetric(id):
    print(id)
    metricFound = [
        metric for metric in db if metric['id'] == id]
    if(len(metricFound) > 0):
        return jsonify({"metric": metricFound[0]})
    return jsonify({"message": "Metric not found"})


@app.route('/metrics', methods=['POST'])
def addMetric():
    last = db[len(db)-1]
    new_metric = {
        "id": last['id']+1,
        "humedad": request.json['humedad'],
        "centigrados": request.json['centigrados'],
        "fahrenheit": request.json['fahrenheit'],
        "i_calor_c": request.json['i_calor_c'],
        "i_calor_f": request.json['i_calor_f'],
        "luz": request.json['luz'],
        "last_update": datetime.now().strftime("%Y/%m/%d"),
    }
    print(new_metric)
    db.append(new_metric)
    return jsonify({"message": "Metric addes successfully", "metric": new_metric})


@app.route('/metrics/<int:id>', methods=['PUT'])
def editMetric(id):
    metricFound = [
        metric for metric in db if metric['id'] == id]
    if(len(metricFound) > 0):
        metricFound[0]['humedad'] = request.json['humedad']
        metricFound[0]['centigrados'] = request.json['centigrados']
        metricFound[0]['fahrenheit'] = request.json['fahrenheit']
        metricFound[0]['i_calor_c'] = request.json['i_calor_c']
        metricFound[0]['i_calor_f'] = request.json['i_calor_f']
        metricFound[0]['luz'] = request.json['luz']
        metricFound[0]['last_update'] = datetime.now().strftime("%Y/%m/%d")
        return jsonify({
            "message": "Metric Updated",
            "metric": metricFound[0]
        })
    return jsonify({"message": "Metric not found"})


@app.route('/metrics/<int:id>', methods=['DELETE'])
def deleteMetric(id):
    metricFound = [
        metric for metric in db if metric['id'] == id]
    if(len(metricFound) > 0):
        db.remove(metricFound[0])
        return jsonify({
            "message": "metric deleted",
            "metrics": db
        })


if(__name__) == '__main__':
    app.run(debug=True, port=4000)
