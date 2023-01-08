from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Fine_particles = float(request.form['Fine_particles'])
    Coarse_particles = float(request.form['Coarse_particles'])
    NO = float(request.form[' NO'])
    NO2 = float(request.form['NO2'])
    NOx = float(request.form['NOx'])
    NH3 = float(request.form['NH3'])
    CO = float(request.form[' CO'])
    SO2 = float(request.form['SO2'])
    O3 = float(request.form['O3'])
    Benzene = float(request.form['Benzene'])
    Toluene = float(request.form['Toluene'])
    Xylene = float(request.form['Xylene'])
    result = model.predict([[Fine_particles, Coarse_particles, NO, NO2, NOx,NH3, CO, SO2, O3,Benzene,Toluene,Xylene]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(port=3333)