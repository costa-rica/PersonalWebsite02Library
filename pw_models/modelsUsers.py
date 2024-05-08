# from .main import dict_base, dict_sess
from .Base import Base, DatabaseSession
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean, Table, JSON

from itsdangerous.url_safe import URLSafeTimedSerializer#new 2023
from datetime import datetime
from flask_login import UserMixin
from .config import config
import os
from flask import current_app

# Base_users = dict_base['Base_users']
# sess_users = dict_sess['sess_users']

def default_username(context):
    return context.get_current_parameters()['email'].split('@')[0]



class Users(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(Text, unique = True, nullable = False)
    password = Column(Text, nullable = False)
    permissions = Column(Text)
    posts = relationship('BlogPosts', backref='author', lazy=True)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def get_reset_token(self):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            payload = serializer.loads(token, max_age=1000)
            user_id = payload.get("user_id")
        except:
            return None

        # return sess.query(Users).get(user_id)
        db_session = DatabaseSession()
        try:
            user = db_session.query(Users).get(user_id)
        finally:
            db_session.close()  # Ensure the session is closed after use

    def __repr__(self):
        return f'Users(id: {self.id}, email: {self.email}, permissions: {self.permissions})'


class BlogPosts(Base):
    __tablename__ = 'blog_posts'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # post_id_name_string = Column(Text)# 20240508 delete
    # network_post_id = Column(Text)# 20240508 delete
    title = Column(Text)
    description = Column(Text)
    category = Column(Text)
    # edited = Column(Text)
    post_dir_name = Column(Text)
    post_html_filename = Column(Text)# New post file name
    # word_doc_to_html_filename = Column(Text)# <-- delete and move data to post_html_filename # 20240508 delete
    # images_dir_name = Column(Text)# 20240508 delete
    # blogpost_index_image_filename = Column(Text)
    image_filename_for_blogpost_home = Column(Text)# 20240508 replace blogpost_index_image_filename
    type_for_blogpost_home = Column(Text)
    has_images = Column(Boolean)
    has_code_snippets = Column(Boolean)
    notes = Column(JSON)
    tags = Column(JSON)
    icon_file = Column(Text)
    url = Column(Text)
    date_published = Column(DateTime, nullable=False, default=datetime.now)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)


    def __repr__(self):
        return f'BlogPosts(id: {self.id}, user_id: {self.user_id}, title: {self.title})'
