#2023-11-29 wnw,The codes only applies to Monolayer to bilayer 2H-MX2,and thanks for the help of Xiao-Huan,Lv.
# before begin,you must prepare the POSCAR of Monolayer 2H MX2 (M=Mo,X=S,Se2:)


import numpy as np
# 读取文件 POSCAR
with open("POSCAR", "r") as f:
    lines = f.readlines()
d = float(input("请输入 M-M 间距,(建议6.1 Ang)："))
#原子数*2
lines[6] = " ".join([str(int(float(x) * 2)) for x in lines[6].split()]) + "\n"

# 复制第10行到最后一行 V2(x,y)=Te1(x,y); V2(z)= V1(z)+d/C d是V-V c轴间距
last_line = lines[9]
last_line = last_line.split()
last_line[2] = str(float(lines[8].split()[2]) + d / float(lines[4].split()[2]))
last_line = " ".join(last_line) + "\n"
lines.append(last_line)
# 复制第9行到最后一行 Te3(x,y)=V1(x,y); T3(z)=T1(z)+d/C
last_line = lines[8]
last_line = last_line.split()
last_line[2] = str(float(lines[9].split()[2]) + d / float(lines[4].split()[2]))
last_line = " ".join(last_line) + "\n"
lines.append(last_line)
# 复制第9行到最后一行 Te4(x,y)=V1(x,y)  T4(z)=T1(z)+d/c
last_line = lines[8]
last_line = last_line.split()
last_line[2] = str(float(lines[10].split()[2]) + d / float(lines[4].split()[2]))
last_line = " ".join(last_line) + "\n"
lines.append(last_line)
#将V2放第二行 11,12交换 10,11交换
lines[10], lines[11] = lines[11], lines[10]
lines[10], lines[9] = lines[9], lines[10]


# 写入新文件
with open("POSCAR_Rev", "w") as f:
    for line in lines:
        f.write(line)
