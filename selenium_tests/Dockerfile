FROM ubuntu:14.04

MAINTAINER stagiaire

# Installing needed packages
RUN apt-get update
RUN apt-get install -y python python-dev python-setuptools zlib1g-dev wget

# Installing the latest version of pip
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

# Installing the needed packages for build and run
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the sources
COPY UITests.py .

# Mount volume for tests outputs
RUN mkdir results
VOLUME /results

ENTRYPOINT ["nosetests", "UITests.py", "--with-xunit", "--xunit-file" , "/results/ui_tests.xml"]
