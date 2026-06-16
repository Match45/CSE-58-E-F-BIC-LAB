pattern = input().strip()
text = input().strip()
d = int(input())
positions=[]

for i in range(len(text)-len(pattern)+1):
    mismatch=0
    
    for j in range(len(pattern)):
        if pattern[j] != text[i+j]:
            mismatch+=1
            
        if mismatch>d:
            break
        
    if mismatch<=d:
        positions.append(str(i))
        
print(" ".join(positions))
