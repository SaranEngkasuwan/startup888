member = str(input("สมาชิกระดับใด"))
price = float(input("ราคาเท่าไร"))
date = int(input("วันที่เท่าไร"))
if member == "gold":
    if price >= 1000:
        price = price  + price*(15/100)
        print("ราคาที่ลดแล้วคือ",price,"บาท")
        if date % 2 != 0:
            if price > 500:
                price = price  + price*(5/100)
                print("วันนี้เลขคี่ลดราคาเป็น",price,"บาท")
            else:
                print("ไม่ลดแล้ว",price,"บาท")
        else:
            print("ไม่ลดแล้ว",price,"บาท")
    else:
        price = price  + price*(10/100)
        print("ราคาที่ลดแล้วคือ",price,"บาท")
elif member == "silver":
    if price >= 1000:
        price = price  + price*(10/100)
        print("ราคาที่ลดแล้วคือ",price,"บาท")
        if date % 2 == 1:
            if price > 500:
                price = price  + price*(5/100)
                print("วันนี้เลขคี่ลดราคาเป็น",price,"บาท")
            else:
                print("ไม่ลดแล้ว",price,"บาท")
        else:
            print("ไม่ลดแล้ว",price,"บาท")
    else:
        price = price  + price*(10/100)
        print("ราคาที่ลดแล้วคือ",price,"บาท")
else:
    print("ลูกค้าไม่เป็นสมาชิกไม่มีส่วนลด")
if price < 800:
    price = price + 50
    print("ค่าส่ง 50 บาท ราคาสุทธิเท่ากับ",price,"บาท")
elif price >= 800:
    print("ส่งฟรี ราคาสุทธิเท่ากับ",price,"บาท")
