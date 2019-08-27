cp -R ../../PQcrypto baseContainer/PQcrypto
docker rmi datasharing/base
docker build -t datasharing/base baseContainer/
rm -R baseContainer/PQcrypto

# if you want to run the container in a command line, and mount the PQcrypto to a local folder, uncomment the line below
# docker run -it datasharing/base /bin/bash
