pk=[2,3,5,7,11,13]

form = []
for i in range (6):
    for j in range(5):
        form.append(pk[0] ** i * pk[1] ** j)
        for z in range(4):
            form.append(pk[0] ** i * pk[1] ** j * pk[2] ** z)
            for k in range(3):
                form.append(pk[0] ** i * pk[1] ** j * pk[2] ** z * pk[3] ** k)
                for u in range(3):
                    form.append(pk[0] ** i * pk[1] ** j * pk[2] ** z * pk[3]** k * pk[4]**u)
form.sort()
print(form)





#2100. Свадебный обед
# import re
# n = input("kol gostei ")
# n = 4
# prise = 200
# name_g = []
# #name_g = ['lol','bol','obo','on one']
# for i in range(int(n)):
#     name_g.append(input())
#     if re.search('one',str(name_g[i])) != None:
#         prise += 100
#     prise +=100
#
# if prise == 1300:
#     prise+=100
#
# print(prise)
