FROM fedora:23

MAINTAINER stagiaire

RUN dnf -y update \
  && dnf -y install python-devel \
  && dnf clean all \
  && python3 -m pip install -U pip \
  && pip3 install virtualenv \
  && pip3 install flask \
  && pip3 install flask_script \
  && pip3 install flask_bootstrap \
  && pip3 install flask_moment \
  && pip3 install flask_wtf \
  && mkdir static \
  && mkdir templates

EXPOSE 5000

COPY static/* static/
COPY templates/* templates/
COPY hello.py .

ENTRYPOINT ["python3", "hello.py", "runserver"]
