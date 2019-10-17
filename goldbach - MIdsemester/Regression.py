import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def linearRegression(data, MultiplesofWhat):
    print("Showing Scatter Plot and best Fit Line using Linear Regression ")
    MultiplesofWhat = MultiplesofWhat / 2
    X = data.iloc[:, 0].values.reshape(-1, 1)
    y = data.iloc[:, 1].values.reshape(-1, 1)
    X = [X[i] for i in range(len(X)) if i % MultiplesofWhat == 0]
    y = [y[i] for i in range(len(y)) if i % MultiplesofWhat == 0]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, y)
    y_pred = linear_regressor.predict(X)
    plt.scatter(X, y, color='blue')
    plt.plot(X, y_pred, color='red')
    plt.title('Data about Goldbach Conjecture')
    plt.xlabel('Even Integers')
    plt.ylabel('Number of pairs of prime numbers (i,j) such that i<j and i+j = x ')
    # plt.savefig('goldbach Statistical Results .pdf',format='pdf')
    # plt.savefig('Goldbach Statistical Results.png',dpi=1200)
    plt.show()
    return


def PolynomialRegression(data, n, Transparency, MultiplesofWhat):
    MultiplesofWhat = MultiplesofWhat / 2
    X = data.iloc[:, 0].values.reshape(-1, 1)
    y = data.iloc[:, 1].values.reshape(-1, 1)
    X = [X[i] for i in range(len(X)) if i % MultiplesofWhat == 0]
    y = [y[i] for i in range(len(y)) if i % MultiplesofWhat == 0]
    polynomial_regressor = PolynomialFeatures(degree=n)
    X_Poly = polynomial_regressor.fit_transform(X)
    polynomial_regressor = LinearRegression()
    polynomial_regressor.fit(X_Poly, y)

    plt.scatter(X, y, color='blue', alpha=Transparency,marker='.')



    plt.plot(X, polynomial_regressor.predict(X_Poly), color='red')
    plt.title('Data about Goldbach Conjecture')
    plt.xlabel('Multiples of ' + str(MultiplesofWhat * 2))
    plt.ylabel('Number of pairs of prime numbers (i,j) such that i<j and i+j = x ')
    # plt.savefig('Goldbach Statistical Results.png', dpi=900)
    #plt.savefig('Goldbach Statistics which are multiples of {0}.png'.format(MultiplesofWhat * 2), dpi=1200)
    plt.show()
    return


def PolynomialAnalysis(data, n, Transparency):
    X = data.iloc[:, 0].values.reshape(-1, 1)
    y = data.iloc[:, 1].values.reshape(-1, 1)
    polynomial_regressor = PolynomialFeatures(degree=n)
    X_Poly = polynomial_regressor.fit_transform(X)
    polynomial_regressor = LinearRegression()
    polynomial_regressor.fit(X_Poly, y)

    # plt.scatter(X,y,color = 'blue',alpha=Transparency,marker='.')
    X_4and6 = [X[i] for i in range(len(X)) if (i % 2 == 0 and i % 3 == 0)]
    y_4and6 = [y[i] for i in range(len(y)) if (i % 2 == 0 and i % 3 == 0)]
    plt.scatter(X_4and6, y_4and6, color='red', alpha=Transparency,marker='.')

    X_4 = [X[i] for i in range(len(X)) if (i % 2 == 0 and i % 3 != 0)]
    y_4 = [y[i] for i in range(len(y)) if (i % 2 == 0 and i % 3 != 0)]
    plt.scatter(X_4, y_4, color='green', alpha=Transparency,marker='.')

    X_6 = [X[i] for i in range(len(X)) if (i % 3 == 0 and i % 2 != 0)]
    y_6 = [y[i] for i in range(len(y)) if (i % 3 == 0 and i % 2 != 0)]
    plt.scatter(X_6, y_6, color='blue', alpha=Transparency,marker='.')

    # X_8= [X[i] for i in range(len(X)) if (i % 4 == 0 )]
    # y_8 = [y[i] for i in range(len(y)) if (i % 4 ==0)]
    # plt.scatter(X_8, y_8, color='orange', alpha=Transparency)

    plt.plot(X, polynomial_regressor.predict(X_Poly), color='black')
    plt.title('Data about Goldbach Conjecture with Degree of best fit polynomial = ' + str(n))
    plt.xlabel('Multiples of 4 in Green and 6 in Blue,Multiplies of 4 and 6 in Red ')
    plt.ylabel('Number of pairs of prime numbers (i,j) such that i<j and i+j = x ')
    plt.savefig('Goldbach Statistical Results with Multiples of 4 and 6 .png', dpi=1200)
    plt.show()
    return


dataset = pd.read_csv('Data.csv')

smalldataset = pd.read_csv('Smalldata.csv')

#for i in range(2,33,+2):
  #PolynomialRegression(dataset,3,0.05,i)

#linearRegression(dataset,1)
#PolynomialRegression(dataset,3,0.05,i)
PolynomialAnalysis(dataset, 3, 0.05)

