from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import Flask,render_template,session,request,redirect,url_for
from flask.ext.moment import Moment
from datetime import datetime
from models import Models
import random
import traceback
#current_time=datetime.utcnow()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret key'
app.config['ADMIN'] = '1173507862@qq.com'

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
    session['postId'] = Id
    catalogue = mode.selectA('py_Catalogue')
    post = mode.selectAll(Id,'PId','PY_Post')
    comments = mode.selectAll(Id,'PId','PY_Comments')
    PT = mode.selectPT(post[0][4])  
    checknum = obtainnumber()
    return render_template('post.html',post = post[0],catalogue = catalogue,PostTi = PT,comments = comments,checknum=checknum)

@app.route("/comment",methods=['GET','POST'])
def comment():
    if request.method == 'POST':
        Id = session.get('postId')
        email = request.form["email"]
        password = request.form["password"]
        # session['email'] = email 
        # Id = request.args.get('Id','')
        # print(session.get('email'))
        # Id = session.get('postId')
        # print(Id)
    return redirect(url_for('post',Id = Id))

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if mode.login(email,password) is  True:
            return email,password
        else:
            return "PasswordIsWrong"
        # if mode.login(email,password):
        #     if email == app.config['ADMIN']:
        #         return redirect(url_for('/admin'))
        #     else:
        #         return redirrct(url_for('/index'))
        # else:
        #     # return 'false'
        #     # flash("You haven't sign in Or you mistake the password!")
@app.route("/register",methods=['GET','POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    if mode.register() is False:
        return "Email Has Been Registered!"
    else:
        sendemail(email)
        return "Please check your email!"

@app.route('/obtainnumber')
def obtainnumber():
    num=""
    numbers = random.sample((1,2,3,4,5,6,7,8,9),4)
    for i in numbers:
       num += str(i)
    session['checknum'] = num
    return num

def sendemail(email):
    pass

#加密
def encryption(expiration=3600,data):
    s = Serializer(app.config['SECRET_KEY'], expiration)
    return s.dumps(data)

def decode():
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return False

if __name__ == '__main__':
    app.run(debug=True)

