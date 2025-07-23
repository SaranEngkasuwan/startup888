grade = float(input("กรุณาใส่เกรดของคุณ"))
if grade > 50:
    print("ผ่าน")
    if grade >= 50 and grade < 60:
        print("D")
    elif grade >= 60 and grade < 70:
        print("C")
    elif grade >= 70 and grade < 80:
        print("B")
    elif grade >= 80:
        print("A")
else:
    print("ไม่ผ่าน คุณได้เกรด F")