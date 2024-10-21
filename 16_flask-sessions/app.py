# Stella Yampolsky
#:(
# SoftDev
#K16: Flask sessions
# October 2024
#Time spent



from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
import os



app = Flask(__name__)
app.secret_key = os.urandom(32)

session[username] = request.cookies.get('username')

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def response():
    if(request.cookies.get('username') is None):
        user = request.args('username')
    else:
        user = request.cookies.get('username')
    return render_template('response.html', username = user )  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
