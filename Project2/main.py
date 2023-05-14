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
filename = "airlines_delay.csv"
data = pd.read_csv(os.path.join(current_dir, filename))
#data = pd.read_csv("airlines_delay.csv")
#data = pd.read_csv("iris-data.csv")

# train and test svm model
data_manip.train_model(data, model_map[ModelType.svm][0], model_map[ModelType.svm][1])
model_test.test_model(model_map[ModelType.svm][1])

# train and test logical regression model
data_manip.train_model(data, model_map[ModelType.randforest][0], model_map[ModelType.randforest][1])
model_test.test_model(model_map[ModelType.randforest][1])

# train and test gradient booster regressor model
data_manip.train_model(data, model_map[ModelType.graboo][0], model_map[ModelType.graboo][1])
model_test.test_model(model_map[ModelType.graboo][1])

# train and test MLPRegressor model
data_manip.train_model(data, model_map[ModelType.MLPR][0], model_map[ModelType.MLPR][1])
model_test.test_model(model_map[ModelType.MLPR][1])


