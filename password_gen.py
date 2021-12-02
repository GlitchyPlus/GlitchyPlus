import random
def password_generator():
    the_pass_input = input("enter the password length,the max length is 44  ")
    digitlist =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3'
        ,'4','5','6','7','8','9',')','(','$','%',"{","}","[",']']
    shrinkedpass = []
    random.shuffle(digitlist)
    for i in range(0,int(the_pass_input)):
        shrinkedpass.append(digitlist[i])
    g ="".join(shrinkedpass)
    print(g)
password_generator()
