import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def softmax_improvement(a):
    c = np.max(a)
    exp_a = np.exp( a-c )
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y


a = np.array([1010, 1000, 990])
print(softmax(a))
print(softmax_improvement(a))
