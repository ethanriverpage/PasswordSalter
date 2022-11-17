![main](https://github.com/ethanriverpage/FSA.EnterpriseAssessment/actions/workflows/main.yml/badge.svg) [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit) [![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

# Password Salter

### This is a password salter, supporting dynamic salting, static salting, and usage of data from a REST API as part of a password salt.
### Built using Python, CI/CD pipeline with GitHub Actions, and deployed to an AWS S3 bucket and subsequently a Lambda function.

#### This was done as part of an assessment for a DevOps Engineering class with Fullstack Academy.

This project uses [Bandit](https://github.com/PyCQA/bandit) for automated security testing and [pylint](https://github.com/PyCQA/pylint/) for linting and formatting. Tested during CI.

This project also uses GitHub Secrets for environment variables. `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION`. 