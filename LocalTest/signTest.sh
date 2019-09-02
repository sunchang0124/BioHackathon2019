openssl genrsa -out privatekey.pem 2048
openssl req -new -x509 -key privatekey.pem -out publickey.cer -days 1825
openssl pkcs12 -export -out public_privatekey.pfx -inkey privatekey.pem -in publickey.cer

docker trust key load --name johan privatekey.pem

################################################################################################
# Note: you should have push rights to the given repository, otherwise signing won't work
################################################################################################

# Sign the repository
docker trust signer add --key publickey.cer johan datasharing/base
# check whether the repository has been signed
docker trust inspect --pretty datasharing/base

# Sign the actual image
docker trust sign datasharing/base:latest
# This process also directly uploads it to the docker registry
docker trust inspect --pretty datasharing/base:latest

