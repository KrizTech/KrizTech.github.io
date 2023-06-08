#!/usr/bin/pyhton3

from flask_sqlalchemy import SQLAlchemy
from engine.database import Course, Lesson, Comment, Discussion, VideoMeeting
from engine.database import db
from engine.database import User


"""
Fnctions for database operations on each table
"""

def update_user(user_id):
    """
    Update a user in the database.
    """
    user = User.query.get(user_id)
    if user:
        db.session.commit()

def delete_user(user_id):
    """
    user_id (int): The ID of the user to delete.
    """
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()

def add_user(user):
    """
    Add a new user to the database.
    """
    db.session.add(user)
    db.session.commit()


def update_video_meeting(video_meeting_id):
    """
    Update a video meeting in the database.
    """
    video_meeting = VideoMeeting.query.get(video_meeting_id)
    if video_meeting:
        db.session.commit()

def delete_video_meeting(video_meeting_id):
    """
    Delete a video meeting from the database.
    """
    video_meeting = VideoMeeting.query.get(video_meeting_id)
    if video_meeting:
        db.session.delete(video_meeting)
        db.session.commit()

def add_video_meeting(video_meeting):
    """
    Add a new video meeting to the database.
    """
    db.session.add(video_meeting)
    db.session.commit()
