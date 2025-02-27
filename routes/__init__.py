"""
This package contains the route blueprints for the Python Learning Platform.

Blueprints:
- auth_bp: Handles user authentication (login, register, logout)
- admin_bp: Admin dashboard and content management
- content_bp: Public content viewing and chapter navigation
"""

from .auth import auth_bp
from .admin import admin_bp
from .content import content_bp

__all__ = ['auth_bp', 'admin_bp', 'content_bp']
