FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive
# tutum/apache-php

#setup python3 and supervisor
RUN apt-get update && apt-get -y --no-install-recommends install python3 python3-watchdog supervisor

#Install container software 
RUN apt-get -y install --no-install-recommends python3-pip watchdog apache2 php libapache2-mod-php python3-requests

#Setup container
RUN mkdir /var/www/html/uploads && chown www-data:www-data /var/www/html/uploads && chmod -R 755 /var/www/html/uploads
COPY files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD files /root/

#Run Supervisor.d( Apache and dirwatch.py)
CMD ["/usr/bin/supervisord"]
EXPOSE 80
