
# Importing the Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Creating an instance of Flask
app = Flask(__name__)

# Using PyMongo to establish Mongo connection
#mongo = PyMongo(app, url="mongodb://localhost:27017/mars_app")
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_dict = mongo.db.mars_dicts.find_one()
    # Return template and data
    return render_template("index.html", mars_dict=mars_dict)


@app.route("/scrape")
def scraper():
    mars_dicts = mongo.db.mars_dicts
    mars_data = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    mars_dicts.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)