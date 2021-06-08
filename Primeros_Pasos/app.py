from db import db
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)


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
        "temperatura": request.json['temperatura'],
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
        metricFound[0]['temperatura'] = request.json['temperatura']
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
