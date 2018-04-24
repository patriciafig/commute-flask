import glob

from google.protobuf import json_format
from google.transit import gtfs_realtime_pb2


def convert_pb_to_json(pb_filename):
    feed = gtfs_realtime_pb2.FeedMessage()

    with open(pb_filename, 'rb') as f:
        feed.ParseFromString(f.read())

    return json_format.MessageToJson(feed)


def main():
    # filenames = glob.glob('*.pb')
    # for filename in filenames:
    # str = 'TripUpdate.pb'
    str = 'VehiclePosition.pb'
    print("Converting file:", str)
    pb_as_json = convert_pb_to_json(str)
    json_filename = str.replace('.pb', '.json')
    with open(json_filename, 'w') as f:
        f.write(pb_as_json)


if __name__ == '__main__':
    main()

# this file converts .pb file to .json file
