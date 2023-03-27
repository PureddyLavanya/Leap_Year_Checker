from flask import Flask
from flask import render_template,request,flash

app=Flask(__name__)
app.secret_key="my_secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sub',methods=["GET","POST"])
def sub():
    if request.method=="POST":
        yr=int(request.form['year'])
        if yr>0:
            if yr%4==0 and yr%100!=0 or yr%400==0:
                flash("Leap Year")
                return render_template('index.html')
            else:
                flash("Not a Leap Year")
                return render_template('index.html')
        else:
            flash("Enter a valid year")
            return render_template('index.html')
    else:
        return render_template('index.html')
    
if __name__=='__main__':
    app.run(debug=True,port=5001)