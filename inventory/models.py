from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Inventory(db.Model):
    """
    Sample Inventory Table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=100), nullable=False)
    description = db.Column(db.String(length=100), nullable=False)
    itemscount = db.Column(db.Integer)

    def __repr__(self) -> str:
        return "<Course id {}>".format(self.id)


