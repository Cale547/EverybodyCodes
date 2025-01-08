FILENAME = "2024/1/note1.txt"
with open(FILENAME, encoding="UTF8") as f:
    INPUT = f.readlines()
INPUT = INPUT[0]
print(INPUT)

answer = INPUT.count('B') + 3*INPUT.count('C')
print(answer)