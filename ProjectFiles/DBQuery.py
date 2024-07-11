import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


#401K
#Mortgage
#Emergency Fund

# connects to local sqlite3 database and reads the database into a pandas dataframe. prints an error if sql query fails.
# finally closes sql connection after query is completed
def getMortgageDatafromDB():
    try:
        con = sqlite3.connect("db.sqlite")
        # print("connected to database")
        # cur = con.cursor()
        sqlQuery = "Select transactions.date AS Date, transactions.amount / 100.0 AS Amount, SUM(Amount/100.0) OVER (Order by Date) AS Balance FROM transactions INNER JOIN accounts ON accounts.id = transactions.acct WHERE accounts.name = 'Mortgage';"
        fmt ='%Y%m%d'
        mortgageDf = pd.read_sql_query(sqlQuery, con, parse_dates={'Date':fmt})
        # print(mortgageDf)

    except sqlite3.Error as error:
        print("Failed to execute the above query", error)

    finally:
        if con:

            con.close()

            # print("sqlite connection closed")

    return mortgageDf


def get401kDataFromDB():
    try:
        con = sqlite3.connect("db.sqlite")
        # print("connected to database")
        # cur = con.cursor()
        sqlQuery = "Select transactions.date AS Date, transactions.amount / 100.0 AS Amount, SUM(Amount/100.0) OVER (Order by Date) AS Balance FROM transactions INNER JOIN accounts ON accounts.id = transactions.acct WHERE accounts.name = '401K';"
        fmt ='%Y-%m-%d'
        retDf = pd.read_sql_query(sqlQuery, con, parse_dates={'Date':fmt})
        # print(retDf)

    except sqlite3.Error as error:
        print("Failed to execute the above query", error)

    finally:
        if con:

            con.close()

            # print("sqlite connection closed")

    return retDf


def getEmergencyFundDataFromDB():
    try:
        con = sqlite3.connect("db.sqlite")
        # print("connected to database")
        # cur = con.cursor()
        sqlQuery = "Select zero_budgets.month, categories.name, zero_budgets.amount From zero_budgets INNER JOIN categories ON categories.id = zero_budgets.category WHERE categories.name = 'Emergency Fund';"
        fmt ='%Y%m%d'
        emergencyDf = pd.read_sql_query(sqlQuery, con, parse_dates={'Date':fmt})
        # print(emergencyDf)

    except sqlite3.Error as error:
        print("Failed to execute the above query", error)

    finally:
        if con:

            con.close()

            # print("sqlite connection closed")

    return emergencyDf
    
getMortgageDatafromDB()
