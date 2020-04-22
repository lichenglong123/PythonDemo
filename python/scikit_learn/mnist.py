# -*- coding:utf-8 -*-
from sklearn import datasets
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
import numpy as np

#获取鸢尾花数据集
#iris = datasets.load_iris()
digits=datasets.load_digits()
x,y=digits.data,digits.target
some_digit=x[100]
some_digit_image=some_digit.reshape(8,8)
plt.imshow(some_digit_image,cmap=matplotlib.cm.binary,interpolation="nearest")
plt.axis("off")
plt.show()
# shuffle_index=np.random.permutation(1500)
# x_train,y_train=x[shuffle_index],y[shuffle_index]
#
# y_train_5=(y_train==5)
#
#
# sgd_clf=SGDClassifier(random_state=42)
#
# sgd_clf.fit(x_train,y_train_5)
#
#
#
# print(sgd_clf.predict([some_digit]))






