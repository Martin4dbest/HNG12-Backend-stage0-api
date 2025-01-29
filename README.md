# HNG12 Stage 0 API

The **HNG12 Stage 0 API** is a straightforward Flask-based application designed for the HNG Internship 12 (HNG12) program. This API serves as an introductory project to demonstrate my ability to create and deploy a RESTful API using **Python** and the **Flask framework**. It returns a simple JSON response, which can serve as a foundation for building more complex APIs.

As part of the **HNG12 Internship**, this project was developed to showcase my proficiency in backend development using Python. The goal of the internship is to create functional APIs that are scalable, efficient, and easy to integrate into larger systems. With this project, I’ve leveraged Flask to set up a minimalistic yet effective API with the following features:

- A **single endpoint** that responds with a success message in JSON format.
- Demonstrates fundamental concepts of **RESTful API** design, which is essential for building modern web applications.
- Provides a template for further experimentation and enhancement, where additional features and endpoints can be added as required.

## Project Overview

The **HNG12 Stage 0 API** is a **basic** and **lightweight** Flask application, developed to introduce developers to the **fundamentals of API creation**. The API features a **single endpoint** (`/api/message`), which, when accessed via an HTTP GET request, returns a structured JSON response. This response confirms that the API is running and accessible. 

### Why This Project?

The core objective of this project is to demonstrate my understanding of key principles in web development, specifically API design using Flask. This is a foundational step in building a comprehensive backend system for applications that require data exchange between clients and servers. I’ve intentionally kept the project simple to ensure that its structure is easy to understand, providing a clean slate for further enhancements as I continue to build on this knowledge.

## Author

**Martin Agoha**  
I am a passionate backend developer with a strong foundation in Python and Flask. This project reflects my dedication to improving my skills and becoming proficient in creating scalable, robust APIs. Through the HNG12 internship, I am gaining hands-on experience with Python and Flask, both of which are essential tools for modern backend development. I look forward to expanding my knowledge by contributing to larger projects and building more sophisticated systems.


## Setup Instructions

1. Clone the repository:
   ```sh
   git clone https://github.com/Martin4dbest/HNG12-Backend-stage0-api.git
   cd HNG12-Backend-stage0-api
   ```

2. Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```sh
   python app.py
   ```

   The server will start, and the API will be accessible at `http://127.0.0.1:5000`.



## API Documentation

### Endpoint URL

- **GET /api/message**

### Request Format

- **Method**: GET
- **URL**: `/api/message`

No parameters are required for this request.

### Response Format

The response will be returned in JSON format.

**Sample Response:**
```json
{
   "status": "success",
   "message": "Welcome to HNG12 Stage 0 API"
}
```

### Example Usage

You can test the API using cURL, Postman, or any HTTP client.

**Using cURL**:
```sh
curl http://127.0.0.1:5000/api/message
```

**Response**:
```json
{
   "status": "success",
   "message": "Welcome to HNG12 Stage 0 API"
}
```

## Additional Resources

For more details on how to become a developer in various programming languages, check out the following links:
- [Python Developers](https://hng.tech/hire/python-developers)
- [C# Developers](https://hng.tech/hire/csharp-developers)
- [GoLang Developers](https://hng.tech/hire/golang-developers)
- [PHP Developers](https://hng.tech/hire/php-developers)
- [Java Developers](https://hng.tech/hire/java-developers)
- [Node.js Developers](https://hng.tech/hire/nodejs-developers)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

