# 發票對號
win = open("win.txt"). read(). split()
mine = open("mine.txt"). read(). split()
print(win)
print(mine)

cnt = 0
sum = 0
for i, num in enumerate(mine):
    if num in win:
        cnt = cnt + 1
        sum = cnt * 200
        print("第", i + 1, "張發票中獎", num, "!")
print("中獎發票共", cnt, "張")
print("中獎金額共", sum, "元")


# # 參考 "對中發票之總發票數" & "對中發票之總金額"
# # 對中發票之總發票數
# cnt = 0
# data = [1, 2, 23, 45, 56]
# for i, num in enumerate(data):
#     if num > 5:
#           cnt = cnt + 1
# print("中獎發票共", cnt, "張")
#
#
# # 對中發票之總金額
# sum = 0
# data = [1, 2, 23, 45, 56]
# for i, num in enumerate(data):
#     sum = sum + num
# print("中獎金額共", sum, "元")

