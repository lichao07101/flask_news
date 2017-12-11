from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from forms import NewsForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/lichao'
app.config['SECRET_KEY'] = 'a random string'
db = SQLAlchemy(app)

class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    body = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<News %r>' % self.title

@app.route('/',methods=['GET', 'POST'])
def index():
    form = NewsForm()
    if form.validate_on_submit():
        n1 = News(
            title=form.title.data,
            body=form.body.data
        )
        db.session.add(n1)
        db.session.commit()
        return redirect(url_for('index'))
    news_list = News.query.all()
    return render_template('index.html',news_list = news_list,form=form)

@app.route('/body/<int:id>')
def body(id):
    news = News.query.get(id)
    return render_template('body.html',news = news)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')