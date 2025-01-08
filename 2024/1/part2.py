FILENAME = "2024/1/note2.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readline()
print(len(INPUT))

all_pairs = []
for i in range(0,len(INPUT),2):
    all_pairs.append("".join([INPUT[i],INPUT[i+1]]))
print(all_pairs)

answer = 0
for p in all_pairs:
    if p.count('x') == 0:
        answer += 2
    
    answer += p.count('B')+3*p.count('C')+5*p.count('D')
print(answer)
