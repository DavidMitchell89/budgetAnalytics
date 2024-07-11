# David Mitchell
# Student ID: 00273705
# C964 Capstone program

import sys

from sktime.performance_metrics.forecasting import mean_absolute_percentage_error
import DBQuery
import regression

def userInterface():
    print("Budget Predictions V1.\n",
          "This Program is the first iteration of a suite of tools used to make predictions based on the data contained in your budget.\n",
          "In the regression and prediction menu you can view the data used, search the prediction data, as well as a metric used to judge the quality of the predictions.",
          "The system can also generate some visualizations of the data to help understand and use the information presented here.")
    print(
        "Please Make a selection:\n",
        "    1. Regression and predictions.\n",
        "    2. View Plotted data.(This will open a popup window with graphs)\n",
        "    3. Exit.\n",
        sep=""
    )
    selection = input()
    try:
        int(selection)
    except ValueError:
        print("Please enter a valid number.\n")
        userInterface()
    if selection == "1":
        regandPredMenu()
    elif selection == "2":
        regression.mortgageplot()
        userInterface()
    elif selection == "3":
        sys.exit()

def regandPredMenu():
    print("\nThis Menu can be used to search the predictions made by the system, and to view the quality of the regression used.\n", 
          "Note: that the quality of the predictions depends, in part, on the amount of data available.\n"
          "    1. View data used from budget.\n",
          "    2. Search a prediction.\n",
          "    3. View Prediction Sample.\n",
          "    4. View Regression analytics.\n",
          "    5. Main menu.\n",
          "    6. Exit.\n",
          sep=""
    )
    selection = input()
    try:
        int(selection)
    except ValueError:
        print("Please enter a valid number.\n")
        userInterface()
    if selection == "1":
        print(DBQuery.getMortgageDatafromDB())
    elif selection == "2":
        regressionSearch()
    elif selection == "3":
        print(regression.y_predDf)
    elif selection == "4":
        print("The mean absolute percentage error is " + str((mean_absolute_percentage_error(regression.X_test, regression.y_predData)*100))+"\n",
              "This Metric measures the percentage difference between the actual data and the number calculated by the system. A lower number is indicative of a more accurate forecast.\n")
        regandPredMenu()
    elif selection == "5":
        userInterface()
    elif selection == "6":
        sys.exit()

def plotMenu():
    print(
        "    1. 401K.\n",
        "    2. Back.\n"
        "    3. Main Menu.\n",
        sep=""
    )
    selection = input()
    try:
        int(selection)
    except ValueError:
        print("Please enter a valid number.\n")
        userInterface()
    if selection == "1":
        DBQuery.getMortgageDatafromDB()
        regression.mortgagePlot()
        plotMenu()
    elif selection == "2":
        regandPredMenu()
    elif selection == "3":
        userInterface()

def regressionSearch():
    print("To search for a prediction please enter a date in the format 'YYYY-MM'.\n",
          "The available dates are between ",regression.y_pred.index[0], "and", regression.y_pred.index[-1], ".\n",
          "Please Select a date within the given range.\n"
          )
    selection=input()
    print(regression.y_pred.loc[[str(selection)]])
    regandPredMenu()

userInterface()
