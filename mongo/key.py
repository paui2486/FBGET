from pymongo import MongoClient

client = MongoClient('mongodb://192.168.120.103:27017/',
                    username='paul2486',
                    password='pauli<3breaktime',
                    authSource='admin',
                    authMechanism='SCRAM-SHA-1')