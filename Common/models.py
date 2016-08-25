# -*- coding:utf-8 -*-
import time
from app import db
from uuid import uuid4


class QBUser(db.Model):
    __tablename__ = 'users_t'
    user_id = db.Column(db.String(255), primary_key=True)
    user_name = db.Column(db.String(255))
    avatar = db.Column(db.String(255))
    # article_count = db.Column(db.Integer)
    author_url = db.Column(db.String(255))


class QBPost(db.Model):
    __tablename__ = 'posts_t'
    post_id = db.Column(db.String(255), primary_key=True)
    user_id = db.Column(db.String(255), db.ForeignKey('users_t.user_id'))
    post_text = db.Column(db.Text)
    like_count = db.Column(db.Integer)
    comment_count = db.Column(db.Integer)
    created_time = db.Column(db.String(255))

    def __init__(self, post_id=None, user_id=None, post_text=None, like_count=None, comment_count=None, create_time=None):
        self.post_id = post_id
        self.user_id = user_id
        self.post_text = post_text
        self.like_count = like_count
        self.comment_count = comment_count
        self.created_time = create_time

    @classmethod
    def post_with_article_soup(cls, article):
        a_soup = article.find('li', class_='user-article-text').find('a')
        article_text = a_soup.text.replace('\n', '')
        article_id = a_soup['href'].split("/")[2]
        article_stats = article.find('li', class_='user-article-stat')
        article_create_time = article_stats.find('a').text.replace('\n', '')
        article_stats_text = article_stats.text.split('\n')
        stats = []
        for com in article_stats_text:
            for s in com.split():
                if s.isdigit():
                    stats.append(int(s))
        post = cls()
        post.post_text = article_text
        post.post_id = article_id
        post.like_count = stats[0]
        post.comment_count = stats[1]
        post.created_time = article_create_time
        return post

    def to_json(self):
        json_post = dict(post_id=self.post_id, user_id=self.user_id, like_count=self.like_count,
                         comment_count=self.comment_count, post_text=self.post_text, created_time=self.created_time)
        return json_post

    @staticmethod
    def post_with(story, user_id):
        post = QBPost()
        post.user_id = user_id
        post.post_text = story
        post.post_id = uuid4().hex
        post.created_time = time.ctime()
        return post

    @staticmethod
    def from_json(json_post):
        # body = json_post.get('body')
        # if body is None or body == '':
        #     raise ValueError
        return QBPost(body=json_post)



class Comment(db.Model):
    __tablename__ = 'comments_t'
    comment_id = db.Column(db.String(255), primary_key=True)
    user_id = db.Column(db.String(255))
    post_id = db.Column(db.String(255), db.ForeignKey('posts_t.post_id'))
    comment_text = db.Column(db.Text)
    floor = db.Column(db.String(255))

    def __init__(self, comment_id=None, user_id=None, post_id=None, comment_text=None, floor=None):
        self.comment_id = comment_id
        self.user_id = user_id
        self.post_id = post_id
        self.comment_text = comment_text
        self.floor = floor
