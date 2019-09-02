### curFolder=$(pwd)

## Run Party_1_Container get its unique encrypt key, file UUID, VerifyKey
cd containers/createContainer/Party_1_Container
docker run --rm --add-host dockerhost:192.168.65.2 \
-v $(pwd)/input.json:/input.json \
-v $(pwd)/encryption:/encryption datasharing/party_1

## Run Party_2_Container its unique encrypt key, file UUID, VerifyKey
cd ../Party_2_Container
docker run --rm --add-host dockerhost:192.168.65.2 \
-v $(pwd)/input.json:/input.json \
-v $(pwd)/encryption:/encryption datasharing/party_2

## Run Party_3_Container its unique encrypt key, file UUID, VerifyKey
cd ../Party_3_Container
docker run --rm --add-host dockerhost:192.168.65.2 \
-v $(pwd)/input.json:/input.json \
-v $(pwd)/encryption:/encryption datasharing/party_3

## Run Party_4_Container its unique encrypt key, file UUID, VerifyKey
cd ../Party_4_Container
docker run --rm --add-host dockerhost:192.168.65.2 \
-v $(pwd)/input.json:/input.json \
-v $(pwd)/encryption:/encryption datasharing/party_4