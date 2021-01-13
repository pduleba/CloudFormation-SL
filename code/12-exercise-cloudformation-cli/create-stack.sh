#!/usr/bin/env bash

# create cloudformation template
aws cloudformation create-stack --stack-name cloudformation-cli-stack \
  --template-body file://cfn-template.yaml \
  --parameters file://cfn-template-parameters.json \
  --profile admin --region eu-west-1

# some options:
# [--disable-rollback | --no-disable-rollback]
# [--rollback-configuration <value>]
# [--timeout-in-minutes <value>]
# [--notification-arns <value>]
# [--capabilities <value>]
# [--resource-types <value>]
# [--role-arn <value>]
# [--on-failure <value>]
# [--stack-policy-body <value>]
# [--stack-policy-url <value>]
# [--tags <value>]
# [--client-request-token <value>]
# [--enable-termination-protection | --no-enable-termination-protection]
# [--cli-input-json <value>]
# [--generate-cli-skeleton <value>]
