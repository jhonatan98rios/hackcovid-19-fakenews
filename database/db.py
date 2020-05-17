import mysql.connector
import sqlalchemy
from databases.auth import user, passw

class DBConnection():

    def __init__(self):
        self.engine = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="mysql+pymysql",
                username=user,
                password=passw,
                database="hackcovid",
                query={"unix_socket": "/cloudsql/advance-verve-276519:southamerica-east1:hack-db-276519"},
            ),
        )

    # mysql://bfd39fe701d7d0:23259851@us-cdbr-east-06.cleardb.net/heroku_84757032c7e3a7d?reconnect=true

    # Create a new user

    def create_user(self, name, job):
        connection = self.engine.raw_connection()
        try:
            cursor = connection.cursor()
            sql = "INSERT INTO users (name, job) VALUES (%s, %s)"
            val = (name, job)
            cursor.execute(sql, val)
            cursor.close()
            connection.commit()
        finally:
            connection.close()


    # Return all users
    def read_all(self):
        array = []
        connection = self.engine.raw_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            for user in result:
                document = {
                    "name" : user[0],
                    "job": user[1]
                }
                array.append(document)
            
            cursor.close()
            connection.commit()
        finally:
            connection.close()
        return array
