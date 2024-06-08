from flask import Blueprint, render_template

# Managing the entire view
about_blueprint = Blueprint("about_view", __name__) # "about_view" is the name of the view


@about_blueprint.route("/about") # Route
def about(): # View Function
    return render_template("about.html", active = "about")
