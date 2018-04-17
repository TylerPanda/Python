import numpy as np

np.random.seed(0)    #指定一個種子值確保每次執行均產生同樣的亂術內容

x1 = np.random.randint(10, size = 6)
x2 = np.random.randint(10, size = (3, 4))
x3 = np.random.randint(10, size = (3, 4 ,5))

print("======一維陣列======")
print(x1, "\n")
print("x1 ndim:", x1.ndim)
print("x1 shape:", x1.shape)
print("x1 size:", x1.size)
print("x1 dtype:", x1.dtype)
print("x1 itemsize:", x1.itemsize)
print("x1 nbytes:", x1.nbytes, "\n")
print("======二維陣列======")
print(x2, "\n")
print("x2 ndim:", x2.ndim)
print("x2 shape:", x2.shape)
print("x2 size:", x2.size)
print("x2 dtype:", x2.dtype)
print("x2 itemsize:", x2.itemsize)
print("x2 nbytes:", x2.nbytes, "\n")
print("======三維陣列======")
print(x3, "\n")
print("x3 ndim:", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size:", x3.size)
print("x3 dtype:", x3.dtype)
print("x3 itemsize:", x3.itemsize)
print("x3 nbytes:", x3.nbytes, "\n")

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y]))
z = np.array([99, 99, 99])
print(np.concatenate([x, y, z]))

grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(np.concatenate([grid, grid]))
print(np.concatenate([grid, grid], axis = 1))
print(np.vstack([z, grid]))
