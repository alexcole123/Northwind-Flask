from dotenv import load_dotenv # pip install python-dotenv
from os import environ

# Load .env file into the Environment Variables:
load_dotenv()

class AppConfig:

    is_development = environ.get("ENVIRONMENT") == "development"
    is_production = environ.get("ENVIRONMENT") == "production"

    mysql_host = environ.get("MYSQL_HOST")
    mysql_user = environ.get("MYSQL_USER")
    mysql_password = environ.get("MYSQL_PASSWORD")
    mysql_database = environ.get("MYSQL_DATABASE")

    session_secret_key = environ.get("SESSION_SECRET_KEY")
    passwords_salt = environ.get("PASSWORDS_SALT")
    
    