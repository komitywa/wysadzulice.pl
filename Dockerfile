FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /root

RUN \
    apt-get update && \
    apt-get install -y wget python gcc build-essential git python-pip && \
    wget https://nodejs.org/dist/v0.12.7/node-v0.12.7.tar.gz && \
    tar -xzf node-v0.12.7.tar.gz

WORKDIR /root/node-v0.12.7

RUN \
    ./configure && \
    make && \
    make install

WORKDIR /root

RUN rm -rf node*
RUN git clone https://github.com/komitywa/plantingjs.git

WORKDIR /root/plantingjs

RUN npm install -g gulp
RUN npm install -g bower
RUN npm install
RUN bower install --allow-root --config.interactive=false
RUN npm run build

RUN pip install Django

ADD . /root/site

WORKDIR /root/site/src

EXPOSE 8000

CMD bash -c "ln -s ../../plantingjs/dist static && python manage.py runserver"
