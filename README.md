# Serverless-Web-Application-Using-AWS-S3-Lambda-API-Gateway-DynamoDB
Developed a real-time serverless web application using AWS S3, Lambda, API Gateway, and DynamoDB to perform dynamic mathematical calculations. Implemented a scalable, event-driven architecture demonstrating full integration of modern AWS cloud services.

---------------------------------------------------------
# Serverless Web Application Using AWS S3, Lambda, API Gateway & DynamoDB

### About
A real-time serverless web application built using AWS managed services to calculate powers of numbers dynamically.

### Tech Stack
- AWS Lambda (Backend logic)
- Amazon API Gateway (API handling)
- Amazon S3 (Frontend hosting)
- Amazon DynamoDB (Data storage)
- AWS IAM (Access control)

### Architecture
Frontend (HTML/JS in S3) → API Gateway → Lambda → DynamoDB

### Screenshots
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9ca003b5-812f-4d6e-a533-87989c96fdb6" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6a536424-e454-44aa-a703-3b5e13e1ca1e" />



### How It Works
1. User enters base and exponent.
2. API Gateway triggers Lambda function.
3. Lambda computes result and stores it in DynamoDB.
4. Response is displayed on the frontend.
