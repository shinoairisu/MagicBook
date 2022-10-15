# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,Response,url_for,send_from_directory,redirect,jsonify
import requests,json,os
from flask_cors import CORS

app = Flask(__name__)
#解决跨域问题
CORS(app, origins="*")
app.secret_key = 'app2app'  #最好要指定这个参数

@app.route("/index2")
def hello2():
    return render_template("index2.html")



@app.route("/",methods=['GET', 'POST'])
def index():
    aa=request.json
    print(aa)
    return jsonify({"uuid":123})

@app.route("/1")
def index2():
    return redirect(url_for("static",filename="html/vue-element.html"))

@app.route("/2")
def index3():
    return redirect(url_for("static",filename="html/boot-jquery-vue-test.html"))

@app.route("/hello")
def hello():
    return render_template("test.html",test=15)

@app.route('/json')
def root():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return Response(json.dumps(t), mimetype='application/json')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__=="__main__":
    app.run(port= 5000,debug=True)