from db_connection import db

class LogModel(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.DateTime)
    uri = db.Column(db.String(255))
    method = db.Column(db.String(10))
    headers = db.Column(db.Text)
    body = db.Column(db.Text)
    
 
