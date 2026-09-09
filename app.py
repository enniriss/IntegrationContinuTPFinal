from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<p>Hello, World!</p>"

@app.route("/health")
def heath():
   return {"status" : "ok" }

if __name__== "__main__":

   app.run('0.0.0.0',port=8000)
