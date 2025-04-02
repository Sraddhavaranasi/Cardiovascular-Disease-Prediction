
# 🩺 Cardiovascular Disease Prediction  

A Machine Learning project to predict the risk of cardiovascular disease using patient health data.

## 🚀 Overview  
This project leverages **Support Vector Machine (SVM)** to predict whether a person is at risk of cardiovascular disease based on health-related parameters.  
It provides a **Flask web application** where users can input values and get predictions.

---

## 📂 Project Structure  
```
E:\Cardiovascular_disease_prediction\
│── app.py                    # Flask API for prediction  
│── Cardiovascular_model.ipynb # Model training notebook  
│── SVM_model_accuracy_0.729857.joblib  # Trained SVM model  
│── cardio_train.csv.zip       # Dataset (not included in Git)  
│── templates\  
│   └── index.html             # Frontend UI  
│── static\                    # (For CSS/JS files if needed)  
│── requirements.txt           # Dependencies  
│── .gitignore                 # Files to ignore  
│── README.md                  # Project documentation  
```

---

## 📊 Dataset  
- **Dataset Name**: `cardio_train.csv.zip`  
- **Source**: [UCI Repository](https://archive.ics.uci.edu/ml/datasets/heart+disease)  
- **Description**: Contains various patient health metrics, such as age, cholesterol, blood pressure, and more.  

### Features Used:
| Feature | Description |
|---------|-------------|
| `age` | Age of the person |
| `gender` | 1: Male, 0: Female |
| `cholesterol` | Cholesterol levels |
| `bp_high` | High blood pressure level |
| `bp_low` | Low blood pressure level |
| `glucose` | Glucose levels |
| `smoking` | 1: Smoker, 0: Non-smoker |
| `alcohol` | 1: Drinks alcohol, 0: Does not drink |

---

## ⚙️ Installation & Setup  
### **1️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows
```

### **2️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Flask App**  
```sh
python app.py
```
- Open **http://127.0.0.1:5000/** in your browser.

---

## 🖥️ Usage  
1. **Open the web app** in a browser.  
2. **Enter feature values** (age, cholesterol, BP, etc.).  
3. **Click "Predict"** to get a risk assessment result.  

---

## 🛠️ Model Details  
- **Algorithm Used**: Support Vector Machine (SVM)  
- **Accuracy**: `72.98%`  
- **Trained on**: `cardio_train.csv` dataset  
- **Saved Model**: `SVM_model_accuracy_0.729857.joblib`  

---

## 📸 UI Preview  
![Cardio Prediction App](https://via.placeholder.com/600x300?text=App+Screenshot)  

---

## 📌 To-Do & Future Enhancements  
✅ Improve UI with Bootstrap  
✅ Add More Model Comparisons (Random Forest, XGBoost, etc.)  
🔲 Deploy to **Render** or **Heroku**  
🔲 Integrate **API for real-time prediction**  

---

## 📜 License  
This project is **MIT Licensed**. Feel free to use or improve it.  

---

## 🙌 Contributing  
Contributions are welcome!  
To contribute:  
1. **Fork the repository**  
2. **Create a new branch** (`git checkout -b feature-name`)  
3. **Commit your changes** (`git commit -m "Added feature"`)  
4. **Push and create a pull request**  

---

## 📝 Author  
**Sraddha Varanasi**  
💼 GitHub: [your-github-profile](https://github.com/your-username)  
📧 Email: your.email@example.com  
```
