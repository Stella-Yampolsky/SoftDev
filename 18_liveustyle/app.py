# Stella Yampolsky
#JST
# SoftDev
#K18
# October 2024
#Time spent 20 minutes



from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating



app = Flask(__name__)


@app.route("/")
def run():
    return render_template('index.html')


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
