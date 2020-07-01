from collections import Counter 
  
ini_list = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 
               5, 5, 5, 4, 4, 4, 4, 4, 4] 

A = ['iit', 'iit', 'iit', 'jee', 'srm', 'jee']
  
# printing initial ini_list 
print ("initial list", str(ini_list)) 
print ("initial list", str(A)) 
  
# sorting on bais of frequency of elements 
result = sorted(ini_list, key = ini_list.count, 
                                reverse = True) 
result_m = sorted(A, key = A.count, 
                                reverse = True) 
  
# printing final result 
print("final list", str(result)) 
print("final list",str(result_m))
print(result_m)

result = list(dict.fromkeys(result_m))
print(result)