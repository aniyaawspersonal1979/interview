FROM centos:7
ENV ACCESS_KEY SECRET_KEY REGION_NAME BUCKET_NAME
RUN yum install python3-pip.noarch python-boto3.noarch awscli.noarch -y
WORKDIR /opt
COPY app.py /opt/
CMD ["/usr/bin/python","/opt/app.py"]
