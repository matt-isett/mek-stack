FROM phusion/baseimage:latest
MAINTAINER Matthew Isett <matt.isett@elastic.co>

RUN apt-get update
COPY cpu_watch.json cpu_watch.json
COPY wait-for-elastic.sh /usr/share/wait-for-elastic.sh
COPY load-watches.sh load-watches.sh

ENTRYPOINT ["sh" "/usr/share/wait-for-elastic.sh"]
