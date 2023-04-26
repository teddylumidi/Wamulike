from app import db


class Win(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    betting_site = db.Column(db.String(50), nullable=False)
    betting_id = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Win {self.id}>'
