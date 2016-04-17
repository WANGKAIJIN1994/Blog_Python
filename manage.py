from flask import Flask,render_template,session,request,redirect
from flask.ext.moment import Moment
from datetime import datetime
from models import Models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the Secret key'
moment = Moment(app)

@app.route('/')
@app.route("/index")
def index():
    return render_template('/index.html',current_time=datetime.utcnow())
  
@app.route("/catalogue")
def catalogue():
    Id = request.args.get('Id','')
    print(Id)
    return render_template('catalogue.html')

@app.route("/catalogue/post")
def post():
    Id = request.args.get('Id','')
    catalogue = Models().selectCa()
    post = Models().selectAll(Id,'PId','PY_Post')
    PT = Models().selectPT(post[0][4])
    return render_template('post.html',post = post[0],catalogue = catalogue,PostTi = PT)
 
@app.route("/login",methods=['GET','POST'])
def login():
    
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        session['username'] = username 
        if username == 'wk':
             return redirect('login')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
