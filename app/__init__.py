import pymysql
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Connect to MySQL database inside Docker
    app.config['MYSQL_HOST'] = 'db'  # Service name in docker-compose.yml
    app.config['MYSQL_USER'] = 'user'
    app.config['MYSQL_PASSWORD'] = 'password'
    app.config['MYSQL_DB'] = 'blind_ctf'

    # Function to establish connection
    def get_db_connection():
        return pymysql.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )

    # Attach database connection function to the app
    app.get_db_connection = get_db_connection

    # Import routes
    from .routes import main
    app.register_blueprint(main)  # Register the Blueprint here

    return app
