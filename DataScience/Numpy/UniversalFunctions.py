import numpy as np
from scipy import special

np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 /values[i]
    return output

values = np.random.randint(1, 10, size = 5)
print(values)
print(compute_reciprocals(values))

x = np.arange(9).reshape((3, 3))
print(x)
print(2 ** x)

print("========== Arithmetic of Array ==========", "\n")

x = np.arange(4)
print("x      =", x)
print("x + 5  =", x + 5)
print("numpy.add(x, 5) =", np.add(x, 5))
print("x - 5  =", x - 5)
print("numpy.subtract(x, 5) = ", np.subtract(x, 5))
print("x * 5  =", x * 5)
print("numpy.multiply(x, 5) = ", np.multiply(x, 5))
print("x / 2  =", x / 2)
print("numpy.divide(x, 2) = ", np.divide(x, 2))
print("x // 2 =", x // 2)
print("numpy.floor_divide(x, 2) = ", np.floor_divide(x, 2))
print("-x     =", -x)
print("numpy.negative(x) = ", np.negative(x))
print("x ** 2 =", x ** 2)
print("numpy.power(x, 2) = ", np.power(x, 2))
print("x % 2  =", x % 2)
print("numpy.mod(x, 2) = ", np.mod(x, 2))

x = np.array([-2, -1, 0, 1, 2])
print("abs(x) = ", abs(x))
print("numpy.abs(x) = ", np.abs(x))
print("numpy.absolute(x) = ", np.absolute(x))

x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
print("numpy.abs(x) = ", np.abs(x))
print("numpy.absolute(x) = ", np.absolute(x))

print("========== Trigonometric Function ==========")
theta = np.linspace(0, np.pi, 3)
print("theta      =", theta)
print("sin(theta) =", np.sin(theta))
print("cos(theta) =", np.cos(theta))
print("tan(theta) =", np.tan(theta))
x = [-1, 0, 1]
print("x          =", x)
print("arcsin(x)  =", np.arcsin(x))
print("arccos(x)  =", np.arccos(x))
print("arctan(x)  =", np.arctan(x))

print("========== Exponentail and Logarithmic ==========")
x = [1, 2, 3]
print("x      = ", x)
print("e^x    = ", np.exp(x))
print("2^x    = ", np.exp2(x))
print("3^x    = ", np.power(3, x))

x = [1, 2, 4, 10]
print("x        = ", x)
print("ln(x)    = ", np.log(x))
print("log2(x)  = ", np.log2(x))
print("log10(x) = ", np.log10(x))

x = [0, 0.001, 0.01, 0.1]
print("exp(x) - 1 = ", np.expm1(x))
print("log(1 + x) = ", np.log1p(x))

print("========== Gauassian function ==========")
x = [1, 5, 10]
print("gamma(x)    = ", special.gamma(x))
print("ln|gamma(x) = ", special.gammaln(x))
print("beta(x, 2)  = ", special.beta(x, 2))

x = np.array([0, 0.3, 0.7, 1.0])
print("erf(x)      = ", special.erf(x))
print("erfc(x)     = ", special.erfc(x))
print("erfinv(x)   = ", special.erfinv(x))

print("========== Setting Output ==========")
x = np.arange(5)
y = np.empty(5)
print("x =", x)
print("y =", y)
np.multiply(x, 10, out = y)
print("y = numpy.multiply(x, 10, out = y) =",np.multiply(x, 10, out = y))

y = np.zeros(10)
print("y =", y)
np.power(2, x, out = y[::2])
print("y = numpy.powewr(2, x, out = y[::2])", np.power(2, x, out = y[::2]))

print("========== Reduce and Accumalate ==========")
x = np.arange(1, 6)
print("x    = ", x)
print("numpy.add.reduce(x)          = ", np.add.reduce(x))
print("numpy.multiply.reduce(x)     = ", np.multiply.reduce(x))
print("numpy.add.accumulate(x)      = ", np.add.accumulate(x))
print("numpy.multiply.accumulate(x) = ", np.multiply.accumulate(x))

print("========== Outer ==========")
x = np.arange(1, 6)
print("x                          = ", x)
print("numpy.multiply.outer(x, x) = ", "\n" , np.multiply.outer(x, x))

print("========== Operator ==========")
x = np.array([1, 2, 3, 4, 5])
print("x < 3 =                              ", x < 3, "dtype = ", (x < 3).dtype)
print("numpy.less(x, 3) =                   ", np.less(x, 3), "dtype = ", np.less(x, 3).dtype)
print("x > 3 =                              ", x > 3, "dtype = ", (x > 3).dtype)
print("numpy.greater(x, 3) =                ", np.greater(x, 3), "dtype = ", np.greater(x, 3).dtype)
print("x <= 3 =                             ", x <= 3, "dtype = ", (x <= 3).dtype)
print("numpy.less_equal(x, 3) =             ", np.less_equal(x, 3), "dtype = ", np.less_equal(x, 3).dtype)
print("x >= 3 =                             ", x >= 3, "dtype = ", (x >= 3).dtype)
print("numpy.greater_equal(x, 3) =          ", np.greater_equal(x, 3), "dtype = ", np.greater_equal(x, 3).dtype)
print("x != 3 =                             ", x != 3, "dtype = ", (x != 3).dtype)
print("numpy.not_equal(x, 3) =              ", np.not_equal(x, 3), "dtype = ", np.not_equal(x, 3).dtype)
print("x == 3 =                             ", x == 3, "dtype = ", (x == 3).dtype)
print("numpy.equal(x, 3) =                  ", np.equal(x, 3),"dtype = ", np.equal(x, 3).dtype)
print("(x ** 2) == (2 **x) =                ", (x ** 2) == (2 ** x), "dtype = ", ((x ** 2) == (2 ** x)).dtype)
print("numpy.equal((x ** 2), (2 ** x)) =    ", np.equal((x ** 2), (2 ** x)), "dtype = ", np.equal((x ** 2), (2 ** x)).dtype)

rng = np.random.RandomState(0)
x = rng.randint(10, size = (3, 4))
print("x =                ", x)
print("x < 6 =            ", x < 6, "dtype = ", (x < 6).dtype)
print("numpy.less(x, 6) = ",np.less(x, 6), "dtype = ", np.less(x, 6).dtype)

print("numpy.count_nonzero(x < 6) = ", np.count_nonzero(x < 6))
print("numpy.sum(x < 6) =           ", np.sum(x < 6))   # True = 1; False = 0
print("numpy.sum(x < 6, axis = 1) = ", np.sum(x < 6, axis = 1))   #less six in each row
print("numpy.sum(x < 6 , axis = 0) =", np.sum(x < 6, axis = 0))   #less six in each column
