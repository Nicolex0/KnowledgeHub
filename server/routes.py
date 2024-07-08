from flask_restful import Resource, Api
from models import db, User, Article, Comment, Follow
from flask import request, jsonify

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user.to_dict()

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.profile_info = data.get('profile_info', user.profile_info)
        db.session.commit()
        return user.to_dict()

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

class ArticleResource(Resource):
    def get(self, article_id):
        article = Article.query.get_or_404(article_id)
        return article.to_dict()

    def put(self, article_id):
        article = Article.query.get_or_404(article_id)
        data = request.get_json()
        article.title = data.get('title', article.title)
        article.content = data.get('content', article.content)
        db.session.commit()
        return article.to_dict()

    def delete(self, article_id):
        article = Article.query.get_or_404(article_id)
        db.session.delete(article)
        db.session.commit()
        return '', 204

class CommentResource(Resource):
    def get(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        return comment.to_dict()

    def put(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        data = request.get_json()
        comment.content = data.get('content', comment.content)
        db.session.commit()
        return comment.to_dict()

    def delete(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        db.session.delete(comment)
        db.session.commit()
        return '', 204

class ArticleListResource(Resource):
    def get(self):
        articles = Article.query.all()
        return [article.to_dict() for article in articles]

    def post(self):
        data = request.get_json()
        new_article = Article(
            title=data['title'],
            content=data['content'],
            user_id=data['user_id']
        )
        db.session.add(new_article)
        db.session.commit()
        return new_article.to_dict(), 201

class CommentListResource(Resource):
    def get(self):
        comments = Comment.query.all()
        return [comment.to_dict() for comment in comments]

    def post(self):
        data = request.get_json()
        new_comment = Comment(
            content=data['content'],
            user_id=data['user_id'],
            article_id=data['article_id']
        )
        db.session.add(new_comment)
        db.session.commit()
        return new_comment.to_dict(), 201

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users]

    def post(self):
        data = request.get_json()
        new_user = User(
            username=data['username'],
            email=data['email']
        )
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201

def initialize_routes(api):
    api.add_resource(UserResource, '/users/<int:user_id>')
    api.add_resource(UserListResource, '/users')
    api.add_resource(ArticleResource, '/articles/<int:article_id>')
    api.add_resource(ArticleListResource, '/articles')
    api.add_resource(CommentResource, '/comments/<int:comment_id>')
    api.add_resource(CommentListResource, '/comments')

