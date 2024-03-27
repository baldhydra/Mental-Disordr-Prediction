from flask import Flask, render_template, request
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model using joblib

model1 = joblib.load('model.joblib')



# Function to map user inputs to numerical values for symptoms
def map_symptoms(sadness, euphoric, exhausted, sleep_disorder):
    feature_mapping = {"most often": 4, "usually": 3, "sometimes": 2, "seldom": 1}
    mapped_sadness = feature_mapping.get(sadness, 0)  # Default to 0 if key not found
    mapped_euphoric = feature_mapping.get(euphoric, 0)
    mapped_exhausted = feature_mapping.get(exhausted, 0)
    mapped_sleep_disorder = feature_mapping.get(sleep_disorder, 0)
    return [mapped_sadness, mapped_euphoric, mapped_exhausted, mapped_sleep_disorder]

# Function to map user inputs to numerical values for yes/no features
def map_yes_no_features(mood_swings, suicidal_thoughts, anorexia, authority_respect, try_explain, aggressive_response, ignore_move_on, nervous_breakdown, admit_mistakes,overthinking):
    feature_mapping = {"yes": 1, "no": 0}
    mapped_features = [feature_mapping.get(feature, 0) for feature in [mood_swings, suicidal_thoughts, anorexia, authority_respect, try_explain, aggressive_response, ignore_move_on, nervous_breakdown, admit_mistakes,overthinking]]
    return mapped_features

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Symptoms form inputs
    sadness = request.form.get('sadness', '')
    euphoric = request.form.get('euphoric', '')
    exhausted = request.form.get('exhausted', '')
    sleep_disorder = request.form.get('sleep_disorder', '')

    # Yes/No features form inputs
    mood_swings = request.form.get('mood_swings', '')
    suicidal_thoughts = request.form.get('suicidal_thoughts', '')
    anorexia = request.form.get('anorexia', '')
    authority_respect = request.form.get('authority_respect', '')
    try_explain = request.form.get('try_explain', '')
    aggressive_response = request.form.get('aggressive_response', '')
    ignore_move_on = request.form.get('ignore_move_on', '')
    nervous_breakdown = request.form.get('nervous_breakdown', '')
    admit_mistakes = request.form.get('admit_mistakes', '')
    overthinking = request.form.get('overthinking', '')
    sexual_activity = int(request.form.get('sexual_activity', 0))
    concentration = int(request.form.get('concentration', 0))
    optimism = int(request.form.get('optimism', 0))

    # Create an array with sexual_activity, concentration, and optimism
    additional_array = np.array([sexual_activity, concentration, optimism]).reshape(1, -1)

    # Map user inputs to numerical values for symptoms
    mapped_symptoms = map_symptoms(sadness, euphoric, exhausted, sleep_disorder)

    # Map user inputs to numerical values for yes/no features
    mapped_features = map_yes_no_features(mood_swings, suicidal_thoughts, anorexia, authority_respect, try_explain, aggressive_response, ignore_move_on, nervous_breakdown, admit_mistakes,overthinking)

    # Convert to numpy arrays
    symptoms_array = np.array(mapped_symptoms).reshape(1, -1)
    features_array = np.array(mapped_features).reshape(1, -1)

    # Concatenate symptoms_array and features_array
    combined_array = np.concatenate((symptoms_array, features_array, additional_array), axis=1)
#     numbers = combined_array.strip("[]").split()

# # Convert the numbers to integers
#     numbers = [int(num) for num in numbers]

# # Convert the list to a string with commas
#     comma_separated = ','.join(map(str, numbers))

# # Convert the comma-separated string back to a list of integers
#     converted_list = [int(num) for num in comma_separated.split(',')]

#     combined_array=[converted_list]
    print(combined_array)
    nw_arr=[]
    for i in combined_array[0][:17]:
        nw_arr.append(int(i))

#     print(nw_arr)
#     nnw_arr=[nw_arr]
#     print(nnw_arr)
#     flist=['Sadness',
#  'Euphoric',
#  'Exhausted',
#  'Sleep dissorder',
#  'Mood Swing',
#  'Suicidal thoughts',
#  'Anorxia',
#  'Authority Respect',
#  'Try-Explanation',
#  'Aggressive Response',
#  'Ignore & Move-On',
#  'Nervous Break-down',
#  'Admit Mistakes',
#  'Overthinking',
#  'Sexual Activity',
#  'Concentration','Optimisim']
#     nn_l=pd.DataFrame(nnw_arr,columns=flist)
    # Make predictions
    prediction1 = model1.predict([nw_arr])
    
    #prediction_label = prediction_labels[prediction1[0]]  # Convert prediction to label

    # Return the predictions
    return render_template('result.html', prediction1=prediction1)

if __name__ == '__main__':
    app.run(debug=True)
