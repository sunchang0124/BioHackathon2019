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
** native on Ubuntu[Install](https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository)
** for Windows [Install](https://hub.docker.com/editions/community/docker-ce-desktop-windows)
** for Mac [Install](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
* Python 3.6 (with pip as dependency manager)

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

