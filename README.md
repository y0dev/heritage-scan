# AI Image Processor 📸

A **Micro SaaS** application that allows users to **digitize photos** without visiting physical stores. This backend processes images, manages user authentication, and handles payments.

---

## 🚀 Features

- 📷 **Image Upload & Processing**
- 🔐 **User Authentication (JWT)**
- 💰 **Stripe Payment Integration**
- 📩 **Email Notifications (SendGrid)**
- 🗄️ **SQLAlchemy Database Support**

---

## 📂 Project Structure

```text
ai_image_processor/
│── components/
│ ├── auth/
│ ├── users/
│ │ ├── schema/
│ │ ├── controller/
│ │ ├── routes/
│ ├── photos/
│ │ ├── schema/
│ │ ├── controller/
│ │ ├── routes/
│ ├── payments/
│ ├── notifications/
│── middleware/
│── public/
│── utils/
│── storage/
│── config/
│── database/
│── tests/
│── app.py
│── config.py
│── requirements.txt
│── README.md
```

---

## 🔧 Setup & Installation

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/yourusername/ai-image-processor.git
cd ai-image-processor
```

### 2️⃣ **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4️⃣ **Set Up Environment Variables**

Create a `.env` file in the root directory:

```ini
DEBUG=True
DATABASE_URL=sqlite:///./database.db
SECRET_KEY=your_secret_key
STRIPE_SECRET_KEY=your_stripe_key
SENDGRID_API_KEY=your_sendgrid_key
```

### 5️⃣ **Run the Server**

```bash
uvicorn app:app --reload
```

---

## 🎯 API Endpoints

| Method | Endpoint         | Description      |
| ------ | ---------------- | ---------------- |
| `POST` | `/auth/login`    | User Login       |
| `POST` | `/auth/signup`   | Register User    |
| `GET`  | `/users/profile` | Get User Profile |
| `POST` | `/photos/upload` | Upload an Image  |
| `POST` | `/payments/pay`  | Process Payment  |

---

## 🛠 Tech Stack

- **FastAPI** (Backend Framework)
- **SQLAlchemy** (Database ORM)
- **JWT** (User Authentication)
- **Stripe API** (Payment Processing)
- **SendGrid** (Email Notifications)

---

## 🎯 Next Steps

✅ Build the **frontend**
✅ Deploy on **AWS/GCP**
✅ Add AI-based **image enhancement**

---

## 🤝 Contributing

Feel free to **fork** this repo and submit **pull requests**! 🚀

---

## 📜 License

This project is licensed under the **MIT License**.
