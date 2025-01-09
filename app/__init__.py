import pymysql
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['MYSQL_HOST'] = 'db'
    app.config['MYSQL_USER'] = 'user'
    app.config['MYSQL_PASSWORD'] = 'password'
    app.config['MYSQL_DB'] = 'blind_ctf'

    # Database connection function
    def get_db_connection():
        return pymysql.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )

    app.get_db_connection = get_db_connection

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app
