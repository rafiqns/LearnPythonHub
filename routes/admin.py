from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from functools import wraps
from app import db
from models import Chapter, SubChapter, Content, User
from forms import ChapterForm, SubChapterForm, ContentForm

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Access denied', 'danger')
            return redirect(url_for('content.index'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/')
@login_required
@admin_required
def dashboard():
    users = User.query.all()
    chapters = Chapter.query.all()
    return render_template('admin/dashboard.html', users=users, chapters=chapters)

@admin_bp.route('/content', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_content():
    chapter_form = ChapterForm()
    subchapter_form = SubChapterForm()
    content_form = ContentForm()

    chapters = Chapter.query.order_by(Chapter.order).all()
    subchapter_form.chapter_id.choices = [(c.id, c.title) for c in chapters]

    return render_template('admin/manage_content.html',
                          chapter_form=chapter_form,
                          subchapter_form=subchapter_form,
                          content_form=content_form,
                          chapters=chapters)

@admin_bp.route('/chapter/add', methods=['POST'])
@login_required
@admin_required
def add_chapter():
    form = ChapterForm()
    if form.validate_on_submit():
        chapter = Chapter(
            title=form.title.data,
            description=form.description.data,
            is_pro=form.is_pro.data,
            order=form.order.data
        )
        db.session.add(chapter)
        db.session.commit()
        flash('Chapter added successfully', 'success')
    return redirect(url_for('admin.manage_content'))