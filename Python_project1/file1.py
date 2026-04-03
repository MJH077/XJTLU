fr = open("jack3.txt", "r", encoding="UTF-8")
fw = open("jack3.txt.bak", "w", encoding="UTF-8")
for line in fr:
    line = line.strip()
    if line.split(" ")[1] == "测试":
        continue
    fw.write(line)
    fw.write("\n")
fr.close()
fw.close()
