def lei (username,password):
    
    if len(username) >=5 and  len(username) <=8 :
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
            if len(password) >=6 and  len(password) <=9 :
                return True
            else:
                return("密码长度必须在6-9位中间")
        else:
            return("首字母需要小写")
        
    else:
        return("账号长度必须在5-8位中间")
a = lei("zhangsan","w")
print(a)
