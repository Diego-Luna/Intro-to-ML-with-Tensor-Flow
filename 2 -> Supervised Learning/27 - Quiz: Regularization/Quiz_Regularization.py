# TODO: Add import statements
## Diego -> step 1
import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso

# Assign the data to predictor and outcome variables
# TODO: Load the data
#train_data = None
#X = None
#y = None
## Diego -> step 2
train_data = pd.read_csv('data.csv', header = None)
X = train_data.iloc[:,:-1]
y = train_data.iloc[:,-1]

# TODO: Create the linear regression model with lasso regularization.
#lasso_reg = None
## Diego -> step 3
lasso_reg = Lasso()

# TODO: Fit the model.
## Diego -> step 4
lasso_reg.fit(X, y)

# TODO: Retrieve and print out the coefficients from the regression model.
#reg_coef = None
#print(reg_coef)
## Diego -> step 5
reg_coef = lasso_reg.coef_
print(reg_coef)
