nums = [2,4,5,2,9,15,7,8]
target = 15

p = int(len(nums))

print(p)
i = 1
for i in range(0,p):
    g = nums[i] + nums[i+1] 
    if g == target:
        print('Required condition met. ')
   # return [i, i+1]
    else:
        print('Conditon does not satisfy')
    
    if (i+2) <= p:
        i = i+2
    else:
        break
        
        
    
    




