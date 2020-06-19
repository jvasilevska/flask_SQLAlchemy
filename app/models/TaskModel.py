from db_connection import db

class TaskModel(db.Model):
    __tablename__ = 'task_table'
    __table_args__ = {'useexisting': True}

    
    id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.DateTime)
    temperature = db.Column(db.Float)
    duration = db.Column(db.String(120))

