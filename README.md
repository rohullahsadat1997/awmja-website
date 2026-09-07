# AWMJA — Afghanistan Women’s Movement for Justice and Awareness

A modern, bilingual, responsive website developed for the **Afghanistan Women’s Movement for Justice and Awareness (AWMJA)**.

The platform is designed to present the organization's mission, vision, goals, activities, achievements, leadership, news, events, articles, gallery, and contact information in both **Persian/Dari and English**.

The website includes a custom Django-powered administration system that allows authorized administrators to manage website content without modifying the source code.

---

## 🌐 Live Website

**Official Website:**  
https://awmja.org

**GitHub Repository:**  
https://github.com/rohullahsadat1997/awmja-website

---

## 📌 About the Project

AWMJA is a bilingual organizational website built to provide a professional digital presence for the Afghanistan Women’s Movement for Justice and Awareness.

The project combines a modern responsive frontend with a Django backend and a custom content management workflow through Django Admin.

The website supports both:

- 🇦🇫 فارسی / دری
- 🇺🇸 English

The interface automatically adapts between **RTL** and **LTR** layouts based on the selected language.

---

## ✨ Main Features

### 🌍 Bilingual Website

- Persian/Dari language support
- English language support
- RTL layout for Persian/Dari
- LTR layout for English
- Language switching
- Bilingual dynamic content

### 🏠 Homepage

- Hero section
- Organization introduction
- Impact statistics
- Featured activities
- Mission and vision highlights
- Achievements
- Leadership highlights
- Latest news/articles
- Calls to action
- Responsive navigation

### 📝 Content Management

Website content can be managed through Django Admin without editing HTML, CSS, Python, or JavaScript files.

Administrators can manage:

- Site settings
- Homepage content
- Activities
- Activity impacts
- Mission & Vision
- Goals
- Achievements
- Leadership
- News
- Articles
- Events
- Gallery
- Contact information
- Contact messages

---

## 📚 Website Sections

### About

Provides information about the organization, its background, activities, mission, vision, and goals.

### Mission & Vision

Presents the organization's mission, vision, values, and key principles.

### Goals

Displays the organization's strategic goals and priorities.

### Activities

Presents the organization's activities and initiatives.

### Achievements

Highlights organizational achievements and impact.

### Leadership

Displays leadership members with their names, positions, biographies, and profile images.

### News

Allows administrators to publish and manage organizational news.

### Articles

Provides a platform for publishing articles, analysis, opinions, and other written content.

### Events

Allows administrators to publish upcoming and past events, including dates, locations, descriptions, and images.

### Gallery

Provides image albums and media for organizational activities and events.

### Contact

Provides a contact form through which visitors can send messages to the organization.

Contact messages are stored in the Django administration panel for authorized administrators.

---

# 🛠️ Technology Stack

## Backend

- Python
- Django 6.1
- Django ORM
- Django Templates
- Django Internationalization (i18n)

## Frontend

- HTML5
- CSS3
- JavaScript
- Responsive Web Design
- RTL / LTR Support

## Fonts

- Vazirmatn
- Playfair Display

## Database

- SQLite for development/demo deployment
- PostgreSQL-ready architecture for future production infrastructure

## Static Files

- Django Static Files
- WhiteNoise
- `collectstatic`

## Deployment

- Railway
- GitHub
- Gunicorn
- Cloudflare

## Version Control

- Git
- GitHub

---

# 🏗️ Project Structure

```text
AWMJSA/
│
├── backend/
│   │
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── ...
│   │
│   ├── core/
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── context_processors.py
│   │   ├── migrations/
│   │   └── ...
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── activities.html
│   │   ├── leadership.html
│   │   ├── news.html
│   │   ├── events.html
│   │   ├── gallery.html
│   │   ├── contact.html
│   │   └── ...
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   └── fonts/
│   │
│   ├── media/
│   │
│   ├── locale/
│   │
│   ├── core_data.json
│   ├── manage.py
│   ├── requirements.txt
│   └── ...
│
├── .gitignore
└── README.md
