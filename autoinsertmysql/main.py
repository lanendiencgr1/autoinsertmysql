import ast
import random
import re
import string
dict = {}
with open("loadziduan.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
with open("loadmain.txt", "r", encoding="utf-8") as file:
    lines1 = file.readlines()
#字段随机用dict
for line in lines:
    line=line.strip().replace(" ","")
    news=line.split("=")
    key=news[0]
    value=ast.literal_eval(news[1])
    dict[key]=value
# print(dict)
#主字段
main_name=lines1[0].strip()
#将字段和值封装成一个二维列表 table_init
table_init=[]
del lines1[0]
for line1 in lines1:
    line1list=line1.strip().replace(" : "," ").replace(" + "," ").split(" ")
    table_init.append(line1list)
sql="INSERT INTO"
#拼接字段括号
expand="("+table_init[0][0]
for i in range(1, len(table_init)):
    expand=expand + f", {table_init[i][0]}"
expand=expand+")"
#拼接值

def getsql(keynum=1):
    global values
    letters = string.ascii_lowercase + string.ascii_uppercase
    values = ""
    values = "('"
    for i in range(1, len(table_init[0])):
        if re.search(r'e_n', table_init[0][i]):
            if re.search(r'zf\(', table_init[0][i]):
                match = re.findall(r'\d+', table_init[0][i])
                values = values + str(keynum).zfill(int(match[0]))
                continue
                pass
            else:
                values = values + str(keynum)
                continue
                pass
        pass
        if re.search(r'space', table_init[0][i]):
            values = values + " "
            continue
            pass
        if re.search(r'r\(', table_init[0][i]):
            match = re.findall(r'\d+', table_init[0][i])
            number1 = int(match[0])
            number2 = int(match[1])
            if re.search(r'zf\(', table_init[0][i]):
                number3 = int(match[2])
                values = values + str(random.randint(number1, number2)).zfill(number3)
                continue
                pass
            else:
                values = values + str(random.randint(number1, number2))
                continue
                pass
        if re.search(r'RL\(', table_init[0][i]):
            match = re.findall(r'\d+', table_init[0][i])
            values = values + random.choice(letters) * int(match[0])
            continue
            pass
        if re.search(r'rl\(', table_init[0][i]):
            match = re.findall(r'\d+', table_init[0][i])
            for k in range(0, int(match[0])):
                values = values + random.choice(string.ascii_lowercase)
            continue
            pass

        if re.search(r'Rl\(', table_init[0][i]):
            match = re.findall(r'\d+', table_init[0][i])
            for k in range(0, int(match[0])):
                values = values + random.choice(letters)
            continue
            pass
        

        if table_init[0][i] not in dict:
            values = values + table_init[0][i]
            continue
        values = values + random.choice(dict[table_init[0][i]])
    values = values + "'"


    for i in range(1, len(table_init)):
        values=values+", '"
        for j in range(1, len(table_init[i])):
            if re.search(r'e_n',table_init[i][j]):
                if re.search(r'zf\(',table_init[i][j]):
                    match = re.findall(r'\d+', table_init[i][j])
                    values = values + str(keynum).zfill(int(match[0]))
                    continue
                    pass
                else:
                    values = values + str(keynum)
                    continue
                    pass
            pass
            if re.search(r'space',table_init[i][j]):
                values = values + " "
                continue
                pass
            if re.search(r'r\(', table_init[i][j]):
                match = re.findall(r'\d+', table_init[i][j])
                number1 = int(match[0])
                number2 = int(match[1])
                if re.search(r'zf\(', table_init[i][j]):
                    number3 = int(match[2])
                    values=values + str(random.randint(number1,number2)).zfill(number3)
                    continue
                    pass
                else:
                    values=values + str(random.randint(number1,number2))
                    continue
                    pass
            if re.search(r'RL\(',table_init[i][j]):
                match = re.findall(r'\d+', table_init[i][j])
                for k in range(0,int(match[0])):
                    values = values + random.choice(string.ascii_uppercase)
                continue
                pass
            
            if re.search(r'rl\(',table_init[i][j]):
                match = re.findall(r'\d+', table_init[i][j])
                for k in range(0,int(match[0])):
                    values = values + random.choice(string.ascii_lowercase)
                continue
                pass
            
            if re.search(r'Rl\(',table_init[i][j]):
                match = re.findall(r'\d+', table_init[i][j])
                for k in range(0,int(match[0])):
                    values = values + random.choice(letters)
                continue
                pass
            
            if table_init[i][j] not in dict:
                values = values + table_init[i][j]
                continue

            values = values + random.choice(dict[table_init[i][j]])
        values=values+"'"
    values=values+")"
    #总拼接
    res=sql+ " "+main_name+" "+expand+" VALUES "+values
    # print(values)
    # print(res)
    return res

# for i in range(99):
#     autos=getsql(i)
#     with open("automysql.txt","a",encoding="utf-8") as f:
#         f.write(autos+"\n")
#         f.flush()
#     print(autos)
#     pass
