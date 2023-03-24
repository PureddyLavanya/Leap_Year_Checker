from flask import Flask
from flask import render_template,request,flash

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sub')
def sub(methods=["GET","POST"]):
    if request.method=="POST":
        yr=request.form['year']
        if yr>0:
            if yr%4==0 and yr%100!=0 or yr%400==0:
                return render_template('sub.html',result="Leap Year")
            else:
                return render_template('sub.html',result="Not a Leap Year")
        else:
            flash("Enter a valid year")
            return render_template('sub.html')
    else:
        return render_template('index.html')
    
if __name__=='__main__':
    app.run(debug=True,port=5010)