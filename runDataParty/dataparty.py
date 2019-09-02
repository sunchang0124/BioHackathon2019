import json
import func

# print(getStations(signalStation))

with open('input.json', 'r') as f:
    inputData = json.load(f)

signalStation = inputData['signalStation']
myTrain = func.defineTrain("sophia921025/dataparty:15th", inputData, 1)

clientId = inputData['party_id']
taskId = func.requestExecution(signalStation, clientId, myTrain)
print("Task submitted with ID: %s" % taskId)

results = func.getExecutionResult(signalStation, clientId, taskId)
# print(results[0])
result = json.loads(results[0]["response"])
print(result)