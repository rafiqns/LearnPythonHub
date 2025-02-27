from flask import Blueprint, jsonify, redirect, url_for, render_template
from flask_login import current_user, login_required
from app import db
from models import UserProgress, SubChapter, Chapter
from datetime import datetime
import logging

progress_bp = Blueprint('progress', __name__)

@progress_bp.route('/progress/<int:subchapter_id>/complete', methods=['POST'])
@login_required
def complete_subchapter(subchapter_id):
    try:
        subchapter = SubChapter.query.get_or_404(subchapter_id)
        progress = UserProgress.query.filter_by(
            user_id=current_user.id,
            subchapter_id=subchapter_id
        ).first()

        if not progress:
            progress = UserProgress(
                user_id=current_user.id,
                subchapter_id=subchapter_id
            )
            db.session.add(progress)

        progress.completed = True
        progress.completed_at = datetime.utcnow()
        db.session.commit()
        logging.info(f"User {current_user.username} completed subchapter {subchapter_id}")

        # Check if this was the last subchapter in the chapter
        last_subchapter = SubChapter.query.filter_by(chapter_id=subchapter.chapter_id)\
            .order_by(SubChapter.order.desc()).first()

        if last_subchapter and subchapter.id == last_subchapter.id:
            # Check if this is the last chapter
            last_chapter = Chapter.query.order_by(Chapter.order.desc()).first()
            if last_chapter and subchapter.chapter_id == last_chapter.id:
                progress.certificate_generated = True
                db.session.commit()
                return jsonify({'redirect': url_for('progress.show_certificate', 
                                                chapter_id=last_chapter.id)})

        return jsonify({'status': 'success'})
    except Exception as e:
        logging.error(f"Error completing subchapter: {str(e)}")
        return jsonify({'error': 'Terjadi kesalahan'}), 500

@progress_bp.route('/certificate/<int:chapter_id>')
@login_required
def show_certificate(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    return render_template('progress/certificate.html', chapter=chapter)

@progress_bp.route('/progress/status/<int:chapter_id>')
@login_required
def get_progress(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    total_subchapters = SubChapter.query.filter_by(chapter_id=chapter_id).count()
    completed_subchapters = UserProgress.query.join(SubChapter).filter(
        UserProgress.user_id == current_user.id,
        SubChapter.chapter_id == chapter_id,
        UserProgress.completed == True
    ).count()

    progress_percentage = (completed_subchapters / total_subchapters * 100) if total_subchapters > 0 else 0

    return jsonify({
        'total': total_subchapters,
        'completed': completed_subchapters,
        'percentage': round(progress_percentage, 1)
    })