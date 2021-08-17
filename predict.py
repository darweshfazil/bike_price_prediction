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

        if(brand=="BMW"):
            BMW = 1
        elif(brand=="Bajaj"):
            Bajaj = 1
        elif(brand=="Benelli"):
            Benelli = 1
        elif(brand=="Ducati"):
            Ducati = 1
        elif(brand=="HarleyDavidson"):
            HarleyDavidson = 1
        elif(brand=="Hero"):
            Hero = 1
        elif(brand=="Honda"):
            Honda = 1
        elif(brand=="Hyosung"):
            Hyosung = 1
        elif(brand=="Ideal"):
            Ideal = 1
        elif(brand=="Indian"):
            Indian = 1
        elif(brand=="Jawa"):
            Jawa = 1
        elif(brand=="KTM"):
            KTM = 1
        elif(brand=="Kawasaki"):
            Kawasaki = 1
        elif(brand=="LML"):
            LML = 1
        elif(brand=="MV"):
            MV = 1
        elif(brand=="Mahindra"):
            Mahindra = 1
        elif(brand=="Rajdoot"):
            Rajdoot = 1
        elif(brand=="RoyalEnfield"):
            RoyalEnfield = 1
        elif(brand=="Suzuki"):
            Suzuki = 1
        elif(brand=="TVS"):
            TVS = 1
        elif(brand=="Triumph"):
            Triumph = 1
        elif(brand=="Yamaha"):
            Yamaha = 1
        elif(brand=="Yezdi"):
            Yezdi = 1

def price_prediction(brand, power, kms, year, owner):
    bike = pd.read_csv("bikes.csv")

    X = bike.drop("price", axis=1)
    y = bike["price"]

    value(brand)
    print(TVS)
    X_test = np.array([kms, owner, year, power, BMW, Bajaj, Benelli, Ducati, HarleyDavidson, Hero, Honda, Hyosung, Ideal, Indian, Jawa, KTM, Kawasaki, LML, MV, Mahindra, Rajdoot, RoyalEnfield, Suzuki, TVS, Triumph, Yamaha, Yezdi])
    X_test = X_test.reshape((1,-1))
    
    model = RandomForestRegressor()
    model.fit(X, y)
    
    return model.predict(X_test)