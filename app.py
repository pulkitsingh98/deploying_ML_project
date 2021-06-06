from flask import Flask, render_template, request

import model as m
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def hello():
    # global yearly_amount_spent
    name = ''
    yas = 0 
    if request.method == 'POST':
        nam = request.form['username']
        sl = request.form['sl']
        toa = request.form['toa']
        tow = request.form['tow']
        lom = request.form['lom']
        ll = [sl,toa,tow,lom]
        yearly_amount_spent = m.model_prediction(ll)
        yas = yearly_amount_spent
        name = nam
    return render_template('index.html',yas=yas,name=name)

# @app.route('/sub', methods = ['POST'])
# def submit():
#     if request.method == "POST":
#         name = request.form['username']

#     return render_template('sub.html',n = name)

if __name__=='__main__':
    app.run(debug=True)

