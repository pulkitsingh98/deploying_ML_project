import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def model_prediction(l):
    customers = pd.read_csv('Ecommerce Customers')

    X = customers[['Avg. Session Length', 'Time on App',
        'Time on Website', 'Length of Membership']]
    y = customers['Yearly Amount Spent']

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state = 101)

    from sklearn.linear_model import LinearRegression

    lm = LinearRegression()
    lm.fit(X_train,y_train)

    # X_test = np.array([sl,toa,tow,lom])
    X_test = np.array(l,dtype='float64')
    X_test = X_test.reshape((1,-1))

    

    return lm.predict(X_test)[0]

