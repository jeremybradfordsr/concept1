FROM solr
USER root
RUN apt-get update && apt-get -y install cron
USER solr
COPY cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN crontab /etc/cron.d/cron
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["solr-foreground"]
