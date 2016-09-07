SHELL=/bin/bash
ifndef ELASTICSEARCH_VERSION
ELASTICSEARCH_VERSION=5.0.0-alpha5
endif

export ELASTICSEARCH_VERSION

ELASTIC_REGISTRY=container-registry.elastic.co
BASEIMAGE=$(ELASTIC_REGISTRY)/elasticsearch/elasticsearch-alpine-base:latest
CONTAINERREGISTRY_ESIMAGE=$(ELASTIC_REGISTRY)/elasticsearch/elasticsearch:$(ELASTICSEARCH_VERSION)
CONTAINERREGISTRY_ESIMAGE_LATESTTAG=$(ELASTIC_REGISTRY)/elasticsearch/elasticsearch:latest

# Common target to ensure BASEIMAGE is latest
pull-latest-baseimage:
	docker pull $(BASEIMAGE)

# Clean up left over containers and volumes from earlier failed runs
clean-up-from-last-runs:
	docker-compose down -v && docker-compose rm -f -v

run-es-single: pull-latest-baseimage
	ES_NODE_COUNT=1 docker-compose up --build elasticsearch

run-mek-stack:       
	ES_NODE_COUNT=1 docker-compose up --build elasticsearch kibana metricbeat

