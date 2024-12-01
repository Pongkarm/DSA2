import re

#EX 1 

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")
  

#EX2

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)

import re

import re

text = "Name: John Doe, Email: john.doe@example.com, Phone: 123-456-7890"

# กำหนด Regular Expression ที่มีหลายกลุ่ม
pattern = r"Name: (\w+ \w+), Email: (\S+@\S+), Phone: (\d{3}-\d{3}-\d{4})"

# ค้นหาข้อความที่ตรงกับ pattern
match = re.search(pattern, text)

if match:
    name = match.group(1)  # กลุ่มแรก คือชื่อ (John Doe)
    email = match.group(2) # กลุ่มที่สอง คืออีเมล (john.doe@example.com)
    phone = match.group(3) # กลุ่มที่สาม คือเบอร์โทรศัพท์ (123-456-7890)
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
else:
    print("ไม่พบข้อมูลที่ตรงกัน")


