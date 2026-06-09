word = input()
complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
result = ""

for i in word:
    result += complement[i]
    
print(result[::-1])
