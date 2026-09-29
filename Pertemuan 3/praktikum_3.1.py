bilangan1 = 1
bilangan2 = 0
# print(bilangan1/bilangan2)
# print("<End Program>")
if bilangan2 != 0:
    print(bilangan1/bilangan2)
else: 
    print("Operasi matematika ini tidak dapat dijalankan")
print("<<End Program>>")

my_list = []
idx = 0
# print(my_list[idx])
# print("<<End Program>>")
if (idx>-1 & idx<len(my_list)):
    print(my_list[idx])
else:
    print("Operasi tidak dapat dijalankan")
print("<<End Program>>")

#try except
bilangan1 = 1
bilangan2 = 0
try:
    print(bilangan1/bilangan2)
except:
    print("Operasi matematika ini tidak dapat dijalankan")
print("<<End Program>>")
my_list = [9]
idx = 0
try:
    print(my_list[idx])
except:
    print("Operasi tidak dapat dijalankan")
print("<<End Program>>")