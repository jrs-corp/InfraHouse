## InfraHouse
Housing Infrastructure for Small Business.

### Development Build Status
[![Build Status](https://dev.azure.com/sulabhshrestha/InfraHouse/_apis/build/status%2FInfraHouse-Develop?branchName=develop)](https://dev.azure.com/sulabhshrestha/InfraHouse/_build/latest?definitionId=10&branchName=develop) 

### Staging Build Status
[![Build Status](https://dev.azure.com/sulabhshrestha/InfraHouse/_apis/build/status%2FInfraHouse-Staging?branchName=stage)](https://dev.azure.com/sulabhshrestha/InfraHouse/_build/latest?definitionId=9&branchName=stage)

### Production Build Status
[![Build Status](https://dev.azure.com/sulabhshrestha/InfraHouse/_apis/build/status%2FInfraHouse-Production?branchName=main)](https://dev.azure.com/sulabhshrestha/InfraHouse/_build/latest?definitionId=8&branchName=main)

## Motivation:
This DevOps project has been successfully completed with the primary goal of providing small to medium companies with a user-friendly tool for deploying their code on any platform. The project involved dividing the codebase into three stages: development, staging, and production, each with its pipelines and releases. The deployment VMs were created on Azure Cloud and connected with Deployment Groups on Azure DevOps. A Variable group was used to connect sensitive variables on Azure DevOps. The code was stored on GitHub, with Flask and Python being used to handle the backend side. A REST API was created, which was consumed by a frontend built with React and Material-UI.
The program's primary aim was to take input from customers on where they wished to deploy their code and offer them the option to choose their cloud. After selecting their cloud, the backend used Terraform code to create the VM and deploy the code into the newly created VM. Customers could choose to send their code repository (public) or just the docker registry link.
The project was completed within the semester, and it went live on April 6th, 2023. Production support followed until the project presentation. Each team member was assigned a task ranging from build, testing, to documentation. Detailed project activity was discussed in this document, and the objective of providing a tool for small to medium companies to deploy their code based on any platform was achieved.

## Architecture:
![image](https://github.com/jrs-corp/InfraHouse/assets/13358738/25b07882-73a8-47a0-b9ee-50c1571c1009)

## Prerequisites:
1. AWS Cloud
2. Google Cloud
3. Oracle Cloud
4. Azure Cloud
5. Python
6. Javascript
7. Material UI
8. Terraform

## Replication Steps:
Clone the code, install the libraries and make sure that the host machine has permission to create instances on AWS, Azure, GCP and Oracle Cloud.
