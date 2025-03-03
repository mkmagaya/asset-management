# Asset Management System (Django, Streamlit, PostgreSQL)

This Asset Management System is built using Django for backend processing, Streamlit for the web interface, and PostgreSQL for persistent data storage. It allows users to manage assets such as laptops, desktops, and other hardware efficiently.

## Project Stack

- **Django**: Handles the backend, database models, API, and business logic.
- **Streamlit**: Provides an interactive web-based interface for asset management.
- **PostgreSQL**: Stores asset records securely.
- **Pipenv**: Manages the project environment and dependencies.

---

## Prerequisites

- Python 3.11+
- Pipenv (install with `pip install pipenv`)
- PostgreSQL 14+
- Git (for version control)

---

## Installation

### 1. Clone the Repository

```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Setup Virtual Environment using Pipenv

```bash
pipenv install
```

To activate the virtual environment:

```bash
pipenv shell
```

This will install dependencies from `Pipfile.lock` or create a fresh environment based on `Pipfile`.

---

## Configuration

### 1. Database Configuration (PostgreSQL)

Ensure PostgreSQL is installed and running. Create a new database:

```sql
CREATE DATABASE asset_db;
```

Then, configure Django to use PostgreSQL by updating `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'asset_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## Running the Application

### 1. Apply Migrations

Run the following command to apply database migrations:

```bash
python manage.py migrate
```

### 2. Start Django Server

```bash
python manage.py runserver
```

Access the Django admin panel at:  
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

### 3. Start Streamlit App

```bash
streamlit run app.py
```

The Streamlit UI will be available at:  
[http://127.0.0.1:8501](http://127.0.0.1:8501)

---

## Adding an Asset

When adding an asset via the Streamlit interface, the following fields are required:

- **Name** (Laptop/Desktop model)
- **Assigned User** (Who is using the asset)
- **User Company** (Company associated with the asset)
- **Device Type** (Laptop/Desktop)
- **Asset Code** (Unique identifier, if available)
- **Product Number**
- **Serial Number**
- **Domain ID** (Auto-generated based on company and device details)
- **Additional Information**
- **Keyboard, Monitor, Mouse** (For desktops only)

### Auto-generated Domain ID Format:

```
<Company Abbreviation>-<Device Type>-<Department>-<Last 4 Characters of Serial Number>
```

Example:  
- **TXX-L-ICT-9F6G**: TXX (Company), L (Laptop), ICT (Department), 9F6G (Last 4 characters of serial number).

---

## Troubleshooting

- **Pipenv not found?** Install it using:
  ```bash
  pip install pipenv
  ```

- **Database connection issues?** Ensure PostgreSQL is running and your `settings.py` configuration is correct.

- **Migrations not applied?** Run:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

---

## Contribution & Future Improvements

- User roles & permissions
- Asset lifecycle tracking
- API for external integrations
- Advanced reporting & analytics

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
