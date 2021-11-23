import json

#For sending GPS data to command and telemetry
def tojson(data:dict):
        jsonString = json.dump(data)
        return jsonString
