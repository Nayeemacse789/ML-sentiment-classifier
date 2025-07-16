# ML-sentiment-classifier

# 🎬 Movie Review Sentiment Classifier

This project is a **Machine Learning web app** that predicts whether a movie review is **positive** or **negative** using Natural Language Processing (NLP) and a Naive Bayes classifier.

Built using:
- 🧠 scikit-learn
- 🐍 Python
- 🌐 Flask
- 📊 Basic NLP (Bag-of-Words model)

---

## 🚀 Features

✅ Classify text reviews into **positive** or **negative**  
✅ Simple Flask-based web UI for predictions  
✅ Easily extendable with larger datasets or deep learning  
✅ Clean, minimal structure – ready to showcase on GitHub


## 🛠️ Installation & Running

### Step 1: Install dependencies
```bash
pip install flask pandas scikit-learn joblib
Step 2: Train the model
python train_model.py

Step 3: Run the Flask app

Step 4: Open in your browser

http://127.0.0.1:5000
📊 Dataset
The dataset is a tiny example CSV file with two columns:

review: text of the movie review

sentiment: "positive" or "negative"



💡 Future Improvements
Use a large public dataset (IMDb, Kaggle)
Replace Naive Bayes with LSTM or Transformer (BERT)
Add accuracy graph and confusion matrix
Add REST API endpoint (for integration)


