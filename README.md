# 🎨 AI Number Learning Game

An interactive AI-powered learning application that helps children practice writing numbers using handwritten digit recognition.

The application displays a random number, allows children to draw it on a digital canvas, and uses a trained machine learning model to recognize the handwritten digit and provide feedback.

---

## 🚀 Features

✨ Child-friendly interactive interface  
✏️ Digital drawing canvas for handwriting practice  
🤖 AI-based handwritten digit recognition  
🎯 Random number challenges (0-9)  
⭐ Accuracy and progress tracking  
🎉 Positive feedback and encouragement  
🔄 Retry and practice options

---

## 🧠 Machine Learning

This project uses a handwritten digit classification model trained using the **MNIST handwritten digit dataset**.

The model:

- Takes a 28×28 grayscale image as input
- Processes the handwritten digit
- Predicts the digit from 0-9
- Provides confidence estimation for predictions

---

## 🛠️ Technologies Used

### Frontend / Application

- Python
- Streamlit
- Streamlit Drawable Canvas

### Machine Learning

- Scikit-learn
- NumPy
- Joblib
- MNIST Dataset

### Image Processing

- Pillow (PIL)

---

## 📂 Project Structure

```
AI-Number-Learning-Game/
│
├── app.py
├── digit_classifier.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/nathasha-nethmini/Number-Learning-AI.git
```

Move into the project folder:

```bash
cd AI-Number-Learning-Game
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🎮 How It Works

1. A random number is displayed.
2. The child draws the number on the canvas.
3. The drawing is converted into a 28×28 grayscale image.
4. The machine learning model predicts the handwritten digit.
5. The system compares the prediction with the target number.
6. The child receives feedback and can continue practicing.

---

## 📸 Application Preview

(Add screenshots here)

---

## 🔮 Future Improvements

- Replace the current classifier with a CNN-based deep learning model
- Train using children's handwriting samples
- Add difficulty levels
- Add voice-based instructions
- Store learning progress
- Add personalized learning recommendations

---

## 👩‍💻 Author

Your Name

---

## 📜 License

This project is created for educational purposes.
