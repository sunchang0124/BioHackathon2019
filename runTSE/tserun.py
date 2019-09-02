### AT TSE ###
import json
import func

with open('TSEinput.json', 'r') as f:
    inputData = json.load(f)

signalStation = inputData['signalStation']
myTrain = func.defineTrain("sophia921025/tse:4thtry", inputData, 1)

clientId = 1
taskId = func.requestExecution(signalStation, clientId, myTrain)
print("Task submitted with ID: %s" % taskId)

results = func.getExecutionResult(signalStation, clientId, taskId)
print(results[0]["response"])