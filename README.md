  # 📝 Blogging Platform (Full Stack)
- 🔗 **Frontend (Streamlit)**: [View App](https://blogapi-6pk9ubjphuc84adefappclh.streamlit.app/)
A simple full-stack blogging platform built with:

- 🌐 **Spring Boot** (Java) — RESTful backend
- 🗃️ **MySQL** — Persistent database for blog posts by railway 
- 🎨 **Streamlit** — Interactive frontend
- 🚀 **Render** — Backend deployment
- 📦 **Streamlit Cloud** — Frontend deployment

---

## 🔧 Features

- 📄 View all blog posts
- ➕ Create new posts
- ✏️ Edit existing posts
- 🗑️ Delete posts
- 💾 Fully connected to MySQL via railway 
- ☁️ Deployed & live

---

## 📁 Project Structure
blogapi/
├── blogstreamlit/ # Streamlit frontend
│ └── app.py # Main frontend logic
├── src/ # Spring Boot backend source
│ └── main/java/
│ └── main/resources/
├── pom.xml # Maven config
├── Dockerfile # For backend deployment
└── README.md # You are here
## 🛠️ How to Run Locally

### ✅ Backend (Spring Boot)

```bash
cd blogapi
mvn spring-boot:run
