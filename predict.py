import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def value(brand):
        global BMW = 0
        global Bajaj = 0
        global Benelli = 0
        global Ducati = 0
        global Harley-Davidson = 0
        global Hero = 0
        global Honda = 0
        global Hyosung = 0
        global Ideal = 0
        global Indian = 0
        global Jawa = 0
        global KTM = 0
        global Kawasaki = 0
        global LML = 0
        global MV = 0
        global Mahindra = 0
        global Rajdoot = 0
        global Royal Enfield = 0
        global Suzuki = 0
        global TVS = 0
        global Triumph = 0
        global Yamaha = 0
        global Yezdi = 0

        brand = 1

def price_prediction(brand, power, kms, year, owner):
    bike = pd.read_csv("bikes.csv")

    X = bike.drop("price", axis=1)
    y = bike["price"]

    value(brand)
    X_test = np.array([kms, owner, year, power, BMW, Bajaj, Benelli, Ducati, Harley-Davidson, Hero, Honda, Hyosung, Ideal, Indian, Jawa, KTM, Kawasaki, LML, MV, Mahindra, Rajdoot, Royal Enfield, Suzuki, TVS, Triumph, Yamaha, Yezdi])
    X_test = X_test.reshape((1,-1))
    
    model = RandomForestRegressor()
    model.fit(X, y)
    
    return model.predict(X_test)