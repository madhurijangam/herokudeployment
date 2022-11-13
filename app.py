# Importing essential libraries and modules

import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading plant disease classification model





# Loading crop recommendation model




# =========================================================================================

# Custom functions for calculations







# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)
model=pickle.load(open("RandomForest.pkl", "rb"))
# render home page


@ app.route('/')
def home():
    title = 'Harvestify - Home'
    return render_template('index.html', title=title)

# render crop recommendation form page


@ app.route("/predict",methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    return render_template("index.html", prediction_text="The BEST CROP FITS  is {}".format(prediction))


# render fertilizer recommendation form page




# render disease prediction input page




# ===============================================================================================

# RENDER PREDICTION PAGES

# render crop recommendation result page




# render fertilizer recommendation result page




# render disease prediction result page





# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)


