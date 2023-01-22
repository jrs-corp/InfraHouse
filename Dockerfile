FROM centos:7
RUN yum install -y yum-utils
RUN yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
RUN yum -y install terraform
RUN yum install -y python3
RUN pip3 install flask
WORKDIR infra
COPY . /infra
CMD python3 main.py 

