# Campus Lost & Found System

A Django-based web application that helps students report, search, and manage lost and found items on campus.

## Features

* **User Authentication:** User registration, login, and logout.
* **Report Lost Items:** Submit details of lost items.
* **Report Found Items:** Report items found on campus.
* **Search Items:** Search by item name or category.
* **Status Tracking:** Update item status to Found or Returned.
* **Manage Reports:** Edit and delete your own reports.
* **Item Details:** View item descriptions, locations, dates, and contact details.
* **My Reports:** View all items reported by the logged-in user.
* **Admin Panel:** Manage item records through Django Admin.
* **Responsive UI:** Simple and user-friendly interface.

## Technologies Used

* Python
* Django
* HTML5
* CSS3
* SQLite
* Django Authentication System

## Project Structure

```text
Qus4_Campus_Lost_Found_System/
├── items/
│   ├── migrations/
│   ├── templates/
│   │   └── items/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── lostfound/
│   ├── settings.py
│   └── urls.py
├── static/
│   └── css/
│       └── style.css
├── manage.py
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Campus-Lost-and-Found-System.git
```

### 2. Navigate to the Project Folder

```bash
cd Campus-Lost-and-Found-System
```

### 3. Install Django

```bash
python -m pip install django
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an Admin Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open the following URL in your browser:

```text
http://127.0.0.1:8000/
```

## Application Pages

| Page        | URL             |
| ----------- | --------------- |
| Home        | `/`             |
| Register    | `/register/`    |
| Login       | `/login/`       |
| Lost Items  | `/lost-items/`  |
| Found Items | `/found-items/` |
| My Reports  | `/my-reports/`  |
| Admin Panel | `/admin/`       |

## How to Use

1. Register a new account or log in.
2. Report a lost or found item using the appropriate form.
3. Browse the Lost Items and Found Items pages.
4. Search for items by name or category.
5. Open an item to view its details.
6. Edit, delete, or update the status of your own reports.
7. Access the Django Admin Panel to manage records.

## Database

The application uses SQLite as its default database. Item records are associated with the user who reported them.

## Purpose

This project demonstrates Django web development concepts, including authentication, models, forms, CRUD operations, database management, search functionality, and template rendering.

## Author

**Poonam Bhavsar**

GitHub: [BhavsarPoonam1409](https://github.com/BhavsarPoonam1409)
