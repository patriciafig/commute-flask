from google.transit import gtfs_realtime_pb2
import urllib
from flask import Flask
import json
from pprint import pprint

app = Flask(__name__)

# export PATH=/Users/patricia/Documents/Work/Workspace/iOS/swift-protobuf/swift-protobuf:$PATH

@app.route("/vehiclePosition")
def getVehiclePosition():
    vehilceFile = 'VehiclePosition.json'
    with open(vehilceFile) as data_file:
        data = json.load(data_file)
        return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


@app.route("/tripUpdate")
def getTripUpdate():
    vehilceFile = 'TripUpdate.json'
    with open(vehilceFile) as data_file:
        data = json.load(data_file)
        return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == "__main__":
    app.run()
