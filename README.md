# 📄 CV & Cover Letter Generator – Django Web App

A full-stack Django application that customizes resumes and generates cover letters using the OpenAI API. Users upload their resume and a job description, and the system tailors both documents accordingly.

---

## 🚀 Features

- ✅ Upload a resume (`.docx` or `.pdf`)
- ✅ Paste job description text
- ✅ AI-powered keyword extraction
- ✅ Resume customization with job-relevant keywords
- ✅ Cover letter generation with dynamic user info (name, email, etc.)
- ✅ Download output in `.docx` or `.pdf`
- ✅ Modern and clean frontend (HTML/CSS)
- ✅ Deployed to Render

---

## 🧩 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML + CSS (custom)
- **AI:** OpenAI GPT-3.5 Turbo (`openai` SDK)
- **Document Tools:** `python-docx`, `pdf2docx`
- **Deployment:** Render

---

## 📦 Project Structure

``` 
CV_CL_Integration/
├── resume_project/ # Django project folder
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── resume_app/ # Django app folder
│ ├── views.py
│ ├── urls.py
│ ├── forms.py
│ └── templates/
│ ├── base.html
│ ├── index.html
│ ├── cover_letter_form.html
│ └── cover_letter_pdf.html
├── static/
│ └── css/
│ └── style.css # Custom CSS styling
├── manage.py
├── requirements.txt
├── render.yaml
└── README.md ✅

```

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/CV_CL_Integration.git
cd CV_CL_Integration

```
### 2. Create a Virtual Environment

```
python -m venv venv
# Activate:
source venv/bin/activate         # On macOS/Linux
venv\Scripts\activate            # On Windows
```

### 3. Install Requirements
```
pip install -r requirements.txt
```
### 4. Create .env File

```
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX
SECRET_KEY = ...
```

### 5. Run Server
```
python manage.py runserver

```


