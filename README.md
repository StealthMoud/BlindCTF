# **BlindCTF**

Welcome to **BlindCTF**, a Capture The Flag challenge designed to simulate a vulnerable web application for testing purposes. This project is built to help you practice web application security concepts in a controlled environment.

---

## **Getting Started**

### **Prerequisites**
To set up this project, ensure you have the following installed on your system:
- [Docker](https://www.docker.com/)  
- [Docker Compose](https://docs.docker.com/compose/)

---

### **Setup Instructions**

1. **Clone the repository**  
   Start by cloning this repository to your local system:
   ```bash
   git clone https://github.com/StealthMoud/BlindCTF
   cd BlindCTF
   ```

2. **Start the application**  
   Use Docker Compose to build and run the application:
   ```bash
   docker-compose up --build
   ```

3. **Access the application**  
   Once the containers are running, open your browser and visit:
   ```
   http://127.0.0.1:5001
   ```

4. **Shut down the application**  
   When you’re done, stop the containers with:
   ```bash
   docker-compose down
   ```

---

## **Project Overview**

### **Tech Stack**
- **Backend**: Flask (Python)  
- **Database**: MySQL  
- **Frontend**: HTML, CSS, and JavaScript  

### **Features**
- A modern user interface for interacting with the challenge.
- Containerized setup for seamless deployment.
- Includes a preconfigured MySQL database.

### **Directory Structure**
```
BlindCTF/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── routes.py            # Application routes
│   ├── templates/           # HTML templates
│   │   ├── index.html       # Homepage
│   │   ├── items.html       # Items page
│   ├── static/              # Static files (CSS, JS)
│       ├── styles.css       # Custom styles
│       ├── scripts.js       # JavaScript logic for dynamic behavior
├── db_init.sql              # SQL script to initialize the database
├── Dockerfile               # Docker configuration for the web application
├── docker-compose.yml       # Docker Compose setup
├── requirements.txt         # Python dependencies
```

---

## **Notes**

This project is intentionally designed for learning and should only be used in a safe, isolated environment. Avoid deploying it in production environments or exposing it to untrusted users.

---

## **Questions or Issues?**

If you encounter any issues, have questions, or want to contribute, feel free to:

1. **Open an Issue on GitHub**  
   Visit the [issues page](https://github.com/StealthMoud/BlindCTF/issues) for this repository and create a new issue.

2. **Contact Me Directly**  
   Email me at: [stealthmoud@gmail.com](mailto:stealthmoud@gmail.com)

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for exploring BlindCTF! 😊