# http://3.108.133.100/myportfolio/

# Menu-Based Project

This project is a comprehensive, menu-driven application that integrates a wide range of tasks and technologies from my curriculum, providing a hands-on, practical approach to mastering various domains in software development and cloud computing.

## Overview

The project is designed as a multi-functional tool where each menu option represents a different task, each focused on specific areas of expertise. The goal is to create an interactive and versatile environment where users can navigate through tasks related to:

- **Frontend Development**: Implementation of responsive and dynamic user interfaces using HTML, CSS, JavaScript, and modern frameworks like ReactJS.
- **Python Programming**: Includes scripts and applications that showcase automation, data manipulation, and integration with various APIs.
- **GenAIops**: Integration of AI-driven operations to automate and optimize workflows, blending AI with DevOps practices.
- **Docker**: Containerization of applications to ensure consistency across different environments, supporting microservices architecture.
- **Full Stack Development**: A complete web application stack that includes frontend, backend (Node.js, Express), and database management (MongoDB, MySQL).
- **Databases**: Tasks involving CRUD operations, complex queries, and database design for both SQL and NoSQL databases.
- **Linux Operations**: Includes shell scripting, system administration tasks, and network management using Linux.
- **AWS Services**: Utilization of various AWS cloud services for deployment, storage, and computing, integrating tools like EC2, S3, Lambda, and more.

## Purpose

This project serves as a capstone to my learning journey, demonstrating my ability to integrate and apply knowledge across multiple domains. It is designed to be a versatile toolkit that not only serves educational purposes but also provides practical, real-world solutions.

---

## Project Deployment
The project is deployed on httpd (apache)webserver on AWS for that we need:
1. To  launch an instance on AWS with allowing HTTP, HTTPS, and all traffics.
2. Then go to root user on the instance.
3. Then install the httpd webserver.
   ``` yum install httpd ```
4. Then start and enable the httpd webserver.
   ``` systemctl start httpd ```
   ```systemctl enable httpd ```
   

## Install Python Dependencies
Install python on aws instance.
``` yum install python3-pip ```

To install the required Python dependencies, use the following commands:

```
pip install twilio
pip install google-generativeai
pip install geopy
pip install paramiko
pip install boto3
pip install requests
pip install beautifulsoup4
pip install secure-smtplib

```
For docker we need to install docker first.
 ``` yum install docker ```

Then start and enable docker.
``` systemctl start docker ```
``` systemctl enable docker ```


Install all dependencies at once:

 
``` pip install twilio google-generativeai geopy paramiko boto3 requests beautifulsoup4 secure-smtplib ```

Dependency Descriptions
twilio: Provides a Python library for interacting with the Twilio API, used for sending and receiving SMS, voice calls, and other communications. It's commonly used for integrating messaging or communication features into applications.

google-generativeai: Likely related to Google's Generative AI services. It may provide functionality for interacting with Google's AI models for generating text, images, or other media. The exact use depends on the specific APIs and services provided.

geopy: A Python library for geocoding and reverse geocoding, converting addresses into geographical coordinates and vice versa. It's useful for applications involving location data, such as mapping or location-based services.

paramiko: A library for working with SSH (Secure Shell) in Python. It allows secure connections to remote machines, executing commands and transferring files. It's often used for automating administrative tasks on remote servers.

boto3: The Amazon Web Services (AWS) SDK for Python, providing an interface for interacting with AWS services like S3, EC2, DynamoDB, and more. It's essential for managing AWS resources programmatically.

requests: A popular Python library for making HTTP requests. It simplifies sending HTTP requests and handling responses, useful for interacting with web APIs and performing web scraping.

beautifulsoup4: A library for parsing HTML and XML documents. It provides tools for extracting and manipulating data from web pages, making it useful for web scraping and parsing content.

secure-smtplib: An enhanced version of Python’s smtplib with support for secure connections. It's used for sending email via SMTP with added security features, such as TLS/SSL encryption.
 
 
