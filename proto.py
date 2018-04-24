from google.transit import gtfs_realtime_pb2
import urllib
from flask import Flask
import proto_pb2

app = Flask(__name__)

# export PATH=/Users/patricia/Documents/Work/Workspace/iOS/swift-protobuf/swift-protobuf:$PATH

@app.route("/trafficUpdates")
def getTrafficUpdates():
    contacts = []
    feed = gtfs_realtime_pb2.FeedMessage()
    response = urllib.urlopen('/Users/patricia/Desktop/VehiclePosition.pb')
    feed.ParseFromString(response.read())

    for entity in feed.entity:
        if entity.vehicle.HasField('trip'):
            contact = proto_pb2.Vehicle()
            contact.Trip.route_id = entity.vehicle.trip.route_id
            print(contact)
            contacts.append(contact)

    print(contacts)
    vehicles = proto_pb2.Vehicles()
    vehicles.vehicle.extend(contacts)
    str = vehicles.SerializeToString()

    return str


if __name__ == "__main__":
    app.run()
