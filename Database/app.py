from datetime import datetime
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
from flask_cors import CORS

from config import *

app = Flask(__name__)
app.config['MONGO_URI'] = MONGODB_URI
mongo = PyMongo(app)
CORS(app)


@app.route('/metrics', methods=['GET'])
def getMetrics():
    metrics = mongo.db.metrics.find()
    metrics = json_util.dumps(metrics)
    return Response(metrics, mimetype='application/json')


@app.route('/metrics/<id>', methods=['GET'])
def getMetric(id):
    metric = mongo.db.metrics.find_one({'_id': ObjectId(id)})
    if(metric == None):
        return Response(json_util.dumps({'message': 'Metric not found'}), mimetype='application/json', status=404)
    return Response(json_util.dumps(metric), mimetype='application/json')


@app.route('/metrics', methods=['POST'])
def addMetric():
    body = request.json
    new_metric = {
        "humedad": body['humedad'],
        "centigrados": body['centigrados'],
        "fahrenheit": body['fahrenheit'],
        "i_calor_c": body['i_calor_c'],
        "i_calor_f": body['i_calor_f'],
        "luz": body['luz'],
        'last_update': datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
    }
    print(new_metric)
    id = mongo.db.metrics.insert(new_metric)
    new_metric['_id'] = str(id)
    return jsonify({'message': 'Metric addes successfully', 'metric': new_metric})


@app.route('/metrics/<id>', methods=['PUT'])
def editMetric(id):
    body = request.json
    metric = mongo.db.metrics.find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': {"humedad": body['humedad'],
                  "centigrados": body['centigrados'],
                  "fahrenheit": body['fahrenheit'],
                  "i_calor_c": body['i_calor_c'],
                  "i_calor_f": body['i_calor_f'],
                  "luz": body['luz'],
                  'last_update': datetime.now().strftime('%Y/%m/%d %H:%M:%S')}}
    )
    if(metric == None):
        return jsonify({'message': 'Metric not found'})

    metric['_id'] = str(metric['_id'])
    return jsonify({
        'message': 'Metric Updated',
        'metric': metric
    })


@app.route('/metrics/<id>', methods=['DELETE'])
def deleteMetric(id):
    metric = mongo.db.metrics.find_one_and_delete({'_id': ObjectId(id)})
    if(metric == None):
        return jsonify({'message': 'Metric not found'})
    metric['_id'] = str(metric['_id'])
    return jsonify({
        'message': 'metric deleted',
        'metrics': metric
    })


if(__name__) == '__main__':
    app.run(debug=True, port=4000)
