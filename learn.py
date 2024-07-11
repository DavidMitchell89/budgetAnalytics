import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

iris = sns.load_dataset('iris')
iris = iris[['petal_length', 'petal_width']]
print(iris)

X = iris['petal_length']
y = iris['petal_width']

# plt.scatter(X, y)
# plt.xlabel("petal_length")
# plt.ylabel("petal_width")
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state= 23)

X_train = np.array(X_train).reshape(-1, 1)
X_Test = np.array(X_test).reshape(-1, 1)

lr = LinearRegression()
lr.fit(X_train, y_train)

c = lr.intercept_
print(c)

m = lr.coef_
print(m)

y_pred_train = m*X_train + c
print(y_pred_train.flatten())

y_pred_train1 = lr.predict(X_train)
print(y_pred_train1)

# plt.scatter(X_train, y_train)
# plt.plot(X_train, y_pred_train1, color = 'red')
# plt.xlabel("petal_length")
# plt.ylabel("petal_width")
# plt.show()

y_pred_test1 = lr.predict(X_test)
print(y_pred_test1)

plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred_test1, color = 'red')
plt.xlabel("petal_length")
plt.ylabel("petal_width")
plt.show()
