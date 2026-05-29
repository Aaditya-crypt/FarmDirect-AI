# 🌾 FarmDirect AI

## Smart Farm-to-Customer Marketplace with AI Price Prediction

FarmDirect AI is a full-stack web application that helps farmers sell their produce directly to customers while using Machine Learning to predict market prices of agricultural products.

The platform aims to reduce dependency on middlemen by enabling direct farmer-to-customer transactions with integrated order management and delivery tracking.

---

## 🚀 Features

### 🤖 AI Price Prediction
- Predicts crop prices using Machine Learning
- Uses historical agricultural market data
- Supports multiple crops and states
- Displays predicted price per quintal and per kilogram

### 👨‍🌾 Farmer Module
- Add crop listings
- Specify crop quantity
- Manage available produce

### 🛒 Customer Module
- Browse available crops
- View crop details
- Place orders directly from farmers

### 📦 Order Management
- Create orders
- View order history
- Track order status

### 🚚 Delivery System
- Assign delivery partners
- Update delivery status
- Track order progress

---

## 🏗️ System Architecture

Farmer
↓
Add Crop
↓
Backend Storage
↓
Customer Marketplace
↓
Place Order
↓
Delivery Assignment
↓
Order Tracking

AI Model
↓
Price Prediction
↓
Farmer Decision Support

---

## 🛠️ Technologies Used

### Frontend
- React
- TypeScript
- Vite
- Tailwind CSS
- Framer Motion

### Backend
- FastAPI
- Python
- Pandas
- Joblib

### Machine Learning
- Scikit-Learn
- Random Forest Regressor

### Data Storage
- JSON-based storage (Prototype)

### Development Tools
- VS Code
- Google Colab
- Git & GitHub

---

## 📊 Dataset

Agricultural market price dataset containing:

- Crop Name
- State
- Market
- Price Date
- Modal Price
- Minimum Price
- Maximum Price

Data was preprocessed and used to train a crop price prediction model.

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Label Encoding
5. Model Training
6. Model Evaluation
7. Model Deployment
8. API Integration

### Model Inputs
- Crop Type
- State
- Month

### Model Output
- Predicted Market Price

---

## 📂 Project Structure

```text
FarmDirect-AI
│
├── backend
│   ├── main.py
│   ├── price_model.pkl
│   ├── crop_encoder.pkl
│   ├── state_encoder.pkl
│   ├── crops.json
│   └── orders.json
│
├── frontend
│   ├── src
│   ├── components
│   ├── pages
│   └── assets
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### Backend

```bash
pip install fastapi uvicorn pandas scikit-learn joblib
```

Run Backend:

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

### Frontend

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## 📈 Future Enhancements

- User Authentication
- Farmer Dashboard
- Customer Dashboard
- Real Database Integration (PostgreSQL)
- Payment Gateway
- Live Location Tracking
- Delivery Partner Portal
- Price Trend Charts
- Demand Forecasting
- Mobile Application

---

## 🎯 Project Objective

To create an AI-powered agricultural marketplace that:

- Predicts crop prices
- Helps farmers make informed decisions
- Enables direct farmer-to-customer transactions
- Reduces dependency on intermediaries
- Improves transparency in agricultural trade

---

## 👨‍💻 Developer

**Aaditya Anil Pandey**

B.Sc. Computer Science

FarmDirect AI – Academic & Portfolio Project

---

## 📜 License

This project is developed for educational, research, and portfolio purposes.
