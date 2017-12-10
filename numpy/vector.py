import numpy as np;

# Product
vector_a = np.array([1,2]);
vector_b = np.array([2,1]);

dot_product = vector_a.dot(vector_b);

print("Dot: " + str(dot_product));

# Magnitude
vector_magnitude = np.sqrt((vector_a*vector_a).sum());

print("Vector Magnitude: " + str(vector_magnitude));

vector_magnitude = np.linalg.norm(vector_a);

print("Vector Magnitude: " + str(vector_magnitude));