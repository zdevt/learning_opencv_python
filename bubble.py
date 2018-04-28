

ar = [ 1,8,2,6,3,9,4]

for i in range(len(ar)):
    for j in range(i+1):
        if ( ar[i] < ar[j]):
            ar[i],ar[j] = ar[j],ar[i]

print( ar)
