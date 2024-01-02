# an object of WSGI application
from flask import Flask, render_template
# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function


@app.route('/')
def home():
   return(render_template("homepage.html"))



if __name__=='__main__':
   app.run()

#Testing