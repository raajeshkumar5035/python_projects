f1 = open('mydata.txt', 'r')
f2 = open(r'C:\Users\91955\Downloads\ansible_projects\my_file.txt', 'w')

for data in f1:
    f2.write(data)

f1.close()
f2.close()
