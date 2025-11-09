# Serverless Web Application Using AWS S3, Lambda, API Gateway & DynamoDB
### About
A real-time serverless web application built using AWS managed services to calculate powers of a numbers dynamically.

### STEPS
1.Create IAM role to connect Lambda & DynamoDB
2.Configure lambda
3.Configure API gateway
4.Configure DynamoDB
5.Configure S3

### Tech Stack
- Frontend: HTML, CSS, JavaScript (hosted on Amazon S3)
- Backend: AWS Lambda (Backend logic)(python)
- APIs: Amazon API Gateway (API handling)
- Amazon S3 (Frontend hosting)
- Database: Amazon DynamoDB (Data storage)
- Security: AWS IAM (Access control)

### Architecture Overview
<img width="1894" height="357" alt="image" src="https://github.com/user-attachments/assets/65520332-e5f6-4844-a2e5-8460aac29c81" />
Frontend (HTML/JS in S3) → API Gateway → Lambda → DynamoDB

### Screenshots
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4001b74a-94b2-4d22-bdac-8db5633fe944" />
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
1. User enters the base and exponent on the web page.
2. The frontend sends the request to API Gateway, which triggers a Lambda function.
3. Lambda performs the calculation and stores the result in DynamoDB.
4. The output is displayed on the frontend in real time.

### Key Features
• 100% Serverless Architecture
• Real-time API Interaction
• Scalable and Cost-efficient Design
• Secure Access through AWS IAM Policies
