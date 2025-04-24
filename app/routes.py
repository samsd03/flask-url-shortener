from flask import Blueprint, request, redirect, render_template, flash
from app.models import db, URL
import string, random

shortener = Blueprint('shortener', __name__)

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@shortener.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        code = generate_code()
        new_url = URL(original_url=original_url, short_code=code)
        db.session.add(new_url)
        db.session.commit()
        return render_template('index.html', short_url=code)
    return render_template('index.html')

@shortener.route('/<short_code>')
def redirect_short_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first_or_404()
    url.click_count += 1
    db.session.commit()
    return redirect(url.original_url)

@shortener.route('/stats/<short_code>')
def stats(short_code):
    url = URL.query.filter_by(short_code=short_code).first_or_404()
    print(url.click_count)
    return render_template('stats.html', url=url)
