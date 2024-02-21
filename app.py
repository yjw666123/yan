from flask import Flask,request,render_template
import replicate
import os
import time

app=Flask(__name__)
os.environ["REPLICATE_API_TOKEN"]="787f515cb0624813736c11e7fefec66473394f02"

r=""
first_time=1

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    global r,first_time
    if first_time==1
    r=request.form.get("r")
    first_time=0
    return(render_template("main.html",r=r))

@app.route("/image_gpt",methods=["GET","POST"])
def image_gpt():
    return(render_template("image_gpt.html"))

@app.route("/image_result",methods=["GET","POST"])
def image_result():
     q=request.form.get("q")//前端——后端
        r//后端 = replicate.run(
    "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
    input={
        "prompt": q,//后端
         }
    )
    time.sleep(10)   
    return(render_template("image_gpt.html",r//前端=r[0]//后端))

@app.route("/end",methods=["GET","POST"])
def end():
    global first_time
    first_time=1
    return(render_template("end.html"))

if __name__=="__main__":
         app.run()
