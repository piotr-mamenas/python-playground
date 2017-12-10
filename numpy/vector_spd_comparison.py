import numpy as np;
from datetime import datetime;

rand_norm_distribution_list_a = np.random.randn(100);
random_norm_distribution_list_b = np.random.randn(100);
T = 100000

def slow_dot_product(a,b):
    result = 0;
    for e, f in zip(a,b):
        result += e*f
    return result
	
start_time = datetime.now()
for t in range(T):
    slow_dot_product(rand_norm_distribution_list_a,random_norm_distribution_list_b)
end_time_a = datetime.now() - start_time;

start_time = datetime.now()
for t in range(T):
    rand_norm_distribution_list_a.dot(random_norm_distribution_list_b)
end_time_b = datetime.now() - start_time;

print("stdlib time / numpy time: " + str(end_time_a.total_seconds() / end_time_b.total_seconds()));