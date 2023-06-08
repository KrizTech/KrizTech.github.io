#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy
from engine.db_config import SQLALCHEMY_DATABASE_URI


db = SQLAlchemy()

class User(db.Model):
    """Creates a table for user info"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    password = db.Column(db.String(6533))
    account_type = db.Column(db.Enum('Tutor', 'Student'))
    courses = db.relationship('Course', backref='tutor', lazy=True)
    lessons = db.relationship('Lesson', backref='tutor', lazy=True)

class Course(db.Model):
    """Creates a table for courses"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    tutor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='course', lazy=True)
    forum = db.relationship('Discussion', backref='course', lazy=True)
    meetings = db.relationship('VideoMeeting', backref='course', lazy=True)

class Lesson(db.Model):
    """Creates a table for lessons"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    tutor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

class Comment(db.Model):
    """Creates a table for comments"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(500))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

class Discussion(db.Model):
    """Creates a table for the discussion forum"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

class VideoMeeting(db.Model):
    """Creates a table for video meetings"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
