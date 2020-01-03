# -*- coding:utf-8 -*-
import numpy as np
def load_data_set():
    train_data = [[1.0, 2, 3], [1.0, 8, 1], [1.0, 7, 4], [
        1.0, 5, 6], [1.0, 4, 3], [1.0, 2, 9], [1.0, 1, 7]]
    train_label = [25, 41, 53, 55, 34, 58, 43]
    return train_data, train_label

if __name__ == '__main__':
    train_data,train_label=load_data_set()
    data_mat=np.matrix(train_data)
    lable_mat=np.matrix(train_label).transpose()
    n = np.shape(data_mat)[1]

    weights = np.ones((n, 1))
    print(data_mat)
    print(lable_mat)
    print(n)
    print(weights)









