# Decision Trees in sklearn

n this section, you'll use decision trees to fit a given sample dataset.

Before you do that, let's go over the tools required to build this model.

For your decision tree model, you'll be using scikit-learn's [Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) class. This class provides the functions to define and fit the model to your data.

## Hyperparameters

When we define the model, we can specify the hyperparameters. In practice, the most common ones are

- `max_depth`: The maximum number of levels in the tree.
- `min_samples_leaf`: The minimum number of samples allowed in a leaf.
- `min_samples_split`: The minimum number of samples required to split an internal node.

For example, here we define a model where the maximum depth of the trees `max_depth` is 7, and the minimum number of elements in each leaf `min_samples_leaf` is 10.

```
> > > model = DecisionTreeClassifier(max_depth = 7, min_samples_leaf = 10)
```

## You'll need to complete each of the following steps:

1. Build a decision tree model

Create a decision tree classification model using scikit-learn's `DecisionTreeClassifier` and assign it to the variable `model`.

2. Fit the model to the data

You won't need to specify any of the hyperparameters, since the default ones will yield a model that perfectly classifies the training data. However, we encourage you to play with hyperparameters such as max_depth and min_samples_leaf to try to find the simplest possible model.

3. Predict using the model

Predict the labels for the training set, and assign this list to the variable y_pred.

4. Calculate the accuracy of the model

For this, use the function sklearn function accuracy_score. A model's accuracy is the fraction of all data points that it correctly classified.
