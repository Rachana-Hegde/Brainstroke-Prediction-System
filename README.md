# 🧠 Brain Stroke Prediction – Machine Learning Web App

This project is a web-based application that predicts the likelihood of a **brain stroke** using user-provided medical data. Built with **Python**, **Django**, and **Machine Learning (CNN Model)**, the system offers a fast and interactive way to assess stroke risk.


## 🚀 Features

* 🧮 Predicts stroke risk based on medical and lifestyle input.
* 📊 Trained on real medical data using a **Convolutional Neural Network (CNN)**.
* 🌐 Built with **Django**, styled with **HTML**, **CSS**, **Bootstrap**, and includes **JavaScript** interactivity.
* 🛡️ User signup/login with **OTP-based email verification** for enhanced security.
* 📅 Appointment booking feature with form data stored in **SQLite** database.


## 📌 Technologies Used

* **Frontend:** HTML, CSS, Bootstrap, JavaScript
* **Backend:** Django (Python)
* **Machine Learning:** CNN (Convolutional Neural Network)
* **Database:** SQLite
* **Email Verification:** SMTP-based OTP system


## 🧠 How It Works

1. User enters health-related details (like age, BMI, glucose level, etc.).
2. The CNN model processes the inputs and returns a prediction:

   * 🔴 High risk of stroke
   * 🟢 Low risk of stroke
3. The result is displayed immediately on the web page.
4. Users can also book an appointment with a doctor via the appointment form.


## 📥 Installation

```bash
git clone https://github.com/your-username/brainstroke-prediction.git
cd brainstroke-prediction
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Access the app at: `http://127.0.0.1:8000/`


## 🧪 Input Features Used for Prediction

* Age
* Gender (encoded)
* Hypertension
* Heart Disease
* Work Type (encoded)
* Avg Glucose Level
* BMI
* Smoking Status (encoded)

> 📝 Only these 8 key features are used for model training and prediction.


## 📊 Model Training

* Trained on a **cleaned Kaggle stroke prediction dataset**.
* Used a **Convolutional Neural Network (CNN)** architecture.
* Model is saved and loaded using `joblib` or `pickle` for real-time predictions.


## 📂 Project Structure

```
brainstroke-prediction/
│
├── stroke_model/              # ML model + preprocessing
├── templates/                 # HTML pages
├── static/                    # CSS, JS, images
├── appointments/              # Appointment form logic
├── authentication/            # User login/signup + OTP
├── manage.py
└── db.sqlite3
```


## ✅ How to Use

1. Register or login using email verification.
2. Fill in the prediction form with health details.
3. Get instant prediction results.
4. Optionally, book an appointment for further medical assistance.


## 🔐 Security Note

* Email OTP verification ensures secure user registration.
* Prediction data is **not stored** in the database to preserve user privacy.


## 📬 Contact  

For any inquiries or feedback, feel free to reach out:    
🔗 **GitHub**: [Rachana-Hegde](https://github.com/Rachana-Hegde)  
