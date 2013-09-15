from flask import render_template, request
from app import app, db
from models import Article, Comment


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    latest_article_list = Article.query.order_by(Article.pub_date.desc()).all()
    
    return render_template("index.html", latest_article_list=latest_article_list)

@app.route('/articles')
@app.route('/articles.html')
def articles():
    latest_article_list = Article.query.order_by(Article.pub_date.desc()).all()
    num_articles = len(latest_article_list)
    latest_article_list = latest_article_list[:5]
    comments_list = Comment.query.order_by(Comment.id).all()
    
    return render_template('articles.html', latest_article_list=latest_article_list, comments_list=comments_list, num_articles=num_articles)

@app.route('/articles/<int:article_id>')
def article(article_id):
    article = Article.query.get_or_404(article_id)
    comments_list = Comment.query.order_by(Comment.id.desc()).filter_by(article_id=article_id).all()[:5]
    
    return render_template('article.html', article=article, comments_list=comments_list)

@app.route('/projects')
@app.route('/projects.html')
def projects():
    return render_template('projects.html')

@app.route('/faq')
@app.route('/faq.html')
def faq():
    return render_template('faq.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/newComment', methods=['POST'])
def newComment():
    articleID = request.form['article_id']
    author = request.form['author']
    contents = request.form['comment']
    comment = Comment(author, contents, articleID)
    db.session.add(comment)
    db.session.commit()
    return ""