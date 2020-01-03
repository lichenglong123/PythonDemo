from sklearn.datasets import fetch_mldata
from sklearn.datasets import fetch_openml
from sklearn import datasets
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone
import numpy as np

mnlist=fetch_mldata('MNIST Original',data_home='./datasets')
x,y=mnlist.data,mnlist.target
some_digit=x[36100]
some_digit_image=some_digit.reshape(28,28)
plt.imshow(some_digit_image,cmap=matplotlib.cm.binary,interpolation="nearest")
plt.axis("off")
plt.show()

x_train,x_test,y_train,y_test=x[:60000],x[60000:],y[:60000],y[60000:]

shuffle_index=np.random.permutation(60000)
x_train,y_train=x_train[shuffle_index],y_train[shuffle_index]


y_train_5=(y_train==5)
y_test_5=(y_test==5)

sgd_clf=SGDClassifier(random_state=42)
sgd_clf.fit(x_train,y_train_5)


print(sgd_clf.predict([some_digit]))
