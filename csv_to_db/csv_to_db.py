import psycopg2
from configparser import ConfigParser


def drop_tables(conn):
    print('Dropping tables...')
    cur = conn.cursor()
    cur.execute( 'DROP TABLE IF EXISTS task_table' )
    cur.close()
    conn.commit()
    print('Dropping tables finished')

def create_table(conn):
    print('Creating table...')
    cur = conn.cursor()
    cur.execute( 'CREATE TABLE IF NOT EXISTS task_table ('
                 'ID INTEGER PRIMARY KEY,'
                 'TIME_STAMP TIMESTAMP,'
                 'TEMPERATURE FLOAT,'
                 'DURATION VARCHAR(120)'
                 ');'
                 )
    cur.close()
    conn.commit()
    print('Creating table finished')

def import_data_from_file(conn, filename):
    print('Importing data from CSV file...')
    cur = conn.cursor()
    with open( '../{}'.format(filename), 'r' ) as f:
        next(f)
        for row in f:          
            cur.execute("INSERT INTO task_table (ID, TIME_STAMP, TEMPERATURE, DURATION) VALUES (%s, %s, %s, %s)", row.split(","))          
    cur.close()
    conn.commit()
    print('Importing data finished')



def config(filename, section):    
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    section_config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            section_config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return section_config



postgresql_config = config('config.cfg', 'postgresql')
conn = psycopg2.connect( **postgresql_config )
drop_tables(conn)
create_table(conn)
import_data_from_file(conn,'task_data.csv')
conn.close()