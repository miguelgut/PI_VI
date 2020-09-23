from pymongo import MongoClient
import psutil
import time
import datetime
import pprint

cliente = MongoClient('mongodb://app:ucpel_2020@ucpelpivi-shard-00-00.h3o8t.gcp.mongodb.net:27017,ucpelpivi-shard-00-01.h3o8t.gcp.mongodb.net:27017,ucpelpivi-shard-00-02.h3o8t.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-13yvxa-shard-0&authSource=admin&retryWrites=true&w=majority', 27017)

banco = cliente.pc_data
colecao = banco.pi_vi
pp = pprint.PrettyPrinter(indent=4);

start = datetime.datetime(2020, 8, 27)
end = datetime.datetime(2020, 8, 27, 23, 59, 59)


print(colecao.count_documents({"date":{"$gte":start, "$lt":end}}))

for post in colecao.find({"date":{"$gte":start, "$lt":end}}).sort("date"):
  pp.pprint(post)
 
