from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load("models/sentiment_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    prediction = model.predict([review])[0]
    return render_template('index.html', prediction=prediction, review=review)

if __name__ == "__main__":
    app.run(debug=True)
