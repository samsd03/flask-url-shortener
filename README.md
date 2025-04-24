# 🔗 Flask URL Shortener

A simple, full-stack **URL Shortener** web application built using **Flask** and deployed on **AWS EC2 Free Tier** with production-ready setup using **Gunicorn** and **NGINX**.

## 🌟 Features

- Shorten long URLs to short aliases
- Track number of visits and creation time
- View individual URL stats
- Simple and modern UI
- Deployed and live on AWS EC2

---

## 🛠️ Tech Stack

- **Backend:** Flask, SQLAlchemy
- **Database:** SQLite (easy local setup)
- **Web Server:** Gunicorn (WSGI)
- **Reverse Proxy:** NGINX
- **Hosting:** AWS EC2 Free Tier
- **Deployment:** SSH, SCP, systemd, Git
- **OS:** Amazon Linux 2 (EC2 Instance)

---



---

## ⚙️ Local Development

```bash
# Clone the repository
git clone https://github.com/<your-username>/flask-url-shortener.git
cd flask-url-shortener

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py

Visit: http://127.0.0.1:5000


---

## 🔍 Explanation of Key Files

### `app.py`
- Initializes the Flask app
- Configures the SQLite database using SQLAlchemy
- Contains all routes: homepage (`/`), stats (`/stats/<short_code>`), and redirection (`/<short_code>`)

### `models.py`
- Defines the `URL` class (with `id`, `original_url`, `short_url`, `visits`, and `created_at`)

### `run.py`
- Contains `app` instance
- Used by Gunicorn (`gunicorn -w 3 -b 127.0.0.1:8000 run:app`)

### `templates/`
- HTML files using Jinja2 templating engine
- `index.html`: Landing page with form to shorten a URL
- `stats.html`: Displays analytics for a shortened URL

### `static/style.css`
- Custom CSS for styling the app

---

## ⚙️ Deployment & Services

### `flaskapp.service`
- A **systemd** unit file to keep the Flask app running as a background service via Gunicorn
- Located at: `/etc/systemd/system/flaskapp.service`

---

## 💡 Tips

- Keep sensitive settings (like secrets or production configs) in environment variables.
- You can extend this by adding user accounts, Redis caching, or a PostgreSQL database.
- For scalability, replace SQLite with PostgreSQL and add NGINX + Certbot for HTTPS.

---



