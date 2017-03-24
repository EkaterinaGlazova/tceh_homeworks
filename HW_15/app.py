from flask import Flask, request, render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm
import json


import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(10), nullable = False)
    comment = db.Column(db.String(100), nullable = False)

    def __init__(self, name, comment):
        self.name = name
        self.comment = comment

@app.route('/', methods=['GET'])
def run():
    return render_template('index.html')


@app.route('/comment', methods=['POST'])
def Comment_add():
    class CommentForm(ModelForm):
        class Meta:
            model = Comment

    form = CommentForm(request.form)

    if form.validate():
        comment = Comment(request.form['name'], request.form['comment'])
        db.session.add(comment)
        db.session.commit()
        flash('New comment was added')
        result = {"status": True, "statusText": "Ok"}
    else:
        flash(str(form.errors))
        result = {"status": False, "errors": form.errors}

    return jsonify(result)



if __name__ == '__main__':
    db.create_all()
    app.run()