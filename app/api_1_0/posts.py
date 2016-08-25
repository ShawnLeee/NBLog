# encoding: utf-8
import os
from config import allowed_file
from config import DevelopmentConfig
from . import api
from flask import request
from Common import QBUser, QBPost, Comment
from flask import jsonify
from app import db


@api.route('/post', methods=['GET'])
def get_post():
    post_id = request.args.get('post_id')
    post = QBPost.query.get_or_404(post_id)
    return jsonify(post.to_json())


@api.route('/posts')
def get_posts():
    posts = QBPost.query.all()
    return jsonify({'posts': [post.to_json() for post in posts]})


@api.route('/comments')
def get_comments():
    post_id = request.args.get('post_id')
    comments = Comment.query.get_or_404()


@api.route('/posts/', methods=['POST','GET'])
def new_post():
    story = request.form.get('story')
    user_id = request.form.get('user_id')
    post = QBPost.post_with(story=story, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json())


@api.route('/upload',methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('not file')
        file = request.files['file']
        if file and allowed_file(file.filename):
            pwd = os.getcwd()
            img_path = os.path.join(pwd, 'app/static/img')
            filename = file.filename
            path = os.path.join(img_path,filename)
            file.save(path)
