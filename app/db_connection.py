from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def save_to_db(model):
    db.session.add(model)
    db.session.commit()