# Perform the following steps below:

## 1. Load in the data

- The data is in the file called 'data.csv'. Note that this data has a header line.
- Make sure that you've split out the data into the predictor feature in `X` and outcome feature in `y`.
- For `X`, make sure it is in a 2-d array of 20 rows by 1 column. You might need to use NumPy's `reshape` function to accomplish this.

## 2. Create polynomial features

- Create an instance of sklearn's `PolynomialFeatures` class and assign it to the variable `poly_feat`. Pay attention to how to set the degree of features, since that will be how the exercise is evaluated.
- Create the polynomial features by using the `PolynomialFeatures` object's `.fit_transform()` method. The "fit" side of the method considers how many features are needed in the output, and the "transform" side applies those considerations to the data provided to the method as an argument. Assign the new feature matrix to the `X_poly` variable.

## 3. Build a polynomial regression model

- Create a polynomial regression model by combining sklearn's `LinearRegression` class with the polynomial features. Assign the fit model to `poly_model`.
