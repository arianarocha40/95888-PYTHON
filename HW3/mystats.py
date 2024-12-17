"""
@author: arian
Andrew ID: afrocha
Name: Ariana Rocha
Data Focused Python hw3.1 -- SECTION 2&3
"""

#SECTION 2: Variadic Functions
# File: mystats.py

import numpy as np #part 2d

# Defining the mean function here
# Old function from part (a)
def mean(*args):
    if len(args) == 0:
        raise ValueError("mean() needs at least one input to run")
    total_sum = sum(args)
    count = len(args)
    return total_sum/count
    print(total_sum/count)
    
#Improved Function is successful
def mean(*args):
    if len(args) == 0:
        raise ValueError("mean() needs at least one input to run")
    total_sum = 0
    count = 0    
    
    for arg in args:
        if is_iter(arg):
            total_sum += sum(arg)
            count += len(arg)
        else: 
            total_sum += arg
            count+= 1
    return total_sum / count

# Defining the stddev function here
def stddev(*args):
    if len(args) ==0:
        raise ValueError("mean() needs at least one input to run")
    all_values = []
    for arg in args:
        if is_iter(arg):
            all_values.extend(arg)
        else: 
            all_values.append(arg)
            
    n = len(all_values)
    if n < 2: 
        raise ValueError("stddev() requires at least two data points")
    mu = mean(*all_values)
    
    variance = sum((x-mu)** 2 for x in all_values) / (n-1)
    
    return variance ** 0.5

# Defining the median function here
def median(*args):
    if len(args) == 0 :
        raise ValueError("median() needs at least one input to run")
    all_values =[]
    for arg in args: 
        if is_iter(arg):
            all_values.extend(arg)
        else: 
            all_values.append(arg)
        
    all_values.sort()
    
    n = len(all_values)
    mid = n // 2
    
    if n == 1:
        return all_values[mid]
    else:
        return (all_values[mid-1] + all_values[mid]) / 2

# Defining the mode function here
def mode(*args):
    if len(args) == 0 :
        raise ValueError("median() needs at least one input to run")
    all_values =[]
    for arg in args:
        if is_iter(arg):
            all_values.extend(arg)
        else: 
            all_values.append(arg)
        
    frequency_dict = {}
    for value in all_values:
        if value in frequency_dict:
            frequency_dict[value] +=1
        else: 
            frequency_dict[value] = 1
    max_freq = max(frequency_dict.values())
    modes = [key for key, freq in frequency_dict.items() if freq == max_freq]
    return tuple(modes)

# part (c)
def is_iter(v):
    v_is_iter = True
    try:
        iter(v)
    except:
        v_is_iter = False
    return v_is_iter

#SECTION 3: MODULES
## part (b.) making sure its only executed when mystats is main module
if __name__ == "__main__":
    # part (a)
    print('The current module is:', __name__)
    #the output is 'The current module is: __main__' when mystats.py is the main module.
    
    # part (b) statements ran successfully
    print('mean(1) should be 1.0, and is:', mean(1))
    print('mean(1,2,3,4) should be 2.5, and is:',
                                        mean(1,2,3,4))
    print('mean(2.4,3.1) should be 2.75, and is:',
                                        mean(2.4,3.1))
    #print('mean() should FAIL:', mean()) # Successfully failed and am thus commenting out as instructed
    
    
    v1 = {1, 2, 3}     # a set is iterable
    print(v1, "is iterable:", is_iter(v1))
    v2 = 123
    print(v2, "is iterable:", is_iter(v2))
    
    print('mean([1,1,1,2]) should be 1.25, and is:',
                                   mean([1,1,1,2]))
    print('mean((1,), 2, 3, [4,6]) should be 3.2,' +
          'and is:', mean((1,), 2, 3, [4,6]))
    
    # part (d)
    print("Ten random draws from Norm(0,1):")
    for i in range(10):
        print("Draw", i, "from Norm(0,1):",
                            np.random.randn())
    ls50 = [np.random.randn() for _ in range(50)]
    print("\nMean of", len(ls50), "values from Norm(0,1):", mean(ls50))
    
    ls1000 = [np.random.randn() for _ in range(1000)]
    print("\nMean of", len(ls1000), "values from Norm(0,1):", mean(ls1000))
    
    # part (e)
    seed = 0
    np.random.seed(seed)
    a1 = np.random.randn(10)
    print("a1:",a1) 
    print("the mean of a1 is:", mean(a1)) 
    
    # part (f)
    print("the stddev of a1 is:", stddev(a1))
    
    # part (g)
    print("the median of a1 is:", median(a1))
    
    # part (h)
    print("mode(1, 2, (1, 3), 3, [1, 3, 4]) is:",
                mode(1, 2, (1, 3), 3, [1, 3, 4]))
    
