# 🔥 FitBurn - Calories Burnt Prediction Web App

A modern web application that predicts calories burnt based on user input such as age, weight, gender, heart rate, etc. Built with **FastAPI**, **TailwindCSS**, and an ML pipeline trained using **XGBoost**.

---

## 📦 Features

- 🧠 Predict calories burnt using a trained machine learning model
- 🧪 Includes a preprocessing pipeline for feature scaling and encoding before prediction
- 🎨 Clean, responsive UI with Tailwind CSS
- 🚀 FastAPI backend for fast, async request handling
- 📂 Pickle-based ML pipeline loading with `.env` support
- 📈 Model built with `XGBoost` and `scikit-learn`

---

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python
- **Frontend**: HTML, Tailwind CSS
- **ML Libraries**: pandas, scikit-learn, xgboost
- **Other**: Jinja2, python-dotenv

---

## 📁 Project Structure

```
Calories-Predictor/
│
├── app.py                  # Main FastAPI app
├── pipeline_model.pkl      # Pickled ML pipeline
├── .env                    # Environment variable for secure file paths
│
├── templates/              # HTML templates
│   ├── index.html          # Form for user input
│   └── result.html         # Prediction display
│
└── README.md               # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/calories-predictor.git
cd calories-predictor
```

### 2️⃣ Create and Activate Virtual Environment (optional)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, run:

```bash
pip install fastapi uvicorn jinja2 python-dotenv pandas scikit-learn xgboost
```

### 4️⃣ Add `.env` File

Create a `.env` file in the root with the following:

```
MODEL_PATH=pipeline_model.pkl
```

---

## ▶️ Running the App

```bash
uvicorn app:app --reload
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Example Input

- Gender: Female
- Age: 24
- Height: 165 cm
- Weight: 60 kg
- Duration: 30 min
- Heart Rate: 120 bpm
- Body Temp: 37.2 °C

➡️ Returns: `Calories Burnt: 240.5 kcal` (example)
