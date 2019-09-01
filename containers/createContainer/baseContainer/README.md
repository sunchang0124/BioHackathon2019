# How to read data from an endpoint?

```
import functions
import os

inputObjects = { "sparqlQuery": "SELECT * WHERE { ?s ?p ?o }" }
functions.getData(inputObjects)
```

However, the script reads the environment variables given to the docker image to know which data service it offers (CSV file, SPARQL endpoint, or FileService). Usually, this is specified in the configuration of the client in the PyTaskManager. To override it in your test, add the following environment variables:

* endpointType = {CSV,SPARQL,FileService}
* endpointUrl = <location_of_service_or_data>

In python, you can mock this (temporarily, by using the following lines before calling `functions.getData()`:

```
os.environ["endpointType] = "SPARQL"
os.environ["endpointUrl"] = "http://sparql.cancerdata.org/namespace/johan/sparql"
```
