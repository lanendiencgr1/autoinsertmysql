from pymysql import Connection
import main
code=0
def load_connection_info(file_path):
    connection_info = {}
    with open(file_path, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            connection_info[key] = value
    return connection_info
file_path = "connection_info.txt"
# 从文件中读取连接信息
connection_info = load_connection_info(file_path)
print(connection_info)
conn = None
def connet():
# 使用读取到的连接信息进行连接
    try:
        global conn
        global code
        conn = Connection(
            host=connection_info["host"],
            port=int(connection_info["port"]),
            user=connection_info["user"],
            password=connection_info["password"],
            autocommit=bool(connection_info["autocommit"])
        )
        code=1
        return True
    except Exception as e:
        code=-1
        return False

if connet():
    dbselect = str(connection_info["choice_database"]).strip('"')
    cursor = conn.cursor()
    try:
        conn.select_db(dbselect)
        # res=main.getsql(60)
        # cursor.execute(res)
        code=2
        # conn.close()
    except Exception as e:
        code=-2
        # conn.close()
#插入
def insert(xuanze=0,keynum=1,xunhuan=1,xuanhuan1=1,con=None):
    jisuan=0
    cnt=0
    cntyes=0
    cntno=0
    res=None
    try :
        if keynum==1:
            for i in range(xunhuan,xuanhuan1):
                jisuan+=1
                res = main.getsql(i)
                if xuanze==1:
                    try:
                        cons=con.cursor()
                        cons.execute(res)
                        cnt+=1
                        cntyes+=1
                        with open("txtt/success.txt","a",encoding="utf-8") as f:
                            f.write(str(cntyes)+"."+str(res)+"\n")
                    except Exception as e:
                        cntno+=1
                        with open("txtt/failu.txt","a",encoding="utf-8") as f:
                            f.write(str(cntno)+".语句:"+str(res)+"错误:"+str(e)+"\n")
                        pass
                if xuanze==2:
                    with open("automysql.txt","a",encoding="utf-8") as f:
                        f.write(res+"\n")
                if xuanze==3:
                    try:
                        cons = con.cursor()
                        cons.execute(res)
                        cnt += 1
                        cntyes+=1
                        with open("txtt/success.txt", "a", encoding="utf-8") as f:
                            f.write(str(cntyes) + "." + str(res) + "\n")
                    except Exception as e:
                        cntno+=1
                        with open("txtt/failu.txt", "a", encoding="utf-8") as f:
                            f.write(str(cntno) + ".语句:" + str(res) + "错误:" + str(e) + "\n")
                        pass
                    with open("automysql.txt","a",encoding="utf-8") as f:
                        f.write(res+"\n")
        return cnt

        pass
    except Exception as e:
        print("失败")
        print(e)


# try :
#     res=main.getsql(2)
#     print(res)
#     print(conn)
#     cons=conn.cursor()
#     print(cons)
#     cons.execute(res)
#     print("成功")
#     pass
# except Exception as e:
#     print("失败")
#     print(e)

def connclose():
    conn.close()

# for i in range(1,5):
#     insert(i)

#执行语句 插入知乎要conn.commit()
# cursor.execute("select * from client")
# results=cursor.fetchall()
# for r in results:
#     print(r)

