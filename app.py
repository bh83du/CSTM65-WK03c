# Import Flask and render-template.
from flask import Flask, render_template

# Define the app 

app = Flask(__name__)

# Add function for the default route

@app.route('/')
def index():
    users = ['Stuart','Joe','Frank']
    return render_template('index.html', title = 'Home', users=users)

# Add further functions for the User routes.
# Each route takes the end user to a page for the selected User.
# User page is an extension of the layout.html
# Can be used to produce identical pages for different users
  
@app.route('/Stuart')
def stuart():
    return render_template('user.html', title = 'Home', users='Stuart')

@app.route('/Joe')
def joe():
    return render_template('user.html', title = 'Home', users='Joe')

@app.route('/Frank')
def frank():
    return render_template('user.html', title = 'Home', users='Frank')


# Debugging is ON
app.run(debug=True)
