#Udacity Item Catalog Project
###Project made for Udacity's Full Stack Web Developer Nanodegree

This is a python module that creates a website and JSON API for a list of items grouped into a category. Users can edit or delete items they've creating. Adding items, deleteing items and editing items requiring logging in with Google+.

## Instrucitons to Run Project

### Set up a Google Plus auth application.
1. go to https://console.developers.google.com/project and login with Google.
2. Create a new project
3. Name the project
4. Select "API's and Auth-> Credentials-> Create a new OAuth client ID" from the project menu
5. Select Web Application
6. On the consent screen, type in a product name and save.
7. In Authorized javascript origins add:
    https://0.0.0.0:8080
    https://localhost:8080
8. Click create client ID
9. Open /catalog/config.py and edit  with the provided infos
11. In /catalog/site/templates/main.html replace the line
"781544697558-3gjnobb4utugg6f867i3m3ekpkg3jm50.apps.googleusercontent.com" so that it uses your Client ID from the web applciation.

### Setup the Database & Start the Server
1. Start up your VM, go to the application root and type "python
database_setup.py" this will create the database.
2. Type "python database_seed.py" to seed the database with some dummy data.
3. Type "pip install -r dependencies.txt" to install the dependencies.
4. Type "python run.py"

### Open in a webpage
1. Now you can open in a webpage by going to either:
    https://0.0.0.0:5000
    https://localhost:5000

