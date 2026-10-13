with open("student.txt","r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        line = line.split(",")
        print(line)