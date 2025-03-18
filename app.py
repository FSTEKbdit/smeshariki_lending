from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/characters')
def characters():
    return render_template('characters.html')

@app.route('/episodes')
def episodes():
    return render_template('episodes.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        author = request.form['author']
        content = request.form['content']
        new_comment = Comment(author=author, content=content)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('comments'))
    all_comments = Comment.query.all()
    return render_template('comments.html', comments=all_comments)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)