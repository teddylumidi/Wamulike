from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wins.db'
db = SQLAlchemy(app)


class Win(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    betting_site = db.Column(db.String(100), nullable=False)
    betting_id = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Win {self.id}>'


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/wins', methods=['POST'])
def add_win():
    data = request.get_json()
    betting_site = data['betting_site']
    betting_id = data['betting_id']
    date = data['date']
    win = Win(betting_site=betting_site, betting_id=betting_id, date=date)
    db.session.add(win)
    db.session.commit()
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(port=8080)
