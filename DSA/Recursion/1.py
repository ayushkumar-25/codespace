# def openRussianDoll(doll):
#     if doll == 1:
#         print("All dolls are opened")
#     else:
#         print(doll)
#         openRussianDoll(doll - 1)
        

# openRussianDoll(10)

#print(~-5)

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
#order = "ayush"
print(*sorted(input("Enter : "), key=order.index), sep='')