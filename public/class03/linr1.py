# linr1.py

# Demo:
# python linr1.py

# This script should do linear regression.
import numpy as np
# I should create some simple observations to learn from:
x_a = np.array([[1.1,1.1],[2.2,2.2]])
y_a = np.array([1.1,2.2])

# I should import linear_model:
from sklearn import linear_model
linr_model = linear_model.LinearRegression()
# I should call fit() to create the model:
linr_model.fit(x_a, y_a)

# I should make 2 predictions:

yhat = linr_model.predict([[3,3],[4,4]])
print('The predictions for ')
print('yhat = linr_model.predict([[3,3],[4,4]])')
print('are:')
print(yhat)

# should wrap linr_model with Keras:
# ref:
# https://keras.io/scikit-learn-api/

# You can use Sequential Keras models (single-input only) as
# part of your Scikit-Learn workflow via
# the wrappers found at keras.wrappers.scikit_learn.py.

# keras.wrappers.scikit_learn.KerasRegressor(build_fn=None, **sk_params)
# implements the Scikit-Learn regressor interface.

# build_fn: callable function or class instance
# sk_params: model parameters & fitting parameters

# build_fn should construct, compile and return a Keras model,
# which will then be used to fit/predict.

# sk_params takes model parameters 

# sk_params could also accept parameters for calling fit, predict, predict_proba

# google:
# example of keras.wrappers.scikit_learn.KerasRegressor

import keras

'bye'
