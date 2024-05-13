import sys

print(sys.getrefcount(1921))  # 3
getre_val_1 = 1921
print(sys.getrefcount(1921))  # 4
getre_val_2 = getre_val_1
print(sys.getrefcount(1921))  # 5
getre_val_3 = [1921, 1922, 1923]
print(sys.getrefcount(1921))  # 6

getre_val_3[0] = 1924
print(sys.getrefcount(1921))  # 5
del getre_val_1  # 执行del getre_val_1语句后从当前名称空间中删除getre_val_1
print(sys.getrefcount(1921))  # 4
getre_val_2 = 1924
print(sys.getrefcount(1921))
