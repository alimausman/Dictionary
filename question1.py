# Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
d3={}
for key in d1:
    if key in d2:
        d3[key]=d2[key]+d1[key]
    else:
        d3[key]= d1[key] 
    for k in d2:
        if k not in d1:
            d3[k]= d2[k]    
print(d3)                  
