
n = int(input("文档总共有几面:"))
k = int(input("文档排版几页一面:"))
odd_list = []
eda_list = []

change = 0
flag = 1
for i in range(1, n + 1):
    if change == 0:
        flag = flag ^ 1
        change = change+1
    if flag == 0:
        odd_list.append(i)
    else:
        eda_list.append(i)
    change = (change + 1) % (k+1)

print(odd_list)
print(eda_list)
