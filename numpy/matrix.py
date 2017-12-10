import numpy as np;

#
matrix_a = np.array([ [1,2,3,4], [3,4,1,2], [6,9,3,2], [3,8,1,2] ]);
matrix_b = np.array([ [1,4,5,6], [6,2,5,7], [1,0,2,5], [1,0,9,1] ]);

print(matrix_a);
print(matrix_a[0,0]);

#
zero_matrix = np.zeros((10,10));

print(zero_matrix);

#
ones_matrix = np.ones((10,10));

print(ones_matrix);

#
random_matrix = np.random.random((10,10));

print(random_matrix);

#
gaussian_matrix = np.random.randn(10,10);

print(gaussian_matrix);
print(gaussian_matrix.mean());
print(gaussian_matrix.var());

#
inverted_matrix = np.linalg.inv(matrix_a);
print(inverted_matrix);
print(inverted_matrix.dot(matrix_a));
print(matrix_a.dot(inverted_matrix));

#
solve_a = np.linalg.inv(matrix_a).dot(matrix_b);
solve_b = np.linalg.solve(matrix_a,matrix_b);

print(solve_a);
print(solve_b);