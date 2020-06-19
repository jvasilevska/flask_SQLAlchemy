#Instructions

##Task - part one (data from CSV file to database) :

###Installation
####Requirements
* Python 3
* PostgreSQL
* virtualenv 


####Setup

* Copy `config.cfg.example` to `config.cfg` with the following command:  
```
cp config.cfg.example config.cfg
```

* Add your credentials for database connection in `config.cfg`
* Create new environment: `python -m venv env`
* Activate the environment: `env\Scripts\activate`
* Install requirements: `pip install -r requirements.txt`
* When done, deactivate environment: `env\Scripts\deactivate.bat`

###Running the script
`python csv_to_db.py`

After running this script a table will be created in the database that will contain the data from the CSV file.


##Task - part two (serve database data to HTML; log requests):

###Installation
####Requirements
* Python 3
* PostgreSQL
* virtualenv 


####Setup

* Copy `config.cfg.example` to `config.cfg` with the following command:  
```
cp config.cfg.example config.cfg
```

* Set your database connection string in `SQLALCHEMY_DATABASE_URI` variable in `config.cfg`
* Create new environment: `python -m venv env`
* Activate the environment: `env\Scripts\activate`
* Install requirements: `pip install -r requirements.txt`
* When done, deactivate environment: `env\Scripts\deactivate.bat`


###Running the script
`python app.py`

* After running the script you should get an url.
Copy the url and paste it in browser in order to view the table with the data.
* A log table will be created in the same database that will contain log information for the GET requests.