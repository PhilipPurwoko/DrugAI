from flask import Flask, render_template, request, jsonify
import pickle

# App and model initializer
app = Flask(__name__)
with open('ml_model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    unique_label = ['DrugY','drugA', 'drugB', 'drugC', 'drugX']
    data = []
    for i in request.form.values():
        try:
            data.append(int(i))
        except ValueError:
            data.append(float(i))
    data = [data]
    prediction = model.predict(data)
    prediction = unique_label[prediction[0]]

    return render_template('index.html', message='Hasil Prediksi', prediction_text=f'Pecandu merupakan pengonsumsi narkoba {prediction}')


@app.route('/result', methods=['POST'])
def result():
    data = request.get_json(force=True)
    prediction = model.predict([list(data.values())])

    return jsonify(prediction)