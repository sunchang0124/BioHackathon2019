docker rmi datasharing/party_2
docker build -t datasharing/party_2 .\

# Optional execution of container included
#docker run --rm --add-host dockerhost:10.0.75.1 -v %~dp0\output.txt:/output.txt datasharing/um
