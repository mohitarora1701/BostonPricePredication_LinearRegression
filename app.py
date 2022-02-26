from flask import Flask, render_template, redirect, url_for, request, current_app
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():

    data=[]
    data2=[]
    if request.method == 'POST':
        print("Post Call")
        if request.form.get('pred') == 'Predict':
            print("Prediction")
            model = pickle.load(current_app.open_resource('model.pkl'))
            print(model)
            lstat = request.form.get('population')
            rad = request.form.get('highways')
            indus = request.form.get('non_retail')
            nox = request.form.get('nitric_oxide')
            rm = request.form.get('nitric_oxide')
            tax = request.form.get('tax')
            ptratio = request.form.get('teacher')
            print(lstat,rad,indus,nox,rm,tax,ptratio)
            data.append(float(lstat))
            data.append(float(rad))
            data.append(float(indus))
            data.append(float(nox))
            data.append(float(rm))
            data.append(float(tax))
            data.append(float(ptratio))
            data2.append(data)
            # data = [[float(lstat), float(rad), float(indus), float(nox), float(rm), float(tax), float(ptratio)]]
            print(data2)
            prediction = model.predict(data2)

            print("Prediction:",prediction)
            prediction=prediction[0]*1000
            print(prediction)
            pred="{:.2f}".format(prediction)
            print(pred)
            final_price=f"${str(pred)}"
            return render_template('predict.html', prediction=final_price)
        if request.form.get('back') == 'Back':
            print("Prediction")
            return render_template('index.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
