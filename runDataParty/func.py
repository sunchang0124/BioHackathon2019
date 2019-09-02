import uuid
import json
import time
import requests

def getStations(signalStation):
    response = requests.get(signalStation + "/client")
    return json.loads(response.text)

def defineTrain(image, inputVars, runId):
    return {
        "image": image,
        "inputString": ("%s" % json.dumps(inputVars)),
        "runId": runId
    }

def requestExecution(signalStation, clientId, taskDescription):
    response = requests.post(signalStation + "/client/" + str(clientId) + "/task/add", json=taskDescription)
    taskId = json.loads(response.text)["taskId"]
    return taskId

def getExecutionResult(signalStation, clientId, taskId, wait=True):
    url = signalStation + "/client/" + str(clientId) + "/task/" + str(taskId) + "/result"
    jsonResult = json.loads(requests.get(url).text)
    
    while len(jsonResult)==0 & wait:
        time.sleep(2)
        jsonResult = json.loads(requests.get(url).text)
    
    return jsonResult