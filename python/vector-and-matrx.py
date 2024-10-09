#Linear/Vector algebra tools. NumPy tools.
import math
def vector_add(v,w):
    return [v_i + w_i
            for v_i,w_i in zip(v,w)]

def vector_subtraction(v,w):
    return[v_i - w_i
           for v_i,w_i in zip(v,w)]

'''
component wise sum of list of all vectors
create anew vector whose first element is the sum of all the first elements, whose second element is the sum of all the second elements, and so on
'''
def vector_sum(vectors):
    result = vectors[0];
    for vector in vectors[1:]:
        result = vector_add(result,vector)
    return result

a = [1,
     2,
     3,
     4,
     5]

b = [10,
     20,
     30,
     40,
     50]

c = [100,
     200,
     300,
     400,
     500]

print(vector_add(a,b))
# [11, 22, 33, 44, 55]
print(vector_sum([a,b,c]))
# [111, 222, 333, 444, 555]

def scalar_multiply(c,v):
    return [c* v_i
            for v_i in v]

# vector mean of same sized vectors
def mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

print(mean([a,b,c]))
# [37.0, 74.0, 111.0, 148.0, 185.0]

def dot(v,w):
    return sum(v_i * w_i
               for v_i,w_i in zip(v,w))

print(dot(a,b))
# 550

def sum_of_square(v):
    return dot(v,v)

print(sum_of_square(b))
#5500

def magnitude(v):
    return math.sqrt(sum_of_square(v))

print(magnitude(b))
# 74.16198487095663

def distance(v,w):
    return magnitude(vector_subtraction(v,w))

print(distance(a,b))

# Matirx = list of vectors

a = [[1,2,3],
     [4,5,6]]

b = [[1,2],
     [3,4],
     [5,6]]

def shape(a):
    num_rows = len(a)
    num_cols = len(a[0]) if a else 0
    return num_rows, num_cols

print(shape(a))
# (2,3)
print(shape(b))
# (3,2)

def get_row(a,i):
    return a[i]

def get_col(a,j):
    return [a_i[j] for a_i in a]

print(get_row(a,1))
# [4, 5, 6]

print(get_col(a,2))
# [3, 6]

def make_matrix (num_rows, num_cols,entry_func):
    return[[entry_func(i,j)
           for i in range(num_rows)]
           for j in range(num_cols)]

def is_diaginal(i,j):
    return 1 if i == j else 0

identity_matrix = make_matrix(5,5,is_diaginal)

print(identity_matrix)
# [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]