from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained model
model_path = 'mymodel.pkl'  # Make sure this file exists and is a trained model
with open(model_path, 'rb') as file:
    model = pickle.load(file)
print("Loaded the model")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    try:
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        
        # Make prediction
        prediction = model.predict(final_features)
        iris_species = ["Setosa", "Versicolor", "Virginica"]
        output = iris_species[int(prediction[0])]
    except Exception as e:
        output = f"Error: {str(e)}"

    return render_template('index.html', prediction_text='Prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
