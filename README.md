# Student API

## Overview
This project provides a simple RESTful API to manage students with basic CRUD operations.

## Project Setup
1. **Clone Repository**:
   ```bash
   git clone https://github.com/yashrajput0811/MidtermExam-RemoteData.git
   cd your-repository
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Locally**:
   ```bash
   python app.py
   ```

   The API will run on `http://localhost:5000`.

## API Endpoints
- `GET /students`: Retrieve all students.
- `GET /students/{id}`: Retrieve a student by ID.
- `POST /students`: Add a new student.
- `PUT /students/{id}`: Update a student by ID.
- `DELETE /students/{id}`: Delete a student by ID.

## Deploy to Azure
- Follow the instructions in `.github/workflows/azure-deploy.yml` for CI/CD.
- Configure Azure secrets in GitHub.
