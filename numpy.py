# Ques: What is Numpy?
# Ans: NumPy is the fundamental packege for scientific computing in Python. It is a Python library that provides a multidimenstional
#     data types

# 1. Numpy Arrays have a fixed size at creation,unlike Python lists(which can grow dynamically). Changing the size of an ndarray will create 
# a new Array and delte the original one.

# 2. Same data type and thus will be same size in memory.

# 3. Numpy arrays facilliate advanced mathematical and other types of operations on large numbers of data. Typically,such operations
#     are executed more effficiently and with less code than is possible using python built in sequences.

import numpy as np

# Array initialization
a = np.array([1,2,3,4])


np.zeroes((3,4))    
output: -> array([[0.,0.,0.,0.],
                  [0.,0.,0.,0.],
                  [0.,0.,0.,0.]
                  ])

np.zeroes((3,4))    
output: -> array([[1.,1.,1.,1.],
                  [1.,1.,1.,1.],
                  [1.,1.,1.,1.]
                  ])

np.random.random((3,4)) -> give random no. same array as like above have 

np.linspace(-10,10,10)  -> fixed length generate krega from starting range to end range 

array.ndim -> in 3d array (a,b,c) return krta hai jisme a-> kitne 2D Array hai , b -> kitne row , c-> kitne column 

array.itemsize()    

array.resshape()

array.dtype -> data type btata hai -> int32 , int64, float64

array.astype(np.int32)    -> convert kr diya hai dusre data type mai.

array+2 -> ye sab mai add hoga

# Sigmoid  -> 
def sigmoid(array):
    return 1/(1+np.exp(-(array)))

example: -> a = np.arrayrange(100)  -> ye array ki range hai kha tak chalega array
            sigmoid(a)



# Notes of Numpy


import numpy as np

# From lists
arr = np.array([1, 2, 3])
arr2d = np.array([[1,2],[3,4]])

# Special arrays
np.zeros((3,4))          # 3x4 zeros
np.ones((2,3))           # 2x3 ones
np.full((2,2), 7)        # 2x2 filled with 7
np.eye(5)                # Identity 5x5
np.empty((2,2))          # uninitialized

# Ranges
np.arange(0, 10, 2)      # [0,2,4,6,8]
np.linspace(0, 1, 5)     # [0, 0.25, 0.5, 0.75, 1]
np.logspace(0, 2, 5)     # log spaced

# Random arrays
np.random.rand(3,2)      # uniform [0,1)
np.random.randn(3,2)     # standard normal
np.random.randint(0,10, size=(3,3))
np.random.random((2,2))

# Repetition
np.tile([1,2], 3)        # [1,2,1,2,1,2]
np.repeat([1,2], 3)      # [1,1,1,2,2,2]


arr = np.array([[1,2,3],[4,5,6]])

arr.shape       # (2,3)
arr.size        # 6
arr.ndim        # 2
arr.dtype       # int64
arr.nbytes      # total bytes
arr.itemsize    # bytes per element
arr.T           # transpose

arr = np.array([10,20,30,40,50])
arr[1:4:2]          # [20,40]
arr[::-1]           # reverse

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[0,2]          # 3
arr2d[:2, 1:]       # [[2,3],[5,6]]
arr2d[1, :]         # row 1

# Boolean indexing
arr = np.array([1,2,3,4])
mask = arr > 2
arr[mask]           # [3,4]
arr[arr % 2 == 0]   # [2,4]

# Fancy indexing
arr[[0,2,3]]        # [1,3,4]
arr2d[[0,1], [1,2]] # [2,6] (0,1) and (1,2)


arr = np.arange(12)

# Reshape
arr.reshape(3,4)
arr.reshape(-1, 4)   # auto compute rows

# Flatten
arr.flatten()        # returns copy
arr.ravel()          # returns view (faster)

# Stacking
a = np.array([1,2])
b = np.array([3,4])
np.vstack((a,b))     # [[1,2],[3,4]]
np.hstack((a,b))     # [1,2,3,4]
np.column_stack((a,b))
np.stack((a,b), axis=1)

# Split
arr = np.arange(10)
np.split(arr, [3,7])  # [0-2],[3-6],[7-9]
np.vsplit(mat, 3)
np.hsplit(mat, 2)

a = np.array([1,2,3])
b = np.array([4,5,6])

# Element-wise
a + b
a - b
a * b
a / b
a ** 2
np.sqrt(a)
np.exp(a)
np.log(a)
np.sin(a)

# Matrix multiplication
np.dot(a,b)          # scalar
a @ b                # Python 3.5+
np.matmul(a,b)

# Aggregate functions
np.sum(a)            # or a.sum()
np.mean(a)
np.median(a)
np.std(a)
np.var(a)
np.min(a), np.max(a)
np.argmin(a), np.argmax(a)
np.cumsum(a)         # cumulative sum
np.cumprod(a)

# Axis-wise
arr2d.sum(axis=0)    # column sums
arr2d.mean(axis=1)   # row means


# Broadcasting rules
arr = np.array([[1,2,3],[4,5,6]])
arr + 10               # add scalar
arr + [100,200,300]    # add row vector
arr + [[10],[20]]      # add column vector

# Vectorized condition
np.where(arr > 3, 1, 0)
np.select([arr<3, arr>5], [0,2], default=1)

from numpy.linalg import *

mat = np.array([[1,2],[3,4]])
inv(mat)               # inverse
det(mat)               # determinant
eig(mat)               # eigenvalues/vectors
svd(mat)               # singular value decomposition
qr(mat)                # QR decomposition
solve(mat, [5,6])      # solve linear system
norm(mat)              # Frobenius norm
matrix_rank(mat)


a = np.array([1,2,3,4])
b = np.array([3,4,5,6])

np.intersect1d(a,b)    # [3,4]
np.union1d(a,b)        # [1,2,3,4,5,6]
np.setdiff1d(a,b)      # [1,2]
np.setxor1d(a,b)       # [1,2,5,6]
np.unique(arr)         # unique values
np.in1d(a, b)          # [False,False,True,True]

arr = np.array([3,1,2,5,4])
np.sort(arr)           # returns sorted copy
arr.sort()             # in-place
np.argsort(arr)        # indices that sort: [1,2,0,4,3]

# Search
np.where(arr == 2)     # (array([2]),)
np.searchsorted([1,3,5], 4)  # insert position: 2
np.argpartition(arr, 3)      # indices for k smallest

# Clip values
np.clip(arr, 2, 4)

# Rounding
np.round(arr, 2)
np.floor(arr)
np.ceil(arr)

# Gradient (differences)
np.gradient(arr)
np.diff(arr)           # [2,1,2,1]

# Meshgrid
x = np.linspace(0,1,3)
y = np.linspace(0,1,3)
X,Y = np.meshgrid(x,y)

# Einsum (powerful)
a = np.array([[1,2],[3,4]])
np.einsum('ij,jk', a, a)   # matrix multiply
np.einsum('ii', a)         # trace

# Rolling window
def rolling_window(a, window):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

# Memory efficient copy/view
arr.view()   # changes reflect in original
arr.copy()   # independent copy


# Binary
np.save('arr.npy', arr)
np.load('arr.npy')
np.savez('archive.npz', a=arr1, b=arr2)
np.savez_compressed('compressed.npz', a=arr1)

# Text
np.savetxt('file.csv', arr, delimiter=',')
np.loadtxt('file.csv', delimiter=',')
np.genfromtxt('file.csv', delimiter=',', missing_values='NA')


# Binary
np.save('arr.npy', arr)
np.load('arr.npy')
np.savez('archive.npz', a=arr1, b=arr2)
np.savez_compressed('compressed.npz', a=arr1)

# Text
np.savetxt('file.csv', arr, delimiter=',')
np.loadtxt('file.csv', delimiter=',')
np.genfromtxt('file.csv', delimiter=',', missing_values='NA')



# Use views instead of copies
arr[::2, ::2]           # view

# Pre-allocate arrays
result = np.empty(1000000)
for i in range(1000000):
    result[i] = i*2    # faster than appending

# Vectorize custom functions
def my_func(x):
    return x**2 + 3*x + 1
vec_func = np.vectorize(my_func)

# Use boolean indexing instead of loops
arr[arr < 0] = 0       # faster than loop

# Use einsum for complex sums
np.einsum('ij->i', arr)   # row sums







# NumPy methods that are most commonly used in Machine Learning


# Normalization / Standardization
X = (X - X.mean(axis=0)) / X.std(axis=0)  # Standardization (Z-score)

# Min-Max scaling
X_scaled = (X - X.min()) / (X.max() - X.min())

# Train-test split manually
indices = np.random.permutation(len(X))
train_idx, test_idx = indices[:80], indices[80:]
X_train, X_test = X[train_idx], X[test_idx]

# Handle missing values
X[np.isnan(X)] = np.nanmean(X)  # Replace NaN with column mean

# One-hot encoding
labels = np.array([0, 1, 2, 1])
one_hot = np.eye(3)[labels]  # 3 classes → 4x3 matrix

# Polynomial features (simple version)
def add_poly_features(X, degree=2):
    return np.column_stack([X**i for i in range(1, degree+1)])

# Binning / Discretization
bins = np.linspace(0, 10, 5)
digitized = np.digitize(data, bins)


# Linear Regression
# y = X @ w + b
predictions = X @ w + b
loss = np.mean((predictions - y) ** 2)
gradient = (2/len(X)) * X.T @ (predictions - y)

# Logistic Regression
z = X @ w + b
predictions = 1 / (1 + np.exp(-z))  # Sigmoid
cross_entropy = -np.mean(y * np.log(predictions) + (1-y) * np.log(1-predictions))

# Gradient Descent
w = w - learning_rate * gradient

# Softmax (Multi-class)
exp_logits = np.exp(logits)
softmax = exp_logits / np.sum(exp_logits, axis=1, keepdims=True)


# Accuracy
accuracy = np.mean(predictions == y_true)

# Confusion Matrix
def confusion_matrix(y_true, y_pred, n_classes):
    cm = np.zeros((n_classes, n_classes), dtype=int)
    for t, p in zip(y_true, y_pred):
        cm[t, p] += 1
    return cm

# Precision, Recall, F1
TP = np.diag(cm)
FP = cm.sum(axis=0) - TP
FN = cm.sum(axis=1) - TP
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * (precision * recall) / (precision + recall)

# R2 Score
ss_res = np.sum((y_true - y_pred) ** 2)
ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
r2 = 1 - (ss_res / ss_tot)

# PCA from scratch
def pca(X, n_components):
    # Center data
    X_centered = X - np.mean(X, axis=0)
    # Covariance matrix
    cov_matrix = np.cov(X_centered.T)
    # Eigen decomposition
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    # Sort by eigenvalues
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]
    # Select top components
    components = eigenvectors[:, :n_components]
    # Project data
    return X_centered @ components


# Activation functions
def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)

# Derivatives (for backprop)
def d_relu(x):
    return (x > 0).astype(float)

def d_sigmoid(x):
    sig = sigmoid(x)
    return sig * (1 - sig)

# Xavier/Glorot initialization
def xavier_init(n_in, n_out):
    limit = np.sqrt(6 / (n_in + n_out))
    return np.random.uniform(-limit, limit, (n_in, n_out))

# He initialization (for ReLU)
def he_init(n_in, n_out):
    return np.random.randn(n_in, n_out) * np.sqrt(2 / n_in)


# L2 regularization (Ridge)
loss = mse + lambda_reg * np.sum(w ** 2)

# L1 regularization (Lasso)
loss = mse + lambda_reg * np.sum(np.abs(w))

# Dropout (during training)
mask = np.random.binomial(1, keep_prob, size=X.shape) / keep_prob
X_dropped = X * mask

# Early stopping (track best loss)
best_loss = np.inf
patience_counter = 0
if val_loss < best_loss:
    best_loss = val_loss
    patience_counter = 0
else:
    patience_counter += 1
    if patience_counter >= patience:
        break


# Euclidean distance
distances = np.sqrt(np.sum((X_train - X_test[i]) ** 2, axis=1))

# Cosine similarity
cosine_sim = (X @ Y) / (np.linalg.norm(X) * np.linalg.norm(Y))

# Manhattan distance
manhattan = np.sum(np.abs(X_train - X_test[i]), axis=1)

# Pairwise distance matrix
def pairwise_distances(X):
    n = len(X)
    dist = np.zeros((n, n))
    for i in range(n):
        dist[i] = np.sqrt(np.sum((X - X[i]) ** 2, axis=1))
    return dist

# Faster with broadcasting
dist = np.sqrt(((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2).sum(axis=-1))



def kfold_indices(X, k=5):
    indices = np.random.permutation(len(X))
    fold_sizes = np.full(k, len(X) // k, dtype=int)
    fold_sizes[:len(X) % k] += 1
    current = 0
    folds = []
    for size in fold_sizes:
        start, stop = current, current + size
        folds.append(indices[start:stop])
        current = stop
    return folds

# Get train/val indices for fold i
val_idx = folds[i]
train_idx = np.hstack(folds[:i] + folds[i+1:])


def batch_generator(X, y, batch_size=32):
    n_samples = len(X)
    indices = np.random.permutation(n_samples)
    for start in range(0, n_samples, batch_size):
        end = min(start + batch_size, n_samples)
        batch_idx = indices[start:end]
        yield X[batch_idx], y[batch_idx]

# Usage
for X_batch, y_batch in batch_generator(X_train, y_train, 64):
    predictions = X_batch @ w + b
    loss = np.mean((predictions - y_batch) ** 2)
    # Update weights...




# Slow (Python loop)
for i in range(1000):
    loss += (y_pred[i] - y[i]) ** 2

# Fast (vectorized)
loss = np.sum((y_pred - y) ** 2)

#  Memory inefficient
X_new = np.hstack([X, X**2, X**3])  # Creates copies

#  Memory efficient (view if possible)
# Use column_stack or careful reshaping

#  Not numerically stable
softmax = np.exp(logits) / np.sum(np.exp(logits))

# Numerically stable
logits_shifted = logits - np.max(logits, axis=1, keepdims=True)
softmax = np.exp(logits_shifted) / np.sum(np.exp(logits_shifted), axis=1, keepdims=True)