import pandas as pd
import matplotlib.pyplot as plt
import DBQuery
from sktime.forecasting.base import ForecastingHorizon
from sktime.forecasting.model_selection import temporal_train_test_split
from sktime.forecasting.trend import PolynomialTrendForecaster

# Function pulls mortgage data from database using DB Query function
# data is transformed by taking the transaction data and summing each months transactions into a single data point, 
# this is done because time series forecasting needs fixed periods and the users transaction data may not fit that shcema
# using the new monthly data a cumulative running balance of the mortgage is then calculated
# variables are created for start and end dates as well as dates for forecasting, 
# this is done so that additions to the database do not require recoding the ML Algorithm
# A second dataframe is created that only reports the monthly sum of transactions to allow a multivariate regression to be used
# A dataframe of dates for the rergression is also created
# The train test split is created using a 60/40 split of the data
# the ForecastingHorizon, regression to be used are set
# predictions are calculated and passed into a dataframe for plotting
# plots are then generated:
# a scatter plot of the data showing what is used for testing and what is used for training the algorithm along with the plot of the algorithms predictions over that data 
# A stem plot showing the change in balance for each month of provided data
# a bar chart showing the predicted balance 10, 15 and 20 years into the future

df = DBQuery.getMortgageDatafromDB().drop(['Balance'],axis=1)
X = (df.groupby(pd.Grouper(key='Date', freq='M')).sum()).cumsum()
X = X.rename(columns = {"Amount": "Balance"})
X = X.to_period("M")

Xamt = (df.groupby(pd.Grouper(key='Date', freq='M')).sum())
Xamt = Xamt.to_period("M")
# print(Xamt)

start = X.index[0]
# print(start)
end = X.index[-1]
# print(end)
# print(type(end))
plus10 = (end.to_timestamp() + pd.Timedelta(weeks = 480)).round(freq='31D').to_period(freq='M')
# print(plus10)
# print(type(plus10))
plus15 = (end.to_timestamp() + pd.Timedelta(weeks = 780)).round(freq='31D').to_period(freq='M')
plus20 = (end.to_timestamp() + pd.Timedelta(weeks = 1040)).round(freq='31D').to_period(freq='M')
plus50 = (end.to_timestamp() + pd.Timedelta(weeks = 2600)).round(freq='31D').to_period(freq='M')


Xfut = pd.date_range(str(start), str(plus50), freq='M')
Xfut = Xfut.to_period("M")
# print("Xfut: \n",Xfut)

X_train, X_test, Xamt_train, Xamt_test = temporal_train_test_split(X, Xamt, test_size=.4)
# print("X_train:\n", X_train, "X_test:\n", X_test)

fhFut = ForecastingHorizon(Xfut, is_relative=False)

# forecaster = NaiveForecaster(strategy="drift")
forecaster = PolynomialTrendForecaster(degree=1)
forecaster.fit(X_train)
y_predData = forecaster.predict(X_test.index)
y_pred = forecaster.predict(fhFut)
y_predDf = pd.DataFrame(y_pred)
# print(y_predDf.to_string())
# print("y_pred: \n", y_predDf.loc[[str(plus10),str(plus15)]])
	
def mortgageplot():
	fig, (ax1, ax2, ax3) = plt.subplots(3)
	fig.suptitle('Mortgage Data')
	ax1.title.set_text("Mortgage Balance over time")
	ax1.scatter(X_train.index.astype("datetime64"), X_train['Balance'], label='training data')
	ax1.scatter(X_test.index.astype("datetime64"), X_test['Balance'], label='testing data')
	ax1.plot(y_predDf.loc[str(start):str(end)].index.astype("datetime64"), y_predDf.loc[str(start):str(end), 'Balance'], label='Prediction data')
	ax1.title.set_text("Mortgage Balance over time")
	ax1.legend(loc="upper left")
	ax1.tick_params(labelrotation=45)
	
	ax2.stem(Xamt.index.astype("datetime64").drop(['2022-09']), Xamt['Amount'].drop(['2022-09']))
	ax2.title.set_text("Amount of change in mortgage balance each month.")
	ax2.tick_params(labelrotation=45)

	ax3.title.set_text("Mortgage Balance 10, 15 and 20 years out")
	ax3.tick_params(labelrotation=45)
	ax3.bar(y_predDf.loc[[str(plus10), str(plus15), str(plus20)]].index.astype("datetime64"), y_predDf.loc[[str(plus10), str(plus15), str(plus20)], 'Balance'], width=30)
	plt.show()

