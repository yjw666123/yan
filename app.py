from flask import Flask,request,render_template

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
  return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
  r=request.form.get("r")
  return(render_template("main.html",r=r))

@app.route("/imagegpt",methods=["GET","POST"])
def image_gpt():
  return(render_template("imagegpt.html"))

@app.route("/end",methods=["GET","POST"])
def end():
  first_time=1
  return(render_template("end.html"))

  if __name__=="__main__":
         app.run()
