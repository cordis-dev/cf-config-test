# ignore DL3002
# allow DL3006 and DL3003
FROM busybox
USER root
WORKDIR /usr/src/app
RUN cd /usr/src/app && git clone git@github.com:lukasmartinelli/hadolint.git 
