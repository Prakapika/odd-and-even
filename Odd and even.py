num = (1,2,3,4,5,6,7,8,9)
odd = 0
even = 0
for i in num:
    if not i%2:
            even+=1
    else:
            odd+=1
print("Number of odd num:",odd)
print("Number of even num:",even)
