from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def Welcome():
    return render_template("main.html") 

@app.route("/product")
def product():
    return render_template("product.html")


@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name =  request.form['name']
        return f'hello {name}!!'
    return render_template('form.html')

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score>50:
        res="PASSED"
    else:
        res="FAILED"
    
    return render_template('result.html',results = res)

if __name__=="__main__":
    app.run(debug=True)