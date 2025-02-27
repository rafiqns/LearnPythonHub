from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from models import Chapter, SubChapter, Content

content_bp = Blueprint('content', __name__)

@content_bp.route('/')
def index():
    chapters = Chapter.query.order_by(Chapter.order).all()
    return render_template('content/chapter_list.html', chapters=chapters)

@content_bp.route('/chapter/<int:chapter_id>')
@login_required
def chapter_detail(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    if chapter.is_pro and not current_user.is_pro:
        flash('This content is only available for Pro users', 'warning')
        return redirect(url_for('content.index'))

    # Determine if this is the last chapter
    last_chapter = Chapter.query.order_by(Chapter.order.desc()).first()
    is_last_chapter = chapter.id == last_chapter.id

    # Get the last subchapter of this chapter
    last_subchapter = SubChapter.query.filter_by(chapter_id=chapter.id)\
        .order_by(SubChapter.order.desc()).first()

    return render_template('content/chapter_detail.html', 
                         chapter=chapter,
                         is_last_chapter=is_last_chapter,
                         is_last_subchapter=lambda s: s.id == last_subchapter.id if last_subchapter else False)

@content_bp.route('/checkout')
@login_required
def checkout():
    return render_template('payment/checkout.html')

@content_bp.route('/process-payment', methods=['POST'])
@login_required
def process_payment():
    # Mock payment processing
    current_user.is_pro = True
    db.session.commit()
    flash('Welcome to Pro! You now have access to all content.', 'success')
    return redirect(url_for('content.index'))