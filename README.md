# Material for BioHackathon 2019 #
To clone this branch: 
```shell
git clone --branch localRunning https://github.com/sunchang0124/BioHackathon2019.git
```


## Prerequisites ##
Hardware: 
* Windows 10 (fall creators update or higher)
* macOS 10.13 (High Sierra)
* Ubuntu 16.04, 17.10 or 18.04

* Moderately recent CPU (minimum i5 processor)
* 8 GB of RAM (not occupied by many other applications/services)

## Software ##
* Docker Community Edition 
    - native on Ubuntu [Install](https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository)
    - for Windows [Install](https://hub.docker.com/editions/community/docker-ce-desktop-windows)
    - for Mac [Install](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
* Python 3.6 (with pip as dependency manager)


## Install the infrastructure locally ##
### 0. Prepare datasets for multiple parties  ###

#### (Example data files are in data parties folder. You can skip this step if you want) ####

1. In terminal, go to **DataPrepare** folder and run:
```shell
docker build -t splitdata .
```
(You can run `docker images` to check if "splitdata" image is in the list)
2. Edit **input.json** file

```shell
{
    "num_of_party": 4, # how many data parties you have
    "data_file": "Generated_Datasets/generated_data_5000.csv" # which data file you use
}
```

2. In terminal
- Linux/macOS:
```shell
docker run --rm -v $(pwd)/output:/output splitdata
```
- Windows:

```shell
docker run --rm -v %cd%/output:/output splitdata
```

4. You will see splited datasets files in a new generated **output"** folder. Put splited datasets into data parties foler (e.g., "Party_1_Container", "Party_2_Container") 
5. If you need more data parties, 
    - copy paste one existing "Party_X_Container" and rename it
    - Change name of the data file in **Dockerfile** ```COPY data_party_X.csv data_party_X.csv```

### 1. Setup stations at data parties ###
1. Go to **containers/createContainer**  and build the base image (contains Python 3.6 and libraries) by running:
```shell
# docker rmi datasharing/base # (uncomment this line if you built this image before)
docker build -t datasharing/base baseContainer/
```

2. Go to each party folder (e.g., "Party_1_Container", "Party_2_Container") and edit **input.json** file. Each folder acts as a data party. 
```shell
{
  "party_name": "party_1", # unique name
  "data_file": "data_party_1.csv", # file name of the data 
  "salt_text": "apple", # the agreed on salt (all data parties use the same salt)
  "id_feature": ["housenum", "zipcode", "date_of_birth", "sex"] # personal identifier features used for linking purpose
}
```

2. In terminal, run
```shell
# docker rmi datasharing/"your_party_name" # (e.g., party_1) (uncomment this line if you built this image before)

docker build -t datasharing/"your_party_name" .
```

4. Each party needs to do step 2-3
5. Run `docker images` to check if images were built successfully

### 3. Setup another station as Trust Secure Environment (TSE) ###
1. Go to containers/TSEImage and run:
```shell 
# docker rmi datasharing/tse (uncomment this line if you built this image before)

docker build -t datasharing/tse .
```

**Now, all parties are ready**

### 4. Start the communication channel (on localhost(0.0.0.0:5001)) ###
1. Go to Local_PyTaskManager folder and run in terminal: 
  
```shell
docker build -t fileservice .
```

2. After building the image, run
- Linux/macOS:
```shell
docker run --rm -p 5001:5001 -v $(pwd)/storage:/storage fileservice
```

- Windows:
```shell
docker run --rm -p 5001:5001 -v %cd%/storage:/storage fileservice
```

### 5. Data parties prepare and encrypt data files ###
1. Start a new tab in terminal and go to each party's folder (e.g., Party_1_Container):
- Linux/macOS:
```shell
docker run --rm --add-host dockerhost:192.168.65.2 \
-v $(pwd)/input.json:/input.json \
-v $(pwd)/encryption:/encryption datasharing/*Your_party_name*
```
- Windows:
```shell
docker run --rm --add-host dockerhost:10.0.75.1 \
-v %cd%/input.json:/input.json \
-v %cd%/encryption:/encryption datasharing/*Your_party_name*
```
2. A **your_party_name_key.json** file will be generated in a new **encryption** folder. It contains: UUID of data file, verify key, and encryption key. These keys need to be send to TSE

```json
{
  "party_1fileUUID": "xxxxx", 
  "party_1encryptKey": "xxxxx",
  "party_1verifyKey": "xxxxx"
}
```



### 6. Execution at TSE ###
1. Go to _containers/TSEImage_ and edit **security_input.json**:
    
```json
{
  "parties": ["party_1","party_2"],
  "party_1fileUUID": "xxxxx", 
  "party_1encryptKey": "xxxxx",
  "party_1verifyKey": "xxxxx",
  "party_2fileUUID": "yyyyy",
  "party_2encryptKey": "yyyyy",
  "party_2verifyKey": "yyyyy",
}
```



1. Run in terminal:
- Linux/macOS:
```shell
docker run --rm --add-host dockerhost:192.168.65.2 \
-v $(pwd)/output:/output \
-v $(pwd)/security_input.json:/security_input.json datasharing/tse
```

- Windows:
```shell
docker run --rm --add-host dockerhost:10.0.75.1 \
-v %cd%/output:/output \
-v %cd%/security_input.json:/security_input.json datasharing/tse
```


## How infrastructure works ##
1. Set up data parties and Trusted secure enviroment 
2. PyTaskManager gets ready (Master site start listening)
3. Researcher provide data analysis model to TSE 
    - This model should be approved by data parties
3. Data parties give inputs and build the Docker images
    - All parties have to agree on one salting key
    - Hashing and salting will be done
    - Hashed identifiers + actual data will be encrypted 
    - Send to TSE 
4. TSE receives all encrypted data files, then:
    - Verification and decryption 
    - matching and linking data
    - Run linear regression model on actual data
5. Results will be generated at TSE
6. TSE Send results back to researcher

## Contact ##
Chang Sun <chang.sun@maastrichtuniversity.nl>
Johan van Soest <johan.vansoest@maastro.nl>
This repository is the extended version of the repository from https://gitlab.com/OleMussmann/DataSharing 