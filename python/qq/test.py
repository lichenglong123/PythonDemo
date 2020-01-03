import numpy as np
import matplotlib.pyplot as plt
x=2 * np.random.rand(100,1)
y=4+3*x+np.random.rand(100,1)
arr=np.ones((100,1))
x_b=np.c_[arr,x]

theta_best=np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)

x_new=np.array([[0],[2]])
x_new_b=np.c_[np.ones((2,1)),x_new]

y_predict=x_new_b.dot(theta_best)

plt.plot(x_new,y_predict,"r-")
plt.plot(x,y,"b.")
plt.axis([0,2,0,15])
plt.show()








