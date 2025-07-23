monterhp = 500
monterw1 = 10
monterw2 = 20
monterw3 = 30
tuehp = 1000
tuew1 = 50
tuew2 = 75
tuew3 = 100
print(f"เจอ monter มีhp{monterhp} พลังโจมตีของอาวุธที่1คือ{monterw1} พลังโจมตีของอาวุธที่2คือ{monterw2} พลังโจมตีของอาวุธที่3คือ{monterw3}")
print(f"tue มีhp{tuehp} พลังโจมตีของอาวุธที่1คือ{tuew1} พลังโจมตีของอาวุธที่2คือ{tuew2} พลังโจมตีของอาวุธที่3คือ{tuew3}")
x = int(input("ต่อสู้มอนกด1 หนีกด2"))
if x == 1:
    y = int(input("ใช้อาวุธ1กด1 อาวุธ2กด2 อาวุธ3กด3"))
    if y == 1:
        z = int(input("จะตีกี่รอบ"))
        for i in range(z):
            monterhp = monterhp - tuew1
            if monterhp == 0:
                print("you win")
            elif monterhp < 0:
                monterhp = monterhp + 20
            elif i == z:
                tuehp = 0
                print(f"มึงตาย hp ={tuehp}")
    elif y == 2:
        z = int(input("จะตีกี่รอบ"))
        for i in range(z):
            monterhp = monterhp - tuew2
            if monterhp == 0:
                print("you win")
            elif monterhp < 0:
                monterhp = monterhp + 20
            elif i == z:
                tuehp = 0
                print(f"มึงตาย hp ={tuehp}")
    elif y == 3:
        z = int(input("จะตีกี่รอบ"))
        for i in range(z):
            monterhp = monterhp - tuew3
            if monterhp == 0:
                print("you win")
            elif monterhp < 0:
                monterhp = monterhp + 20     
            elif i == z:
                tuehp = 0
                print(f"มึงตาย hp ={tuehp}")     
elif x == 2:
    print("หนีรอดจบ")


