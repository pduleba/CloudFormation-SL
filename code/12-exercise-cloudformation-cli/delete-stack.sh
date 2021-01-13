#!/usr/bin/env bash

# delete cloudformation template
aws cloudformation delete-stack --stack-name cloudformation-cli-stack \
  --profile admin --region eu-west-1
