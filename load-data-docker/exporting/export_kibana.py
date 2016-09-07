__author__ = 'dale'
import elasticsearch
import argparse
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from elasticsearch import helpers
import os
import simplejson as json
import sys
import io

parser = argparse.ArgumentParser(description='Export .Kibana Index in Bulk Indexing Format')
parser.add_argument('--host',help='host name')
parser.add_argument('--port',help='port')
parser.add_argument('--filename',help='filename')
parser.add_argument('--username',help='username')
parser.add_argument('--password',help='password')
parser.set_defaults(host='localhost',port="9200",filename="kibana.json",username="elastic",password="changeme")
args = parser.parse_args()

es=None
if args.username and args.password:
    es = Elasticsearch(["%s:%s"%(args.host,args.port)],http_auth=(args.username,args.password))
else:
    es = Elasticsearch([args.host+":"+args.port])

output_file=open(args.filename,"w")
results=es.search(body={"query": {"match_all": {}},"size":1000},index=".kibana")
for doc in results["hits"]["hits"]:
    doc_content=json.dumps(doc["_source"])
    output_file.write(json.dumps({ "index" : { "_index" : ".kibana","_id":doc["_id"],"_type" : doc["_type"]}})+'\n')
    output_file.write(doc_content+'\n')
output_file.close()


kibana_mapping=IndicesClient(es).get_mapping(".kibana")[".kibana"]
kibana_settings=IndicesClient(es).get_settings(".kibana")[".kibana"]
kibana_mapping["settings"]={"index":{}}
kibana_mapping["settings"]["index"]["number_of_shards"]=kibana_settings["settings"]["index"]["number_of_shards"]
kibana_mapping["settings"]["index"]["number_of_replicas"]=kibana_settings["settings"]["index"]["number_of_replicas"]
mapping_file=open("kibana_mapping.json","w")
mapping_file.write(json.dumps(kibana_mapping))
mapping_file.close()
