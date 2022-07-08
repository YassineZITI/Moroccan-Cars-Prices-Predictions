from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods = ['POST'])
def predict():
    
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Fuel_Type_Essence = request.form['Fuel_Type']
        if(Fuel_Type_Essence == 'Essence'):
            Fuel_Type_Essence = 1
        else:
            Fuel_Type_Essence = 0
            
        Year = 2020-Year

        	
        Transmission_Manuelle = request.form['Transmission_Type']
        if(Transmission_Manuelle == 'Manuelle'):
            Transmission_Manuelle = 1
        else:
            Transmission_Manuelle = 0
        prediction = model.predict([[Year,Kms_Driven,Present_Price,Transmission_Manuelle,Fuel_Type_Essence]])
        output = round(prediction[0])
        if output < 0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at",prediction = output)
    else:
        return render_template('index.html',prediction_text='')

if __name__ == "__main__":
    app.run(debug=True)