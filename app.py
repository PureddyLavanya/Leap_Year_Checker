from flask import Flask
from flask import *

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sub')
def sub(methods=["GET","POST"]):
    if request.method=="POST":
        return render_template('sub.html')
    else:
        return render_template('index.html')
    
if __name__=='__main__':
    app.run(debug=True)