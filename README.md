![main](https://github.com/ethanriverpage/FSA.EnterpriseAssessment/actions/workflows/main.yml/badge.svg) [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit) [![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Password Salter

### Password Salter (written from scratch in Python)
#### Supports dynamic & static salting, using a REST API to pull salts, & more!
##### Built to be dependency-less
> This was done as part of an assessment for Fullstack Academy, used to test knowledge CI/CD pipeline deployment, AWS Lambda functions, among others.
> [Click here](https://www.youtube.com/watch?v=9SyqU9XVHAk) for a video presentation I gave breaking down this project.

#### This project uses:
* Python as primary language
* [Bandit](https://github.com/PyCQA/bandit) for security testing
* [pylint](https://github.com/PyCQA/pylint) for linting & formatting
* [GitHub Actions](https://github.com/features/actions) for CI/CD pipeline
* [AWS CLI](https://aws.amazon.com/cli/) for deployment to S3 & Lambda.
* [GitHub Actions Secrets](https://docs.github.com/en/rest/actions/secrets) for storing environment variables
```
Environment Variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION`
```
