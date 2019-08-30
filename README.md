# Material for BioHackathon 2019 #
Contact: Chang Sun <chang.sun@maastrichtuniversity.nl> \
Contact: Johan van Soest <johan.vansoest@maastro.nl>

This repository is the extended version of the repository from https://gitlab.com/OleMussmann/DataSharing 

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
### Prepare datasets for multiple parties ###
1. In terminal, go to **DataPrepare** folder and run ```docker build -t splitdata . ``` (You can run ```docker images``` to check if "splitdata" image is in the list)
2. Edit **input.json** file. Input how many data parties you have and which data file you use. (Details about data are described in the README.md file in "DataPrepare" folder)
3. In terminal
    - MAC users: run ```docker run --rm -v $(pwd)/output:/output sliptdata```
    - Windows users: run ```docker run --rm -v %cd%/output:/output sliptdata```
4. You will see splited datasets files in a new generated **output"** folder. Put splited datasets into data parties foler (e.g., "Party_1_Container", "Party_2_Container") 
5. If you need more data parties, copy paste one existing "Party_X_Container" and rename it.

### Setup stations at data parties ###
1. Go to _containers/createContainer_ and build the base image (contains Python 3.6 and libraries) by running:
    - ```cp -R ../../PQcrypto baseContainer/PQcrypto```
    - ```docker rmi datasharing/base``` (skip this line if it's your first time build this image)
    - ```docker build -t datasharing/base baseContainer/```
    - ```rm -R baseContainer/PQcrypto```
2. Go to each party folder (e.g., "Party_1_Container", "Party_2_Container") and edit **input.json** file. Each folder acts as a data party. 
    - Give an unique name to "party_name" (different from other parties)
    - Input the name of the data file
    - Give the agreed on salt (data parties know and use the same salt)
    - Input personal identifier features which are used for linking purpose
3. In terminal, run
    - ```docker rmi datasharing/"your_party_name" ```(e.g., party_1)
    - ```docker build -t datasharing/"your_party_name" .\```
4. Each party needs to do step 2-3
5^. Run ```docker images``` to check if images were built successfully

### Setup another station as Trust Secure Environment (TSE) ###
1. Go to containers/TSEImage and run:
    - ```docker rmi datasharing/tse```
    - ```docker build -t datasharing/tse .\```

*** Now, all parties are ready ***
### Start the communication channel (on localhost(0.0.0.0:5001)) ###
1. Go to Local_PyTaskManager folder and run in terminal: 
    - ```docker build -t fileservice .```
2. After building the image, run: 
    - ```docker run --rm -p 5001:5001 fileservice ```

### Data parties prepare and encrypt data files ###
1. Start a new tab in terminal and go to each party's folder (e.g., Party_1_Container):
    MAC users run:
    - ```docker run --rm --add-host dockerhost:192.168.65.2 \```
    - ```-v $(pwd)/input.json:/input.json \```
    - ```-v $(pwd)/encryption:/encryption datasharing/"Your_party_name"``` (e.g., party_1) 

    Windows users run:
    - ```docker run --rm --add-host dockerhost:10.0.75.1 \```
    - ```-v %cd%/input.json:/input.json \```
    - ```-v %cd%/encryption:/encryption datasharing/"Your_party_name"``` (e.g., party_1) 
    
2. A "your_party_name_key.json" file will be generated in a new "encryption" folder. It contains: UUID of data file, verify key, and encryption key. These keys need to be send to TSE
3^. Potiental error in this step: "dockerhost:192.168.65.2" and "dockerhost:10.0.75.1" 
4^. You can run "sh S1_DataPartyRun.sh" on Mac. It combines all command lines into one file.

### Execution at TSE ###
1. Go to _containers/TSEImage_ and edit **security_input.json**:
    - Give names of all data parties
    - and input data file UUIDs, encrypt keys, and verify keys from all data parties

2. Run in terminal:
    Mac users:
    - ```docker run --rm --add-host dockerhost:192.168.65.2 \```
    - ```-v $(pwd)/output:/output \```
    - ```-v $(pwd)/security_input.json:/security_input.json datasharing/tse```

    Windows users:
    - ```docker run --rm --add-host dockerhost:10.0.75.1 \```
    - ```-v %cd%/output:/output \```
    - ```-v %cd%/security_input.json:/security_input.json datasharing/tse```

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

