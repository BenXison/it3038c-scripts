from flask import Flask, render_template, request
 
app = Flask(__name__) 
app.config.from_object(__name__) 


@app.route('/')
def hell():
   return render_template("index.html")    
@app.route('/welcome', methods=['POST']) 
def welcome(): 
   return render_template("welcome.html", myName=request.form['myName']) 

   
#@app.route('/') 
#@app.route('/welcome', methods=["GET","POST"])
#def welcome(): 
   #name = 'AJ' 
#    return render_template("welcome.html", myName=request.form.get('myName'))


