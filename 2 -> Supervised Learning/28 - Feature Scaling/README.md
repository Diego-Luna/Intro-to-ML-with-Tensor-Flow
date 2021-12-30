# Feature Scaling 🤟

What is feature scaling? Feature scaling is a way of transforming your data into a common range of values. There are two common scalings:

- Standardizing
- Normalizing

## Standardizing

Standardizing is completed by taking each value of your column, subtracting the mean of the column, and then dividing by the standard deviation of the column. In Python, let's say you have a column in `df` called `height`. You could create a standardized height as:

```python
df["height_standard"] = (df["height"] - df["height"].mean()) / df["height"].std()
```

## Normalizing

A second type of feature scaling that is very popular is known as normalizing. With normalizing, data are scaled between 0 and 1. Using the same example as above, we could perform normalizing in Python in the following way:

```python
df["height_normal"] = (df["height"] - df["height"].min()) /     \
                      (df["height"].max() - df['height'].min())

```

## Perform the following steps:

1. Load in the data

- The data is in the file called 'data.csv'. Note that there's no header row on this file.
- Split the data so that the six predictor features (first six columns) are stored in `X`, and the outcome feature (last column) is stored in `y`.

2. (NEW) Perform feature scaling on data via standardization

- Create an instance of sklearn's `StandardScaler` and assign it to the variable `scaler`.
- Compute the scaling parameters by using the `.fit_transform()` method on the predictor feature array, which also returns the predictor variables in their standardized values. Store those standardized values in `X_scaled`.

3. Fit data using linear regression with Lasso regularization

- Create an instance of sklearn's `Lasso`: (url)[https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#examples-using-sklearn-linear-model-lasso] class and assign it to the variable `lasso_reg`. You don't need to set any parameter values: use the default values for the quiz.
- Use the `Lasso` object's `.fit()` method to fit the regression model onto the data. Make sure that you apply the fit to the standardized data from the previous step (`X_scaled`), not the original data.

4. Inspect the coefficients of the regression model

- Obtain the coefficients of the fit regression model using the `.coef_` attribute of the `Lasso` object. Store this in the `reg_coef` variable: the coefficients will be printed out, and you will use your observations to answer the question at the bottom of the page.
