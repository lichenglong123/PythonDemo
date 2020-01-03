#!/usr/bin/python
from sklearn.linear_model import LinearRegression
import numpy as np

def linearReg():
    x=2 * np.random.rand(100,1)
    y=4+3*x+np.random.rand(100,1)
    lin_reg=LinearRegression()
    lin_reg.fit(x,y)
   # print(lin_reg.intercept_)
   # print(lin_reg.coef_)
    x_new=np.array([[0],[2]])
    newValue=lin_reg.predict(x_new)
    print(newValue)

def tdxj():
    eta=0.1
    n_iterations=1000
    m=100
    x=2 * np.random.rand(100,1)
    y=4+3*x+np.random.rand(100,1)
    arr=np.ones((100,1))
    x_b=np.c_[arr,x]
    theta=np.random.randn(2,1)
    for iteration in range(n_iterations):
        gradients=2/m * x_b.T.dot(x_b.dot(theta)-y)
        theta=theta-eta*gradients



    print(theta)





tdxj()
#linearReg()

