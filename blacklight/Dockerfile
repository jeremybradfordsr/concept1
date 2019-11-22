FROM ubuntu:devel


#Setup container
ENV DEBIAN_FRONTEND noninteractive
RUN useradd blacklight -m -d /home/blacklight
RUN apt-get update && apt-get install sudo
COPY blacklight /etc/sudoers.d/blacklight
COPY blacklight_wrapper.sh /home/blacklight/blacklight_wrapper.sh
RUN chmod 777 -R /tmp && chmod o+t -R /tmp

#Install rails and dependencies
RUN apt-get -y --no-install-recommends install git-core zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev nodejs yarn libsqlite3-dev rails patch ruby-dev zlib1g-dev liblzma-dev openjdk-8-jdk

#Install blacklight
RUN gem install solr_wrapper
USER blacklight
WORKDIR /home/blacklight

RUN rails new blacklight -m https://raw.github.com/projectblacklight/blacklight/master/template.demo.rb
USER blacklight
#Run solr and blacklight
USER root
RUN chmod 777 /tmp 
USER blacklight
CMD bash blacklight_wrapper.sh
