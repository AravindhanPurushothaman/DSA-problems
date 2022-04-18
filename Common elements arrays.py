A = [1,2,2,1]
B = [2,3,1,2]
n1 = len(A)
n2 = len(B)
hashmap_B = {}

for i in range(n2):
    if B[i] in hashmap_B:
        hashmap_B[B[i]]+=1
    else:
        hashmap_B[B[i]]=1
        
result = []

for i in range(n1):
    if A[i] in hashmap_B and hashmap_B[A[i]]>0:
        result.append(A[i])
        hashmap_B[A[i]] -=1

print (result)
