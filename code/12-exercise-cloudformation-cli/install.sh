#!/usr/bin/env bash

# install python

# upgrade pip
python3.7 -m pip install --upgrade pip

# install aws-cli using python pip
# see http://docs.aws.amazon.com/cli/latest/userguide/installing.html
python3.7 -m pip install awscli --upgrade --user
# it is possible to aws-cli install version 2
# https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html

# configure profile
aws configure --profile admin

