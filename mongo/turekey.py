from pymongo import MongoClient

client = MongoClient('mongodb://35.234.28.186:27017/',
                    username='breaktime',
                    password='1qaz2wsxcde3',
                    authSource='partner',
                    authMechanism='SCRAM-SHA-1')