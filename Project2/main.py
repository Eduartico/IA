import data_manip
import model_test
import warnings
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from enum import Enum
from sklearn.preprocessing import LabelEncoder
import os

class ModelType(Enum):
    svm = 1
    randforest = 2
    graboo = 3
    MLPR = 4

# Set the warning filter to "ignore"
warnings.filterwarnings("ignore", category=UserWarning)

model_map = {
    ModelType.svm: (SVR(), 'svm.sav'),
    ModelType.randforest: (RandomForestRegressor(), 'RandForest.sav'),
    ModelType.graboo: (GradientBoostingRegressor(), 'gradientbooster.sav'),
    ModelType.MLPR: (MLPRegressor(), 'MLPRegressor.sav'),
}

current_dir = os.path.dirname(os.path.abspath(__file__))
filename = "airlines_delay_original.csv"
data = pd.read_csv(os.path.join(current_dir, filename))
data_encoded = data.copy()

# Combine "AirportFrom" and "AirportTo" columns to create a unified set of airports
airports = pd.concat([data_encoded['AirportFrom'], data_encoded['AirportTo']])

# Perform label encoding on the combined set of airports
label_encoder_airports = LabelEncoder()
encoded_airports = label_encoder_airports.fit_transform(airports)

# Perform label encoding on the "Airline" column
label_encoder_airline = LabelEncoder()
data_encoded['Airline'] = label_encoder_airline.fit_transform(data_encoded['Airline'])

# Update "AirportFrom" and "AirportTo" columns with the encoded values
data_encoded['AirportFrom'] = encoded_airports[:len(data_encoded)]
data_encoded['AirportTo'] = encoded_airports[len(data_encoded):]

# Remove the "Flight" column
data_encoded = data_encoded.drop('Flight', axis=1)

# Save the encoded data to a CSV file
data_encoded.to_csv('airlines_delay_encoded.csv', index=False)

# train and test svm model
data_manip.train_model(data_encoded, model_map[ModelType.svm][0], model_map[ModelType.svm][1])
model_test.test_model(model_map[ModelType.svm][1])

# train and test logical regression model
data_manip.train_model(data_encoded, model_map[ModelType.randforest][0], model_map[ModelType.randforest][1])
model_test.test_model(model_map[ModelType.randforest][1])

# train and test gradient booster regressor model
data_manip.train_model(data_encoded, model_map[ModelType.graboo][0], model_map[ModelType.graboo][1])
model_test.test_model(model_map[ModelType.graboo][1])

# train and test MLPRegressor model
data_manip.train_model(data_encoded, model_map[ModelType.MLPR][0], model_map[ModelType.MLPR][1])
model_test.test_model(model_map[ModelType.MLPR][1])