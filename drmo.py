# a = int(input("第一个数"))

# c = input("操作")

# b = int(input("第二个数"))


# if c.index=="+":
#     print(a+b)
# elif c.index=="_" :
#     print(a-b)
# elif c.index=="*" :
#     print(a*b)
# elif c.index=="/" :
#     print(a/b)

"""
highchengji = {}
lowchengji = {}
studentlist = ["张三","李四","李一","李为","李第三方","是否","收到","天天四","热"]
a =0
while a < len(studentlist):
    chengji = int(input("请输入"+studentlist[a]+"的成绩"))
    if chengji >=60 :
        highchengji[studentlist[a]] = chengji
    else :
        lowchengji[studentlist[a]] = chengji
    a = a+1
print(highchengji,lowchengji)
"""

""""
chengjigao = {}
chengjidi = {}
student = ["张三","李四","王五","丽丽"]
a = 0
while a < len(student) :
    chengji = int(input("请输入"+student[a]+"的成绩"))
    if chengji >60 :
        chengjigao[student[a]] =chengji
    else :
        chengjidi[student[a]] =chengji
    a = a+1
print(chengjigao,chengjidi)
    
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end="  ")
    print()
"""

"""
a=0
while a ==0:
        for i in range(5,0,-1):
            print("红灯还有"+str(i)+"秒")
        for i in range(2,0,-1):
            print("绿灯还有"+str(i)+"秒")
        for i in range(3,0,-1):
            print("黄灯还有"+str(i)+"秒")
        a=a+1





lists ={"红灯":5,"绿灯":4,"黄灯":3}
while True:
    for i in lists:
        for j in range(lists[i]):
            print(i,"还有",lists[i]-j,"秒")


"""
"""
username = input("请输入账号")
password = input("请输入账号")
if len(username) >=5 and  len(username) <=8 :
    if username[0] in "qwertyuiopasdfghjklzxcvbnm":
        if len(password) >=6 and  len(password) <=9 :
            print("注册成功","账号:",username,"密码:",password)
        else:
            print("密码长度必须在6-9位中间")
    else:
        print("首字母需要小写")
        
else:
    print("账号长度必须在5-8位中间")
"""



class Car():
    def __init__(self,pinpai,yanse,neishi):
        self.pingpai = pinpai
        self.yanse = yanse
        self.neishi = neishi
    def gongneg(self):
        print("飞行")
    def xingnneg(self):
        print("跑得快")
# qiche = Car("奥迪","红色","星空顶")
# qiche.gongneg()
# qiche.xingnneg()


class Tcar(Car):
    def gongneg(self):
        print("游泳")
dakache = Tcar("奔驰","蓝色","星空顶")
dakache.gongneg()