# Flask Header Echo

This repository is a simple Flask web server that prints all incoming request headers to the console and returns them as a JSON response.

## 📜 Features
- Accepts all HTTP methods (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`)
- Prints request headers to the console
- Returns headers as JSON

## 🚀 Running Locally

### 1️⃣ Run with Python
```bash
pip install Flask
python app.py
```

### 2️⃣ Run with Docker
```bash
docker build -t flask-header-echo .
docker run -p 5000:5000 flask-header-echo
```

### 3️⃣ Run with Docker Compose
```bash
docker-compose up --build
```

Happy Testing!

### 🌟 Instructions to Use:
1. **Clone the Repository**:
   ```bash
   git clone <repo-url>
   cd flask-header-echo
   ```
2. **Run with Docker Compose:**:
   ```bash
   docker-compose up --build
   ```
3. **Test**:
   Use a browser, curl, or Postman:
   ```
   curl -X GET -H "X-Test-Header: Value" http://localhost:5000
   ```