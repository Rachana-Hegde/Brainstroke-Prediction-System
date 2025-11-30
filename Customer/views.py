from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Appointment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import math
import random
import smtplib
from email.mime.text import MIMEText

# Create your views here.
def main(request):
    if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            date = request.POST.get("date")
            department = request.POST.get("department")
            doctor = request.POST.get("doctor")
            message = request.POST.get("message")

            if Appointment.objects.filter(name=name, email=email, date=date, doctor=doctor, department=department).exists():
                messages.warning(request, "You have already booked an appointment with this doctor on the same day")
                return redirect('/main#appointment')
            else:
                Appointment.objects.create(
                    name=name, email=email, phone=phone, date=date,
                    department=department, doctor=doctor, message=message
                )
                messages.success(request, "Appointment booked successfully")
            return redirect('/main#appointment')

    return render(request, "main.html")
    

def index(request):
    if request.method == "POST":
        un = request.POST['username']
        em = request.POST['email']
        pw = request.POST['pass1']
        pw1 = request.POST['pass2']
        
        if pw == pw1:
            if User.objects.filter(username=un).exists():
                messages.info(request, "Username already exists")
                return redirect('index')
            elif User.objects.filter(email=em).exists():
                messages.info(request, "Email already exists")
                return redirect('index')
            else:
                user = User.objects.create_user(username=un, email=em, password=pw1)
                user.save()
                
                user = authenticate(username=un, password=pw1)
                if user is not None:
                    login(request, user)
                    
                messages.success(request, "User created successfully")
                return redirect('otpVerify')
        else:
            messages.warning(request, "Passwords do not match")
            return redirect('index')
    return render(request, "index.html")


def user_login(request):
     if request.method == "POST":
        un = request.POST['username']
        em = request.POST['email']
        pw = request.POST['pass']
        user = auth.authenticate(username=un, email=em, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        if User.objects.filter(username=un, email=em, password=pw).exists:
            messages.info(request, "Invalid username or password")
            return render(request, "login.html")
     return render(request,"login.html")


def prediction(request):
    result = None
    show_result = False 
    if request.method == 'POST':
        show_result = True
        try:
            age = int(request.POST.get('age'))
            hypertension = int(request.POST.get('hypertension'))
            heart_disease = int(request.POST.get('heart_disease'))
            avg_glucose = float(request.POST.get('avg_glucose_level'))
            bmi = float(request.POST.get('bmi'))
            smoking_status = request.POST.get('smoking_status')

            if age > 60 or hypertension == 1 or heart_disease == 1 or bmi > 30 or smoking_status == "smokes":
                result = "High Risk of Stroke — Please consult a doctor immediately and take appropriate treatment"
            else:
                result = "Low Risk of Stroke — Keep maintaining a healthy lifestyle and regular checkups"

        except Exception as e:
            result = "Invalid input. Please check your details."

    return render(request, 'prediction.html', {'result': result, 'show_result': show_result})


def otpGen():
    return ''.join(random.choices('0123456789', k=4))

# Send OTP to user's email
def otpSend(request, otp):
    subject = "Your OTP Code"
    body = f"Your One-Time Password (OTP) is: {otp}"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "abhinayag.off@gmail.com"
    msg['To'] = request.user.email  # Only works if user is logged in

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("abhinayag.off@gmail.com", "bpot klka clpq bcyi")
            smtp.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)

# OTP verification view
def otpVerify(request):
    if not request.user.is_authenticated:
        return redirect('main')  # Ensure user is logged in

    if request.method == "POST":
        entered_otp = request.POST.get('otpVerify')
        session_otp = request.session.get('otp')

        if entered_otp == session_otp:
            del request.session['otp']  # Clean up
            return redirect('main')     # ✅ Correct OTP
        else:
            auth.logout(request)        # ❌ Wrong OTP, log out
            return redirect('main')     # Then redirect to main page anyway
    else:
        otp = otpGen()
        request.session['otp'] = otp
        otpSend(request, otp)
        return render(request, 'otpVerify.html')
