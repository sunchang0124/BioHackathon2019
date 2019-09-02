# Material for BioHackathon 2019

To clone this branch: 

```shell
git clone https://github.com/sunchang0124/BioHackathon2019.git
```

## Prerequisites

Hardware: 

- Windows 10 (fall creators update or higher)
- macOS 10.13 (High Sierra)
- Ubuntu 16.04, 17.10 or 18.04
- Moderately recent CPU (minimum i5 processor)
- 8 GB of RAM (not occupied by many other applications/services)

## Software

- Docker Community Edition 
  - native on Ubuntu [Install](https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository)
  - for Windows [Install](https://hub.docker.com/editions/community/docker-ce-desktop-windows)
  - for Mac [Install](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
- Python 3.6 (with pip as dependency manager)

## Test with URL connection 

We've set up three stations - two for data parties and one for Trusted Secure Environment on "http://biohack.personalhealthtrain.net" 

```shell
[{'id': 1,
  'last_seen': '2019-09-02 19:14:13.829209',
  'name': 'Trusted Secure Environment (TSE)'},
 {'id': 2,
  'last_seen': '2019-09-02 19:14:17.864963',
  'name': 'Data Party A'},
 {'id': 3,
  'last_seen': '2019-09-02 19:14:14.689868',
  'name': 'Data Party B'}]
```

### 0. Pull docker images from Docker Hub

In your terminal: 

```shell
docker pull sophia921025/baseimage
docker pull sophia921025/dataparty
docker pull sophia921025/tse
```

If you want to know the scripts in the images, please check LocalTest folder in this repo. 

### 1. Use Docker container to run:

1. Go to **DataParty** folder, run

```shell
docker build -t rundataparty .
```

2. Stay in the same folder, edit **input.json** file:

```shell
{
  "party_id": 2, # from above information
  "party_name": "party_1", # unique name of data party
    "data_file": "https://raw.githubusercontent.com/sunchang0124/BioHackathon2019/localRunning/containers/createContainer/Party_4_Container/data_party_4.csv", # path to data file
    "salt_text": "apple", # the agreed on salt (all data parties use the same salt)
    "id_feature": ["housenum", "zipcode", "date_of_birth", "sex"], ## personal identifier features used for linking purpose
    "signalStation":"http://biohack.personalhealthtrain.net" # the connecting url
}
```

3. Mac/Linux:

```shell
docker run --rm -v $(pwd)/input.json:/input.json rundataparty
```

​		Windows:

```shell
docker run --rm -v %cd%/input.json:/input.json rundataparty
```

3. Go to TSE folder, run

```shell
docker build -t runtse .
```

4. Stay in the same folder, edit **TSEinput.josn** file:

```json
{"signalStation":"http://biohack.personalhealthtrain.net",
        "parties": ["party_1","party_2"],
        "party_1fileUUID": " ", 
        "party_1encryptKey": " ", 
        "party_1verifyKey": " ",
        "party_4fileUUID": " ", 
        "party_4encryptKey": " ", 
        "party_4verifyKey": " "}
```

5. Mac/Linux

```shell
docker run --rm -v $(pwd)/TSEinput.json:/TSEinput.json runtse
```

​		Windows

```shell
docker run --rm -v %cd%/TSEinput.json:/TSEinput.json runtse
```

### 2. Or use Jupyter Notebook: 

1. Open and run: **TestInfra.ipynb**



## Try everything on your local machine

Please go to LocalTest folder and follow the instruction