from flask import Flask, request, render_template
from db_connection import db, save_to_db
from flask_migrate import Migrate
from models.TaskModel import TaskModel
from models.LogModel import LogModel
from datetime import datetime
import json

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
migrate = Migrate(app, db)

@app.route('/')
def task_output():
    output_data = TaskModel.query.all()
    return render_template('template.html', data=output_data)

@app.before_request
def log_request_info():
    if request.method != 'GET':
        pass
    data = LogModel(
        time_stamp=datetime.now(), 
        uri=request.path, 
        method=request.method, 
        headers=json.dumps({k:v for k, v in request.headers.items()}), 
        body=request.get_json()
        )
    save_to_db(data)

if __name__ == '__main__':
    db.init_app(app)
    db.create_all(app=app)
    app.run(port=5000, debug=True)