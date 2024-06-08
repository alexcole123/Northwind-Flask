from flask import Flask, render_template, request
from views.home_view import home_blueprint
from views.about_view import about_blueprint
from views.products_view import products_blueprint
from views.api_view import api_blueprint
from views.auth_view import auth_blueprint
from logging import getLogger, ERROR
from utils.app_config import AppConfig
from utils.logger import Logger
from flask_limiter import Limiter, util #pip install flask-limiter

# flask --app src/app.py run --debug
# Website is at: http://localhost:5000/

# Creating Flask server:
app = Flask(__name__)

#prevent DOS attack
Limiter(
    util.get_remote_address, #user remote IP address
    app = app, #Our Flask app object
    default_limits = ["10 per second"], # How many request per window of time
    storage_uri = "memory://", #Save data in memory and not in some file
    default_limits_exempt_when = lambda: "products/images" in request.url
)

# Create session secret key:
app.secret_key = AppConfig.session_secret_key

# Registering all routes: 
app.register_blueprint(auth_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(api_blueprint)

# Catch any 404 route: 
@app.errorhandler(404)
def page_not_found(error): # error = an object containing details about the 404 error.
    return render_template("404.html")

# Catch any unhandled exception error:
@app.errorhandler(Exception)
def catch_all(error):
    print(error)
    Logger.log(error) #log any system error
    error_message = error if AppConfig.is_development else "Some error, please try again." # For security
    return render_template("500.html", error = error_message)


# Quiet console (werkzeug = ארגז כלים): 
getLogger("werkzeug").setLevel(ERROR)

# Display website address on terminal:
print("Listening on http://localhost:5000")
