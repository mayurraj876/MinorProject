import pickle
from flask import Flask, request, url_for, redirect, render_template
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("Diabetes.pkl", "rb"))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    text1 = float(request.form['1'])
    text2 = float(request.form['2'])
    text3 = float(request.form['3'])
    text4 = float(request.form['4'])
    text5 = float(request.form['5'])
    text6 = float(request.form['6'])
    text7 = float(request.form['7'])
    text8 = float(request.form['8'])

    row_df = pd.DataFrame(
        [pd.Series([text1, text2, text3, text4, text5, text6, text7, text8])])
    print(row_df)

    prediction = model.predict_proba(row_df)

    print(prediction)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)
    output = float(output)*100

    if output > 50:
        return render_template('result.html', pred=f'You have a chance of having diabetes.\n Probability of having Diabetes is {output}%')
    else:
        return render_template('result.html', pred=f'You are safe.\n Probability of having diabetes is {output}%')


if __name__ == '__main__':
    app.run(debug=True)
