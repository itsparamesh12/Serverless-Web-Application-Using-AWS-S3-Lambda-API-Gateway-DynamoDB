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
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/09a3da3f-75d1-4fd5-ae15-2a3a5187a4fd" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/47604fb1-a3af-4020-ba26-05d343a0def9" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cd65542c-6f74-4357-abde-a380a218e5fd" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/61f555c9-8060-400e-825a-bff8c0db5748" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f6f2fa50-b516-4ef9-84ec-0362c9c794e4" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d8533593-9289-4fc2-8a18-8daeecbf0d1d" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d38dc619-157d-46f0-b8f7-e2acee0fd135" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/bce65f13-5f0d-433f-9323-2ed1c1db6922" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/dac92801-5752-4b07-91ec-da75a737dfb5" />

### How It Works
1. User enters base and exponent.
2. API Gateway triggers Lambda function.
3. Lambda computes result and stores it in DynamoDB.
4. Response is displayed on the frontend.
