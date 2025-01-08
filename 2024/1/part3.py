FILENAME = "2024/1/note3.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readline()
print(len(INPUT))

all_trios = []
for i in range(0,len(INPUT),3):
    all_trios.append("".join([INPUT[i],INPUT[i+1],INPUT[i+2]]))

answer = 0
for p in all_trios:
    match p.count('x'):
        case 0:
            answer += 6
        case 1:
            answer += 2
    
    answer += p.count('B')+3*p.count('C')+5*p.count('D')
print(answer)
