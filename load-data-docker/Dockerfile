FROM phusion/baseimage:latest
MAINTAINER Matthew Isett <matt.isett@elastic.co>

RUN apt-get update
COPY kibana.json kibana.json
COPY kibana_mapping.json kibana_mapping.json
COPY wait-for-elastic.sh /usr/share/wait-for-elastic.sh
COPY import_kibana_data.sh import_kibana_data.sh

RUN chmod 0700 /usr/share/wait-for-elastic.sh
RUN chmod 0700 import_kibana_data.sh

CMD ["sh", "/usr/share/wait-for-elastic.sh"]
