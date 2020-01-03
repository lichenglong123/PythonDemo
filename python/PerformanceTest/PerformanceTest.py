#!/usr/bin/python
from sklearn.datasets import fetch_mldata
from sklearn.model_selection import StratifiedKFold
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix

class PerformanceTest:
    def test(self):
        mnlist=fetch_mldata('MNIST Original',data_home='./datasets')
        x,y=mnlist.data,mnlist.target
        x_train,x_test,y_train,y_test=x[:60000],x[60000:],y[:60000],y[60000:]
        shuffle_index=np.random.permutation(60000)
        x_train,y_train=x_train[shuffle_index],y_train[shuffle_index]
        y_train_5=(y_train==5)
        y_test_5=(y_test==5)
        sgd_clf=SGDClassifier(random_state=42)
        sgd_clf.fit(x_train,y_train_5)
        skfold=StratifiedKFold(n_splits=5,random_state=42)

       # cross=cross_val_score(sgd_clf,x_train,y_train_5,cv=5,scoring="accuracy")

        y_train_pred=cross_val_predict(sgd_clf,x_train,y_train_5,cv=3)

        mat=confusion_matrix(y_train_5,)
        print(mat)

        print(y_train_pred)



if __name__ == '__main__':
     test=PerformanceTest()
     test.test()