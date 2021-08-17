import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def value(brand):
        global BMW
        BMW = 0
        global Bajaj
        Bajaj = 0
        global Benelli
        Benelli = 0
        global Ducati
        Ducati = 0
        global HarleyDavidson
        HarleyDavidson = 0
        global Hero
        Hero = 0
        global Honda
        Honda = 0
        global Hyosung
        Hyosung = 0
        global Ideal 
        Ideal = 0
        global Indian 
        Indian = 0
        global Jawa
        Jawa = 0
        global KTM
        KTM = 0
        global Kawasaki
        Kawasaki = 0
        global LML 
        LML = 0
        global MV
        MV = 0
        global Mahindra 
        Mahindra = 0
        global Rajdoot 
        Rajdoot = 0
        global RoyalEnfield
        RoyalEnfield = 0
        global Suzuki
        Suzuki = 0
        global TVS
        TVS = 0
        global Triumph 
        Triumph = 0
        global Yamaha
        Yamaha = 0
        global Yezdi 
        Yezdi = 0

        brand = 1

def price_prediction(brand, power, kms, year, owner):
    bike = pd.read_csv("bikes.csv")

    X = bike.drop("price", axis=1)
    y = bike["price"]

    value(brand)
    X_test = np.array([kms, owner, year, power, BMW, Bajaj, Benelli, Ducati, HarleyDavidson, Hero, Honda, Hyosung, Ideal, Indian, Jawa, KTM, Kawasaki, LML, MV, Mahindra, Rajdoot, RoyalEnfield, Suzuki, TVS, Triumph, Yamaha, Yezdi])
    X_test = X_test.reshape((1,-1))
    
    model = RandomForestRegressor()
    model.fit(X, y)
    
    return model.predict(X_test)