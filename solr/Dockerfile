FROM solr

USER root
#Install cron and copy cronjob over
RUN apt-get update && apt-get -y install cron rails nodejs
COPY cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN crontab /etc/cron.d/cron

USER solr
#Create rfaxx core
RUN /opt/solr/bin/solr create -c rfaxx; exit 0

#Run cron then solr
CMD bash /stash/solrcron.sh
