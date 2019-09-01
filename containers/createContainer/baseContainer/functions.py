import pandas as pd
import json
from SPARQLWrapper import SPARQLWrapper, JSON
import requests
import shutil
import os

def getData(inputParameters={}):
    endpointType = "CSV"
    if os.environ.get("endpointType") != None:
        endpointType = os.environ.get("endpointType")

    endpointUrl =  "https://raw.githubusercontent.com/sunchang0124/BioHackathon2019/localRunning/containers/createContainer/Party_1_Container/data_party_1.csv"
    if os.environ.get("endpointUrl") != None:
        endpointUrl = os.environ.get("endpointUrl")

    if endpointType == "CSV":
        return get_local_csv(endpointUrl)
    if endpointType == "SPARQL":
        if "sparqlQuery" not in inputParameters:
            print("Could not find sparqlQuery in input dictionary, returning None")
            return None
        myQuery = inputParameters["sparqlQuery"]
        return get_sparql_dataframe(endpointUrl, myQuery)
    if endpointType == "FileService":
        if "fileServiceObject" not in inputParameters:
            print("Could not find fileServiceObject in input dictionary, returning None")
            return None
        fileName = inputParameters["fileServiceObject"]
        return get_fileservice_file(endpointUrl, fileName)

def get_sparql_dataframe(service, query):
    """
    Helper function to convert SPARQL results into a Pandas data frame.
    """
    sparql = SPARQLWrapper(service)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query()

    processed_results = json.load(result.response)
    cols = processed_results['head']['vars']

    out = []
    for row in processed_results['results']['bindings']:
        item = []
        for c in cols:
            item.append(row.get(c, {}).get('value'))
        out.append(item)

    return pd.DataFrame(out, columns=cols)

def get_local_csv(locationPath):
    return pd.read_csv(locationPath)

def get_fileservice_file(serviceLocation, fileName):
    url = serviceLocation + ('/file/%s' % fileName)
    response = requests.get(url, stream=True)
    with open('/data/%s' % (fileName), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    return '/data/%s' % (fileName)
