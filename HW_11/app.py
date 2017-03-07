from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm
from datetime import date
from sqlalchemy.orm import relationship


import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

#Tables

class User(db.Model):
    id = db.Column(db.Integer, primery_key = True, autoincrement = True)
    name = db.Column(db.String(20), unique = True, nullable = False)

    def __str__(self):
        return '<Name %r>' % self.name

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    date = db.Column(db.Date, default = date.today)
    title = db.Column(db.String(50))
    text = db.Column(db.String(200), nullable = False)
    author = db.Column(db.Integer, db.ForegnKey('author'), nullable = False, index = True)
    tags = relationship("Tag", back_populates = "posts")
    slugfield = db.Column(db.String(100), unique = True)
    is_visible = db.Column(db.Boolean, default = True)

#SlugField
    # @observes('title', 'date')
    # def slug_url(self, title, date):
    #     self.slugfield = re.sub(''[^\w]+', '-', title.lower(), date.lower())

#Post by date
    # @staticmethod
    # def newest(num):
    #     return Post.query.order_by(desc(Post.date)).limit(num)

    def __str__(self):
        return '<Title %r>' % self.title

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), unique = True)
    post_id = db.Column(db.Integer, db.ForegnKey('post.id'), nullable = False, index = True)
    posts = relationship("Post", back_populates = "tags")

    def __str__(self):
        return '<Name %r>' % self.name

#Forms

class UserForm(ModelForm):
    class Meta:
        model = User

class PostForm(ModelForm):
    class Meta:
        model = Post
        include = ['author']

class TagForm(ModelForm):
    class Meta:
        model = Tag


#app

@app.route('/user', methods = ['GET', 'POST'])
def index_user():
    if request.method == 'POST':
        print(request.form)
        form = UserForm(request.form)

        if form.validate():
            user = User(**form.data)
            db.session.add(user)
            db.session.commit()

            flash('New User was added')
        else:
            flash('Wrong data for User')

    users = User.query.all
    return render_template('template.txt', users = users)

@app.route('/post', methods = ['GET', 'POST'])
def index_post():
    if request.method == 'POST':
        print(request.form)
        form = PostForm(request.form)

        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()

            flash('New Post was added')
        else:
            flash('Wrong data for Post')

    posts = Post.query.all
    return render_template('template.txt', posts = posts)

@app.route('/tag', methods = ['GET', 'POST'])
def index_tag():
    if request.method == 'POST'
        print(request.form)
        form = TagForm(request.form)

        if form.validate():
            tag = Tag(**form.data)
            db.session.add(tag)
            db.session.commit()

            flash('New tag was added')
        else:
            flash('Wrong data for Tag')

    tags = Post.query.all
    return render_template('template.txt', tags = tags)



if __name__ == '__main__':
    db.create_all()

    app.run()