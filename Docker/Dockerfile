FROM ubuntu

# installation
RUN apt update && apt upgrade -y
RUN apt install python -y
RUN apt install wget -y
RUN apt install lame -y
RUN apt install build-essential -y
RUN apt install libffi-dev -y
RUN apt install git -y
RUN apt install python-dev -y

RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py

RUN wget https://github.com/mopidy/libspotify-archive/raw/master/libspotify-12.1.51-Linux-x86_64-release.tar.gz && \
    tar xvf libspotify-12.1.51-Linux-x86_64-release.tar.gz && \
    cd libspotify-12.1.51-Linux-x86_64-release/ && \
    make install prefix=/usr/local 

RUN git clone https://github.com/hbashton/spotify-ripper.git && \
    cd spotify-ripper && \
    python setup.py install

# configuration
ADD spotify_appkey.key /root/.spotify-ripper
ADD config.ini /root/.spotify-ripper/

# install processing script
ADD process_lists.py ./

# start downloading
ENTRYPOINT [ "python", "/process_lists.py" ]
