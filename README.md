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
1. Set up data parties and Trusted secure enviroment (IPs)
2. PyTaskManager gets ready (start listening)
3. Researcher requests access to execute analysis model on data
4. All data parties approve and hash PIs 
5. Send to TSE and do matching and linking
6. Matching result go to data parties and the researcher
7. Researcher sends analysis to TSE
8. Run model on data

