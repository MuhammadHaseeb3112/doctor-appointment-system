# 🩺 Doctor Appointment System

A full-stack **Doctor Appointment System** built with **Django** that enables patients to book appointments online, doctors to manage their schedules, and administrators to oversee doctors, appointments, specializations, and website content. The system includes secure authentication with role-based access control for administrators and doctors.

---

# 📌 Features

## 👨‍⚕️ Patient Features

* Browse Available Doctors
* Search Doctors by Name or Specialization
* Book Doctor Appointments
* Appointment Number Generation
* Search Appointments
* View Appointment Details
* Responsive User Interface

---

## 👨‍⚕️ Doctor Features

* Doctor Registration
* Doctor Login
* Doctor Dashboard
* View All Appointments
* View New Appointments
* View Approved Appointments
* View Completed Appointments
* View Cancelled Appointments
* Update Appointment Status
* Add Medical Remarks
* Write Prescriptions
* Recommend Medical Tests
* Search Patient Appointments
* Generate Appointment Reports
* Update Doctor Profile
* Change Password

---

## 👨‍💼 Administrator Features

* Secure Admin Dashboard
* Manage Doctor Specializations
* Add New Specializations
* Update Specializations
* Delete Specializations
* Manage Doctors
* View Doctor Details
* View Patient Details
* Search Doctors
* Appointment Reports
* Website Information Management
* Dashboard Statistics

---

# 🚀 Technology Stack

## Backend

* Python 3
* Django 5.x

## Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

## Database

* SQLite3

## Authentication

* Custom Django User Model
* Email-Based Authentication
* Role-Based Access Control

## Other Technologies

* Django ORM
* WhiteNoise
* Environment Variables (.env)
* Pagination
* Django Messages Framework

---

# Project Structure

```text
doctor-appointment-system/
│
├── docapp/
│   ├── api/
│   ├── templates/
│   ├── static/
│   ├── media/
│   ├── adminviews.py
│   ├── docviews.py
│   ├── userviews.py
│   ├── views.py
│   ├── urls.py
│   └── settings.py
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# Database Models

## CustomUser

* Custom Authentication
* User Roles
* Profile Picture
* Email Login

---

## Doctor

* Doctor Name
* Specialization
* Consultation Details
* Experience
* Location
* Rating
* Profile Image

---

## Doctor Registration

* Doctor Profile
* Mobile Number
* Specialization
* Registration Date

---

## Appointment

Stores appointment information including:

* Appointment Number
* Patient Name
* Email
* Mobile Number
* Appointment Date
* Appointment Time
* Assigned Doctor
* Additional Message
* Doctor Remarks
* Prescription
* Recommended Tests
* Appointment Status

---

## Specialization

Stores medical specializations such as:

* Cardiologist
* Dentist
* Neurologist
* Dermatologist
* Orthopedic
* Pediatrician

---

## Website Page

Stores editable website information:

* Website Title
* About Us
* Address
* Contact Email
* Phone Number

---

# Appointment Workflow

1. Patient selects a doctor.
2. Patient chooses a future appointment date.
3. System generates a unique appointment number.
4. Appointment is stored with **Pending** status.
5. Doctor reviews appointment.
6. Doctor approves or cancels the appointment.
7. Doctor adds remarks and prescription after consultation.
8. Patient can search and view appointment details.

---

# User Roles

## Administrator

* Full System Access
* Manage Doctors
* Manage Specializations
* Website Configuration
* Reports

---

## Doctor

* Manage Own Appointments
* View Patients
* Update Appointment Status
* Add Prescriptions
* Generate Reports

---

## Patient

* Book Appointment
* Search Appointment
* View Appointment Status

---

# Installation

Clone the repository

```bash
git clone https://github.com/MuhammadHaseeb3112/doctor-appointment-system.git
```

Navigate to the project

```bash
cd doctor-appointment-system
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Run migrations

```bash
python manage.py migrate
```

Create a superuser

```bash
python manage.py createsuperuser
```

Run the server

```bash
python manage.py runserver
```

Open your browser

```text
http://127.0.0.1:8000/
```

---

# Screenshots

Add screenshots for:

* Home Page
* Doctor Listing
* Doctor Registration
* Patient Appointment
* Login Page
* Doctor Dashboard
* Admin Dashboard
* Appointment Details
* Reports

---

# Future Improvements

* REST API with Django REST Framework
* Email Appointment Notifications
* SMS Notifications
* Online Payment Integration
* Video Consultation
* Doctor Availability Calendar
* Patient Medical History
* PDF Prescription Download
* Appointment Reminder System
* Docker Support
* PostgreSQL Database
* Deployment on Render or Railway

---

# Security Features

* Environment Variables
* Custom Authentication Backend
* Password Hashing
* Role-Based Authorization
* Login Required Decorators
* WhiteNoise Static File Management

---

# License

This project is developed for educational and portfolio purposes.

---

# Author

**Muhammad Haseeb**

Software Developer

📧 Email: [mhasseb3112@example.com](mailto:mhasseb3112@example.com)

💼 GitHub: https://github.com/MuhammadHaseeb3112

🌐 LinkedIn: https://www.linkedin.com/in/your-linkedin
