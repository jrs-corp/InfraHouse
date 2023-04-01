FROM quay.io/centos/centos:stream9
RUN yum install -y yum-utils
RUN yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
RUN yum -y install terraform

# Update package index and install necessary packages
RUN yum update -y && \
    yum install -y epel-release && \
    yum install -y python3 && \
    yum install -y python3-pip gcc python3-devel openssl-devel && \
    yum clean all

# # RUN yum install -y python3
RUN pip3 install flask
RUN pip3 install flask-cors
WORKDIR infra
COPY . /infra
#CMD python3 main.py
RUN curl -sL https://rpm.nodesource.com/setup_14.x | bash -
RUN yum install nodejs -y
RUN yum install tmux -y
WORKDIR /infra/frontend
RUN npm install
WORKDIR /infra
RUN chmod +x start.sh
ENTRYPOINT ["/bin/bash", "./start.sh"]
#CMD npm start

