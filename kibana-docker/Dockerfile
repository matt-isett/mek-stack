FROM java:8-jre

RUN apt-get update
RUN apt-get install -y vim wget sudo openssh-server curl lsb-release apt-transport-https rsyslog
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl
ENV DEBIAN_FRONTEND noninteractive

#Kibana
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add -

RUN echo "deb https://packages.elastic.co/kibana/5.0.0-alpha/debian stable main" | sudo tee -a /etc/apt/sources.list.d/kibana.list
RUN apt-get update && apt-get install -y kibana
RUN /usr/share/kibana/bin/kibana-plugin install x-pack
RUN /usr/share/kibana/bin/kibana-plugin install https://github.com/gingerwizard/kibana-swimlane-vis/releases/download/5.0.0/kibana-swimlane-vis-5.0.0.zip
#Set up volumes
VOLUME /opt/config/kibana

#SSH and User Setup
RUN useradd -d /home/elastic_user -m -s /bin/bash elastic_user;
RUN echo 'elastic_user:elastic_user' | chpasswd
RUN echo "elastic_user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN echo "Defaults !requiretty" >> /etc/sudoers
RUN mkdir -p /home/elastic_user/.ssh
RUN chown -R elastic_user /home/elastic_user/.ssh
RUN chmod 0700 /home/elastic_user/.ssh
RUN touch /home/elastic_user/.ssh/authorized_keys
RUN chown elastic_user /home/elastic_user/.ssh/authorized_keys
RUN chmod 0600 /home/elastic_user/.ssh/authorized_keys
RUN mkdir /var/run/sshd

RUN echo 'root:changeMe!' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/LogLevel INFO/LogLevel VERBOSE/' /etc/ssh/sshd_config
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
EXPOSE 5601 22

# COPY kibana.yml /opt/config/kibana/kibana.yml
COPY wait-for-elastic.sh /usr/share/wait-for-elastic.sh
RUN chmod 0700 /usr/share/wait-for-elastic.sh
# RUN chmod 0700 /opt/config/kibana/kibana.yml

# RUN ["/usr/share/kibana/bin/kibana", "-c", "/opt/config/kibana/kibana.yml"] 
ENTRYPOINT ["/usr/share/wait-for-elastic.sh"]
