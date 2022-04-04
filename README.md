# Web_Scraping_Challenge
# Mission To Mars

## Background
Known as the Red Planet because of the iron in the soil, Mars is the fourth planet from the sun. Mars has two moons namely, Phobos and Deimos. With the nature of the soil on Mars, the planet can have huge dust storms that can last for months and can cover the enire planet. 
In this project, I built a web application that is used to scraped different sites with information and data relating to Mars. The information scraped is displaced in a single HTML page for viewing. The different stages or steps involved in this project are outlined below.
 
## Step 1 - Scraping
Using Jupyter Noebook, BeautifulSoup, Pandas, and Splinter, the different urls were able to be scraped. A Jupyter Notebook named Mission_to_Mar.ipnyb was created to contain the code used for scraping the different sites.

### NASA Mars News
The Mars News Site was scraped at (https://redplanetscience.com/) and the latest News Title and Paragraph Text were collected.

### JPL Mars Space Images - Featured Image
I then visited the url for the Featured Space Image site (https://spaceimages-mars.com). While at this site, I scraped the featured image and then created the complete url string to the featured image.

### Mars Facts
I then visited the Mars Facts webpage at (https://galaxyfacts-mars.com) and using Pandas, I scraped the table containing facts about the planet including Diameter, Mass, etc. The information scraped was then converted to HTML table string.

### Mars Hemispheres
I then visited the astrogeology site (https://marshemispheres.com/) to obtain high resolution images for each of the Mar's hemispheres: Cerberus, Schiaparelli, Syrtis Major, and Valles Marineris.
The code is designed so a click on each link can take you to the respective hemisphere and provide more information and picture.

## Step 2 - MongoDB and Flask Application
Using MongoDB with Flask templating, I created a new HTML page that displays the different information scraped above. I then converted the Jupyter Notebook into a Python script called scrape_mars.py with a function called "scrape" to execute the code and return a Python dictionary that contains all the scraped information. 
The route "/scrape" was also created to directly import the scrape_mars.py script where the returned values are stored in the MongoDB as a Python Dictionary. 
I then created a a root route `/` that will query the Mongo database and pass the mars data into an HTML template to display the data.
The HTML template file "index.html" was then created. This will take the mars data dictionary and display all of the data in the appropriate HTML elements.


