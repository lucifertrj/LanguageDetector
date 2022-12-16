from flask import Flask,render_template,request
import models

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
    if request.method == 'POST':
        text = request.form['lang']
        return models.predictions(text)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False)