from sqlalchemy import create_engine
import pandas as pd
import os


csv_data = pd.read_csv('assets/skiresorts.csv')


df = pd.DataFrame(csv_data)


db_protocol = 'postgresql+psycopg2'
if "RDS_DB_NAME" in os.environ:
    db_host = os.environ.get('RDS_HOSTNAME', '')
    db_name = os.environ.get('RDS_DB_NAME', '')
    db_password = os.environ.get('RDS_PASS', '')
    db_user = os.environ.get('RDS_USERNAME', '')
else:
    db_host = os.environ.get('DB_HOST', '')
    db_user = os.environ.get('DB_USER', '')
    db_pass = os.environ.get('DB_PASS', '')
    db_name = os.environ.get('DB_NAME', '')

engine = create_engine('{}://{}:{}@{}:5432/{}'.format(
    db_protocol, db_user, db_pass, db_host, db_name
))

df.to_sql("board_resort", engine, if_exists='append', index=False)
print(df)
