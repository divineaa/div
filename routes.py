from pydoc import describe
import sentiment
import datetime
import forms 
from models import User, Article, Comment
from app import app, db
from flask import Flask, make_response, render_template, redirect, url_for,request,flash, get_flashed_messages, session
from flask_login import UserMixin
from flask_login import LoginManager,login_user, current_user
from sqlalchemy import desc
login_manager = LoginManager()
login_manager.init_app(app)
# for getting the current date:
dnow = datetime.datetime.now()
# for upload
from werkzeug.utils import secure_filename
import uuid as uuid
import os

#INDEX/HOME/Article Posts
@app.route('/')
@app.route('/index/', methods=['GET','POST'])
def index():
    if session.get("user_id") == None:
        session["user_id"] = 1
    user_id =session.get("user_id")
    # session.pop("user_id", None) #upon logout
    articles = Article.query.order_by(desc(Article.date)).all()
    return render_template('index.html', articles = articles, user_id=user_id)

#for posting an article
@app.route('/postarticle', methods=['GET','POST'])
def postarticle():
    user_id =session.get("user_id")
    form = forms.AddArticleForm()
    
    if form.validate_on_submit():
        picture = request.files["article_pic"]
        # Grab Image Name
        article_picName = secure_filename(picture.filename)
        # Make filename unique by setting UUID
        article_picName2 = str(uuid.uuid1())+ "_" + article_picName  
        # Save the image
        picture.save(os.path.join(app.config['UPLOAD_FOLDER'],article_picName2))

        r = Article(title=form.title.data, description = form.description.data, location = form.location.data, user_id=8, date=dnow, article_pic = article_picName2)
        db.session.add(r)
        db.session.commit()
        flash('Successfully Added')
        return redirect(url_for('index'))
    return render_template('postarticle.html', form=form, user_id=user_id)

#for viewing an article and commenting
@app.route('/viewarticle/<int:article_id>/', methods=['GET','POST'])
def viewarticle(article_id):
    if session.get("user_id") == None:
        session["user_id"] = 1
    
    user_id =session.get("user_id")
    form = forms.AddCommentForm()
    id = session["user_id"]
    # for displaying the contents of the article:
    article = Article.query.get(article_id)
    art_loc = article.location
    # for displaying the comments about the article:
    comments = db.session.query(User, Comment).join(Comment).filter(Comment.article_id==article_id).all()
    total_sentiments = db.session.query(Comment).filter(Comment.location==art_loc).count()
    # total_negative = db.session.query(Comment).filter(Comment.location==art_loc).\
    #                                           filter(Comment.sentiment_analysis==0).count()
    total_positive = db.session.query(Comment).filter(Comment.location==art_loc).\
                                              filter(Comment.sentiment_analysis==1).count()
    if total_sentiments is not 0:
        percent_positive = (total_positive/total_sentiments)*100
        percent_negative = 100 - percent_positive
    else:
        percent_positive = 0
        percent_negative = 0

    if form.validate_on_submit():
        sentimentScore = sentiment.getSentimentScore(form.description.data)
    
        r = Comment(description=form.description.data, date=dnow, location = art_loc, sentiment_analysis=sentimentScore,user_id=id,article_id=article_id)
        db.session.add(r)
        db.session.commit()
        flash('Successfully Added')
        return redirect(url_for('viewarticle',article_id = article_id))
    return render_template('viewarticle.html', form=form, article_id = article_id, article = article, comments = comments, user_id=user_id, percent_positive=int(percent_positive), percent_negative=int(percent_negative)) #this is where your pass values to be accessed by the front-end rendered template 

#for the paper: sentiment analysis table
@app.route('/commentstable/<location>/', methods=['GET','POST'])
def commentstable(location):
    comments = db.session.query(Comment).filter(Comment.location==location).all()
    return render_template('commentstable.html', comments = comments) 

#for editing an article
@app.route('/edit/<int:article_id>',methods=['GET','POST'])
def edit(article_id):
    article = Article.query.get(article_id)
    form = forms.AddArticleForm()

    if article:
        if form.validate_on_submit():
            article.title = form.title.data
            article.date = dnow
            db.session.commit()
            flash('Successfully Updated')
            return redirect(url_for('index'))
        form.title.data = article.title
        return render_template('edit.html', form=form, article_id = article_id)

    return redirect(url_for('index'))

#for deleting an article
@app.route('/delete/<int:article_id>',methods=['GET','POST'])
def delete(article_id):
    article = Article.query.get(article_id)
    form = forms.DeleteArticleForm()

    if article:
        if form.validate_on_submit():
            db.session.delete(article)
            db.session.commit()
            flash('Record has been deleted')
            return redirect(url_for('index'))
 
        return render_template('delete.html', form=form, article_id = article_id, title=article.title)

    return redirect(url_for('index'))

#for registration
@app.route('/register/', methods = ['POST','GET'])
def register():
    if session.get("user_id") == None:
        session["user_id"] = 1
    user_id =session.get("user_id")

    form = forms.RegistrationForm()
    if form.validate_on_submit():
        user = User(username =form.username.data, email = form.email.data, firstname = form.fname.data, lastname = form.lname.data, middlename = form.mname.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash('Successfully registered!')
        return redirect(url_for('login'))
    return render_template('registration.html', form=form, user_id=user_id)

#for login
@app.route('/login/', methods = ['POST','GET'])
def login():
    if session.get("user_id") == None:
        session["user_id"] = 1
    user_id =session.get("user_id")

    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            session["username"] = user.username
            session["user_id"] = user.id
            return redirect(next or url_for('index'))
        flash('Invalid email address or Password.')  
    return render_template('login.html', form=form, user_id=user_id)

#for logout
@app.route('/logout/', methods = ['POST','GET'])
def logout():
    session["user_id"] = 1
    user_id =session.get("user_id")
    articles = Article.query.order_by(desc(Article.date)).all()
    flash('Successfully logged out of the system.')
    return render_template('index.html', articles = articles, user_id=user_id)

# The login_manager provides the user_loader callback, which is responsible for fetching the current user id. Define the user_loader:
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    # return User.get(user_id)

@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(render_template("404.html"), 404)