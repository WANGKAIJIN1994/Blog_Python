from flask import Flask,render_template,session,request,redirect
from flask.ext.moment import Moment
from datetime import datetime
from models import Models
#current_time=datetime.utcnow()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the Secret key'
moment = Moment(app)
mode = Models()

@app.route('/')
@app.route("/index")
def index():
    catalogue = mode.selectA('py_Catalogue')
    post = mode.selectA('PY_Post')
    comments = mode.selectA('PY_Comments')
    return render_template('/index.html',catalogue = catalogue,posts = post,comments = comments)
  
@app.route("/catalogue")
def catalogue():
    Id = request.args.get('Id','')
    catalogue = mode.selectA('py_Catalogue')
    post = mode.selectAll(Id,'CaId','PY_Post')
    comments = mode.selectA('PY_Comments')
    return render_template('catalogue.html',catalogue = catalogue,posts = post,comments = comments)

@app.route("/catalogue/post")
def post():
    Id = request.args.get('Id','')
    catalogue = mode.selectA('py_Catalogue')
    post = mode.selectAll(Id,'PId','PY_Post')
    comments = mode.selectAll(Id,'PId','PY_Comments')
    PT = mode.selectPT(post[0][4])  
    return render_template('post.html',post = post[0],catalogue = catalogue,PostTi = PT,comments = comments)
 
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
