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

## 🚀 Deployment Guide (AWS EC2)

This app is deployed on an AWS EC2 instance using the free tier. Here's how to do it:

### 1. Launch EC2 Instance
- Use Ubuntu or Amazon Linux 2 (free tier eligible)
- Allow ports 22 (SSH), 80 (HTTP) in the security group

### 2. Connect via SSH
```bash
ssh -i "your-key.pem" ec2-user@your-public-ip

### 3. Install Required Packages
- sudo yum update -y        
- sudo yum install git python3-pip nginx

### 4. Clone Your Repo
- git clone https://github.com/yourusername/flask-url-shortener.git

- cd flask-url-shortener

### 5. Set Up Virtual Environment
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

### 6. Run with Gunicorn
- gunicorn -w 3 -b 127.0.0.1:8000 run:app

### 7. Configure systemd Service
- Create /etc/systemd/system/flaskapp.service:

[Unit]
Description=Gunicorn instance to serve Flask app
After=network.target

[Service]
User=ec2-user
Group=nginx
WorkingDirectory=/home/ec2-user/flask-url-shortener
Environment="PATH=/home/ec2-user/flask-url-shortener/venv/bin"
ExecStart=/home/ec2-user/flask-url-shortener/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 run:app

[Install]
WantedBy=multi-user.target

Enable and start the service:

sudo systemctl daemon-reexec
sudo systemctl start flaskapp
sudo systemctl enable flaskapp


 






