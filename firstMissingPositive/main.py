
def firstMissingPositive(nums):#Our original array 
  
    m = max(nums) #Store max number in Array
    if m < 1: 
          
      #If all numbers in array are negative,just return 1 
        return 1 
    if len(nums) == 1: 
          
        #In case it contains one element 
        return 2 if nums[0] == 1 else 1     
    l = [0] * m 
    for i in range(len(nums)): 
        if nums[i] > 0: 
            if l[nums[i] - 1] != 1: 
                  
                #Changing the value at list index
                l[nums[i] - 1] = 1 
    for i in range(len(l)): 
          
  #Encountering first 0, i.e, the element with least value 
        if l[i] == 0:  
            return i+1
      #In case all values are filled between 1 and the max 
    return i+2 


print(firstMissingPositive([0,1,2]))