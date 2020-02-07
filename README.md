# AppConfig Demo

The main of this project is to help people understand how to use [AWS AppConfig](https://aws.amazon.com/systems-manager/features/#AWS_AppConfig) 
with Lambda functions to retrieve config.

This repository shows how to configure AppConfig using CloudFormation, mixing it with [AWS SAM](https://aws.amazon.com/serverless/sam/).


## What is AppConfig?
AppConfig allows you to provision and manage versioned configuration documents. Config documents allow you redeploy config separately from application code. AppConfig's concepts are:
  - Applications
  - Deployments
  - Configuration


## What's does this repo do?

This project was created to test how the integration between AppConfig and AWS Lambda work together. The Lambda Function simply calls AppConfig to fetch the config and return the config body to the caller.


## Support
Please submit your questions, feature requests, and bug reports on [GitHub issues](https://github.com/sthulb/appconfig-demo/issues) page.


## How to Contribute
We welcome community contributions to ML-IO. Please read our [Contributing Guidelines](CONTRIBUTING.md) to learn more.


## License
This project is licensed under the Apache-2.0 License.