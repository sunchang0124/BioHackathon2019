### curFolder=$(pwd)

cd containers/createContainer/baseContainer
sh build.sh

## Run Party_1_Container get its unique encrypt key, file UUID, VerifyKey
cd containers/createContainer/Party_1_Container
docker build -t datasharing/party_1 .
docker run --rm --add-host dockerhost:192.168.65.2 \
-v $(pwd)/input.json:/input.json \
-v $(pwd)/encryption:/encryption datasharing/party_1

## Run Party_2_Container its unique encrypt key, file UUID, VerifyKey
cd ../Party_2_Container
docker build -t datasharing/party_2 .
docker run --rm --add-host dockerhost:192.168.65.2 \
-v $(pwd)/input.json:/input.json \
-v $(pwd)/encryption:/encryption datasharing/party_2

## Run Party_2_Container its unique encrypt key, file UUID, VerifyKey
cd ../Party_3_Container
docker build -t datasharing/party_3 .
docker run --rm --add-host dockerhost:192.168.65.2 \
-v $(pwd)/input.json:/input.json \
-v $(pwd)/encryption:/encryption datasharing/party_3
