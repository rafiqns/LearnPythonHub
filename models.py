from app import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_pro = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Chapter(db.Model):
    __tablename__ = 'chapters'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    order = db.Column(db.Integer)
    is_pro = db.Column(db.Boolean, default=False)
    subchapters = db.relationship('SubChapter', backref='chapter', lazy=True)

class SubChapter(db.Model):
    __tablename__ = 'subchapters'
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    order = db.Column(db.Integer)
    contents = db.relationship('Content', backref='subchapter', lazy=True)

class Content(db.Model):
    __tablename__ = 'contents'
    id = db.Column(db.Integer, primary_key=True)
    subchapter_id = db.Column(db.Integer, db.ForeignKey('subchapters.id'), nullable=False)
    content_type = db.Column(db.String(20), nullable=False)  # text, video, link
    content = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer)