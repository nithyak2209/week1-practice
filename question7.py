#Remove Consecutive Values

values=[1,1,2,3,3,4,5,5,5,6]
result=[]
for i in range(len(values)-1):
    if values[i]==values[i+1]:
        continue
    else:
        result.append(values[i])
result.append(values[-1])
print(result)