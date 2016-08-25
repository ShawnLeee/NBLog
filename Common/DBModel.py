# -*- coding:utf-8 -*-
from app import db
from QBSpider import Comment


class CommentDB(db.Model):
    comment_id = None
    post_id = None
    user_id = None
    comment_text = None
    floor = None

    def __init__(self, comment):
        """
        :type comment:Comment
        :param comment:
        :return:
        """
        self.comment_id = comment.comment_id
        self.post_id = comment.post_id
        self.user_id = comment.user_id