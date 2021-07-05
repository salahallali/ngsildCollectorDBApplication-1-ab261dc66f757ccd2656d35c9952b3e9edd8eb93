# ngsildCollectorDBApplication

The LAPECI Lab team is providing a platform on the top of NGSI-LD. This module provides access to historical data and their sharing among the end-user applications. It allows interacting with different applications disposed on the platform itself and those which are implemented in remote servers. In addition, it is fully interoperable with the UMU platform provided at M14.

## Requoirments
### Docker & Docker composer
### MongoDB
This is the file.yml which contain the configuration to run MongoDB server and MongoExpress with Docker composer

	version: '2'

	services:

	  mongo:
	    image: mongo
	    restart: always
	    container_name: mongo
	    ports:
	      - 0.0.0.0:27017:27017
	    environment:
	      MONGO_INITDB_ROOT_USERNAME: abdenour
	      MONGO_INITDB_ROOT_PASSWORD: iot

	  mongo-express:
	    image: mongo-express
	    restart: always
	    container_name: mongo_express
	    depends_on:
	      - 'mongo'
	    ports:
	      - 8081:8081
	    environment:
	      ME_CONFIG_BASICAUTH_USERNAME: <authentication user>
	      ME_CONFIG_BASICAUTH_PASSWORD: <authentication pwd>
	      ME_CONFIG_MONGODB_ENABLE_ADMIN: 'false'
	      ME_CONFIG_MONGODB_AUTH_USERNAME: <mongoDB user>
	      ME_CONFIG_MONGODB_AUTH_PASSWORD: <mongoDB pwd>
	      ME_CONFIG_MONGODB_SERVER: <mongo Host>
	      ME_CONFIG_MONGODB_AUTH_DATABASE: NGSI_LDCollector_DB

commands on linux 16.4
### Python3.6

	sudo apt-get install software-properties-common

	add-apt-repository ppa:deadsnakes/ppa

	sudo apt-get update

	sudo apt-get install python3.6

	sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1

	sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2

	sudo update-alternatives --config python3

###  pip3

	sudo apt update
	sudo apt install python3-pip
	pip --version


### Django

	python -m pip3 install Django
  
### Packages
    pip3 install djongo
    pip3 install djangorestframework
    pip3 install pymongo   
    pip3 install django-crispy-forms
    pip3 install python-dateutil


  


## To run the application server 
	python3.6  manage.py runserver 0.0.0.0:80
