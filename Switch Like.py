from flask import Flask, render_template, request
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField

app = Flask(__name__)


@app.route('/min_topup')
def mintopup():
    return render_template('min_topup.html')

@app.route('/about1')
def aboutReach():
    return render_template('about_to_reach1.html')

@app.route('/about2')
def aboutReach2():
    return render_template('about_to_reach2.html')

@app.route('/fixedDeposit')
def fixedDeposit():
    return render_template('draft_FD.html')

@app.route('/fixedDeposit2')
def fixedDeposit2():
    return render_template('draft_fdPart2.html')

@app.route('/switchAccount')
def switchAccount():
    return render_template('switchAccount.html')

@app.route('/homepage')
def homepage():
    return render_template('home.html')

@app.route('/balance')
def balances():
    return render_template('balance.html')

@app.route('/promotions')
def promotions():
    return render_template('promotions.html')

@app.route('/interestGraph')
def interestGraph():
    return render_template('interestGraph.html')

@app.route('/amtFD')
def amtFD():
    return render_template('amt_fixedDeposit.html')

@app.route('/pending')
def pending():
    return render_template('pendingList.html')







if __name__ == '__main__':
    app.run()
