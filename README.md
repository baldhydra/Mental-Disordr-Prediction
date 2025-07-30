# Mental Disorder Prediction System

A machine learning-based web application that predicts mental disorders based on user-input symptoms and behavioral patterns. This project uses a Random Forest Classifier trained on mental health data to provide preliminary assessments.

## 🧠 Features

- **Interactive Web Interface**: User-friendly form-based input system
- **Comprehensive Symptom Assessment**: Evaluates multiple mental health indicators
- **Real-time Prediction**: Instant results using trained machine learning model
- **Responsive Design**: Works on desktop and mobile devices
- **Privacy-Focused**: Local processing with no data storage

## 📋 Assessment Categories

The system evaluates users across three main categories:

### 1. Symptom Frequency (4 questions)
- Sadness levels
- Euphoric feelings
- Exhaustion
- Sleep disorders

### 2. Behavioral Patterns (10 questions)
- Mood swings
- Suicidal thoughts
- Anorexia
- Authority respect
- Communication patterns
- Aggressive responses
- Coping mechanisms
- Nervous breakdowns
- Self-awareness
- Overthinking tendencies

### 3. Life Quality Metrics (3 questions)
- Sexual activity (1-10 scale)
- Concentration levels (1-10 scale)
- Optimism levels (1-10 scale)

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Frontend**: HTML, CSS
- **Model Persistence**: Joblib
- **Data Processing**: NumPy, Pandas

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Mental-Disordr-Prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv myvenv
   ```

3. **Activate the virtual environment**
   
   **Windows:**
   ```bash
   myvenv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source myvenv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install flask scikit-learn joblib numpy pandas
   ```

## 🚀 Usage

1. **Start the application**
   ```bash
   python app2.py
   ```

2. **Open your web browser**
   Navigate to `http://localhost:5000`

3. **Complete the assessment**
   - Fill out all required fields in the form
   - Be honest and accurate with your responses
   - Click "Predict" to get your results

4. **Review results**
   - The system will display the predicted mental disorder category
   - Results are for educational purposes only

## 📁 Project Structure

```
Mental-Disordr-Prediction/
├── app2.py                 # Main Flask application
├── model.joblib           # Trained machine learning model
├── templates/
│   ├── index.html         # Assessment form page
│   └── result.html        # Results display page
├── myvenv/                # Virtual environment
└── README.md             # This file
```

## 🔧 Model Details

- **Algorithm**: Random Forest Classifier
- **Features**: 17 input features (4 symptoms + 10 behaviors + 3 metrics)
- **Training**: Model trained on mental health dataset
- **Output**: Mental disorder classification

## ⚠️ Important Disclaimers

- **Not Medical Advice**: This tool is for educational and research purposes only
- **No Diagnosis**: Results should not be considered as medical diagnosis
- **Professional Consultation**: Always consult qualified mental health professionals for proper assessment
- **Crisis Support**: If you're experiencing a mental health crisis, contact emergency services or crisis hotlines



## 🔒 Privacy

- No user data is stored or transmitted
- All processing occurs locally on your device
- No personal information is collected
- Results are not saved or shared

---

**Remember**: Mental health is important. This tool is designed to raise awareness and encourage professional consultation, not replace it.
