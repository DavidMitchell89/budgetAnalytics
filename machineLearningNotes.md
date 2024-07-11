# SciKit Learn

Scikit learn API is always the same
  can put and algorithm as mod and use the same steps to get an output
  
  `from sklearn.datasets import Dataset`
  `dataset(return_X_y=True)` 
    makes dataset split into two arrays
      an array of X values, properties of the dataset
      an array of y values, the values resulting from those properties
  `X, y = dataset(return_X_y=True)`
    sets dataset values to X and y for model
  `from sklearn.neighbors import KNeighborsRegressor`
    imports K-nearest neighbor regression algorithm
  `import matplotlib.pylab as plt`
    imports graphical plots for data from matplotlib
  `mod = KNeighborsRegressor()`
    points algorithm to a model object
  `mod.fit(X, y)`
    learns from model as best as possible
  `pred = mod.predict(X)`
    sets predictions from the model to variable pred 
  `plt,scatter(pred, y)`
    generates scattes plot of data and their predicted values

   

# General flow of Machine Learning  
  data -> model -> prediction
  typically data must be split into two parts

        -> X - Properties from the dataset
  Data -
        -> Y - values resulting from the dataset

  Data can then be passed to Model using X to predict Y

  Model must be created from the data
    the Object in scikit learn
  Model then learns from the data
    the .fit(x,y) in scikit learn

  Model then applies a given algorithm to the data to make predictions for new values

  the size of the numbers in the data can affect the predictions
    one side of the data could have substantially larger numbers skewing the math in the algorithm
  model may need to be preprocessed before the model

        -> X -> Scale the values ->
  Data -                           -> Model -> Prediction
        -> Y ->

  The Scaling must become part of the model itself
                          Model
        -> X |                               |
  Data -     | Scale the values -> Algorithm | -> Predictions
        -> Y |-------------------------^     |  
    
  SciKit Learn includes an entire pipeline for handling the modeling and predictions together
    .fit(X, y)
    .pred(X)

  
  # Models

  k-nearest neighbors Alg
    for regression the output is the value of the object based on the average values the k neighbors
    for classification the output is the class membership of the object by a plurality vote of the k neighbors
    
  
