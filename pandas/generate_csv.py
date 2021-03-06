import numpy as np;
import sys;

def create_dataset(filename,entries,cols):
    file = open(filename,'w');
    
    for t in range(entries):
        random_numbers = np.random.random(cols);
        line = ",".join(str(e) for e in random_numbers);
        file.write(line + '\n');
        
    file.close();
    return;
     
create_dataset(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]));