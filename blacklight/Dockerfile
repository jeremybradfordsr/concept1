FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive

#setup python3 and supervisor
RUN apt-get update && apt-get -y --no-install-recommends install python3 python3-watchdog supervisor

#setup container specific software
RUN apt-get -y --no-install-recommends install rails ruby-dev openjdk-8-jdk sudo ruby-nokogiri build-essential libxml2-dev zlib1g-dev

#Setup container
RUN useradd -m -d /home/blacklight blacklight && su && chmod 777 -R /tmp && chmod o+t -R /tmp
COPY files/blacklight-sudo /etc/sudoers.d/blacklight
COPY files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD files /home/blacklight/

#Install blacklight
RUN gem install solr_wrapper
USER blacklight
WORKDIR /home/blacklight
RUN rails new blacklight -m https://raw.github.com/projectblacklight/blacklight/master/template.demo.rb
USER blacklight

#Run solr and blacklight
USER root
RUN chmod 777 /tmp
CMD ["/usr/bin/supervisord"]
