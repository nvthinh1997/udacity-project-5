# Cloud DevOps Engineer Capstone Project

This project represents the successful completion of the last final Capstone project and the Cloud DevOps Engineer Nanodegree at Udacity.
- Github: https://github.com/nvthinh1997/udacity-project-5
- Docker: https://hub.docker.com/r/nvthinh1997/capstone-project
- CircleCI: [![CircleCI](https://circleci.com/gh/circleci/circleci-docs.svg?style=svg)](https://circleci.com/gh/nvthinh1997/udacity-project-5)
## What did I learn?

In this project, I applied the skills and knowledge I developed throughout the Cloud DevOps Nanodegree program. These include:
- Working in AWS
- Using Circle CI to implement Continuous Integration and Continuous Deployment
- Building pipelines
- Working with Ansible and CloudFormation to deploy clusters
- Building Kubernetes clusters
- Building Docker containers in pipelines

## Application

The Application is based on a python3 script using <a target="_blank" href="https://flask.palletsprojects.com">flask</a> to render a simple webpage in the user's browser (and base on project 4).
A requirements.txt is used to ensure that all needed dependencies come along with the Application.

## Kubernetes Cluster

I used AWS CloudFormation to deploy the Kubernetes Cluster.
The CloudFormation Deployment can be broken down into four Parts:
- **Networking**, to ensure new nodes can communicate with the Cluster
- **Elastic Kubernetes Service (EKS)** is used to create a Kubernetes Cluster
- **NodeGroup**, each NodeGroup has a set of rules to define how instances are operated and created for the EKS-Cluster
- **Management** is needed to configure and manage the Cluster and its deployments and services. I created two management hosts for extra redundancy if one of them fails.

#### List of deployed Stacks:
![CloudFormation](./screenshots/cloud-formation-stack.png)

#### List of deployed Instances:
![Show Instances](./screenshots/ec2-instances.png)

## CircleCi - CI/CD Pipelines

I used CircleCi to create a CI/CD Pipeline to test and deploy changes manually before they get deployed automatically to the Cluster using Ansible.

#### From Zero to Hero demonstration:

![CircleCi Pipeline](./screenshots/pipeline.png)

## Linting using Pylint and Hadolint

Linting is used to check if the Application and Dockerfile is syntactically correct.
This process makes sure that the code quality is always as good as possible.

#### This is the output when the step fails:

![Linting step fail](./screenshots/lint-failed.png)


#### This is the output when the step passes:

![Linting step fail](./screenshots/lint-success.png)

## Upload Docker Image After Successful Build

![Upload Docker](./screenshots/docker-repo.png)

## Access the Application

After the EKS-Cluster has been successfully configured using Ansible within the CI/CD Pipeline, I checked the deployment and service log on pipeline as follows:

```
changed: [18.207.197.142] => {
    "changed": true,
    "cmd": "./bin/kubectl get deployments",
    "delta": "0:00:01.726428",
    "end": "2022-11-07 06:29:19.856893",
    "invocation": {
        "module_args": {
            "_raw_params": "./bin/kubectl get deployments",
            "_uses_shell": true,
            "argv": null,
            "chdir": "/root",
            "creates": null,
            "executable": null,
            "removes": null,
            "stdin": null,
            "stdin_add_newline": true,
            "strip_empty_ends": true,
            "warn": false
        }
    },
    "msg": "",
    "rc": 0,
    "start": "2022-11-07 06:29:18.130465",
    "stderr": "",
    "stderr_lines": [],
    "stdout": "NAME                          READY   UP-TO-DATE   AVAILABLE   AGE\n****************-deployment   2/2     2            2           121m",
    "stdout_lines": [
        "NAME                          READY   UP-TO-DATE   AVAILABLE   AGE",
        "****************-deployment   2/2     2            2           121m"
    ]
}

changed: [18.207.197.142] => {
    "changed": true,
    "cmd": "./bin/kubectl get services",
    "delta": "0:00:01.804204",
    "end": "2022-11-07 06:29:22.148893",
    "invocation": {
        "module_args": {
            "_raw_params": "./bin/kubectl get services",
            "_uses_shell": true,
            "argv": null,
            "chdir": "/root",
            "creates": null,
            "executable": null,
            "removes": null,
            "stdin": null,
            "stdin_add_newline": true,
            "strip_empty_ends": true,
            "warn": false
        }
    },
    "msg": "",
    "rc": 0,
    "start": "2022-11-07 06:29:20.344689",
    "stderr": "",
    "stderr_lines": [],
    "stdout": "NAME                          TYPE           CLUSTER-IP       EXTERNAL-IP                                                               PORT(S)        AGE\nkubernetes                    ClusterIP      10.100.0.1       <none>                                                                    443/TCP        133m\n*******************-service   LoadBalancer   10.100.195.109   a3236719219e6478b85a7e5619f26903-1346629195.*********.elb.amazonaws.com   80:31154/TCP   121m",
    "stdout_lines": [
        "NAME                          TYPE           CLUSTER-IP       EXTERNAL-IP                                                               PORT(S)        AGE",
        "kubernetes                    ClusterIP      10.100.0.1       <none>                                                                    443/TCP        133m",
        "*******************-service   LoadBalancer   10.100.195.109   a3236719219e6478b85a7e5619f26903-1346629195.*********.elb.amazonaws.com   80:31154/TCP   121m"
    ]
}
```

Public LB DNS: http://a3236719219e6478b85a7e5619f26903-1346629195.us-east-1.elb.amazonaws.com

![Access LB DNS](./screenshots/lb_dns.png)
