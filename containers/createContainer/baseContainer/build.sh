cp -R ../../../PQcrypto/ ./PQcrypto
docker build --no-cache -t datasharing/base ./
rm -R ./PQcrypto
