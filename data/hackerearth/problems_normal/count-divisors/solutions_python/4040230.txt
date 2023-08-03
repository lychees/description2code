int_array = []
count = 0
int_array = map(int,raw_input().split())
if len(int_array) == 3:
    for i in range(int_array[0], (int_array[1]+1)):        
        if (i%int_array[2])== 0:
            count = count + 1

print count           
    
        
