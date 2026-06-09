text=input()
k=int(input())
count={}

for i in range(len(text)-k+1):
    word = text[i:i+k]
    count[word] = count.get(word,0)+1
    
max_count=max(count.values())

for word in count:
    if count[word] == max_count:
        print(word)
        
