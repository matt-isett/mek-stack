FROM phusion/baseimage:latest
MAINTAINER Matthew Isett <matt.isett@elastic.co>

RUN apt-get update
COPY cpu_watch.json cpu_watch.json
COPY wait-for-elastic.sh /usr/share/wait-for-elastic.sh
COPY load-watch.sh load-watch.sh

RUN chmod 0700 /usr/share/wait-for-elastic.sh
RUN chmod 0700 load-watch.sh

CMD ["sh", "/usr/share/wait-for-elastic.sh"]
