#Description of development decisions

The solution of the task is in two parts, as the instructions required an application that transfers `task_data.csv` to a database and a separate web application that is able to connect to this database. For both applications a separate virtual environment was created in order to have only the necessary libraries for each installed. This way, the two are independent of one another and can be running on different machines. 

Since no particular requirements were provided for the choice of the database, I decided to use PostgreSQL for the purposes of the task.

For accessing the data in the database (app folder) I used `flask_sqlalchemy`, which is an extension for Flask that adds support for SQLAlchemy. SQLAlchemy allows us to streamline the workflow and query our data more efficiently, and allows us to map the data retrieved from the database with our models. Having said this, we could have also used a specific PostgreSQL database adapter such as `psycopg2` in order to achieve our goal. After accessing the table in the database, the related model is populated with the data and then passed into the view, which can be seen in a browser (see instructions for this in README.md file if necessary).

There are two models built for this app: 
* TaskModel - which uses the already created table with the data from the csv file
* LogModel - which will create a table upon the running of the application that will be used for storing the logs of the GET requests

I am sending you the complete folder on which I was working on, including an initialized bare git repository.
From the `.gitignore` file, you can see that `env` folder and `config` files shouldn't be commited as they are personal and sensitive data.