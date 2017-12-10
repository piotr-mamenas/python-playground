import numpy as np

a = np.array([1,2]);
b = np.array([2,1]);

dot = 0;

#
# Manual
for e, f in zip(a,b):
    dot += e*f;
	
print("Vanilla: " + str(dot));

#
# Manual Numpy
dot = np.sum(a*b)

print("Manual Numpy: " + str(dot));

#
# Numpy Inbuilt
dot = a.dot(b);

print("Numpy Inbuilt: " + str(dot));