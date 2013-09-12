from datetime import datetime
from app import db

# An article
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    contents = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    comments = db.relationship('Comment', backref = 'article', lazy = 'dynamic')
    
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.pub_date = datetime.now()
    
    # Make sure if we view it as an object we get the article title
    def __repr__(self):
        return self.title
    
    # Checks if the article was written in the last week: returns True if it was
    def was_written_recently(self):
        return self.pub_date >= datetime.now() - datetime.timedelta(days=7)
    
    

# A comment on an article
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    contents = db.Column(db.Text)
    author = db.Column(db.String(80))
    pub_date = db.Column(db.DateTime)
    
    # If viewed as an object, show author of comment
    def __repr__(self):
        return self.author
    
    def __init__(self, author, contents, article_id):
        self.author = author
        self.contents = contents
        self.article_id = article_id
        self.pub_date = datetime.now()