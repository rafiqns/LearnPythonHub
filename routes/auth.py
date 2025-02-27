from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
import logging
from models import User
from forms import LoginForm, RegisterForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            logging.info(f"User {user.username} logged in successfully")
            next_page = request.args.get('next')
            return redirect(next_page or url_for('content.index'))
        flash('Username atau password salah', 'danger')
        logging.warning(f"Failed login attempt for username: {form.username.data}")
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if username already exists
        if User.query.filter_by(username=form.username.data).first():
            flash('Username sudah digunakan', 'danger')
            logging.warning(f"Registration attempt with existing username: {form.username.data}")
            return render_template('auth/register.html', form=form)

        # Check if email already exists
        if User.query.filter_by(email=form.email.data).first():
            flash('Email sudah terdaftar', 'danger')
            logging.warning(f"Registration attempt with existing email: {form.email.data}")
            return render_template('auth/register.html', form=form)

        try:
            user = User(
                username=form.username.data,
                email=form.email.data,
                password_hash=generate_password_hash(form.password.data)
            )
            db.session.add(user)
            db.session.commit()
            logging.info(f"New user registered successfully: {user.username}")
            flash('Registrasi berhasil! Silakan login.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error during user registration: {str(e)}")
            flash('Terjadi kesalahan saat registrasi. Silakan coba lagi.', 'danger')
            return render_template('auth/register.html', form=form)

    return render_template('auth/register.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logging.info(f"User {current_user.username} logged out")
    logout_user()
    return redirect(url_for('content.index'))