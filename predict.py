import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def price_prediction(power, kms, year, owner):
    bike = pd.read_csv("bike.csv")

    X = bike.drop("price", axis=1)
    y = bike["price"]

    X_test = np.array([power, kms, year, owner])
    X_test = X_test.reshape((1,-1))
    
    model = RandomForestRegressor()
    model.fit(X, y)
    
    return model.predict(X_test)