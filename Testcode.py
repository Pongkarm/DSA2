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

# import re

# text = "Name: John Doe, Email: john.doe@example.com, Phone: 123-456-7890 655"

# # กำหนด Regular Expression ที่มีหลายกลุ่ม
# pattern = r"Name: (\w+ \w+), Email: (\S+@\S+), Phone: (\d{3}-\d{3}-\d{4}) (\d+)"

# # ค้นหาข้อความที่ตรงกับ pattern
# match = re.search(pattern, text)

# if match:
#     name = match.group(1)  # กลุ่มแรก คือชื่อ (John Doe)
#     email = match.group(2) # กลุ่มที่สอง คืออีเมล (john.doe@example.com)
#     phone = match.group(3) # กลุ่มที่สาม คือเบอร์โทรศัพท์ (123-456-7890)
#     phone = match.group(4) 
#     print(f"Name: {name}")
#     print(f"Email: {email}")
#     print(f"Phone: {phone}")
#     print(match.group(4))
# else:
#     print("ไม่พบข้อมูลที่ตรงกัน")


import re

line = "'1101' 'อำเภอบางเสาธง' '11' 'จังหวัดสมุทรปราการ'"

# ใช้ regex ที่ไม่ต้องการเครื่องหมาย '
match = re.findall(r"'(\d{4})'\s*'([ก-์a-zA-Z0-9\s]+)'\s*'(\d{2})'\s*'([ก-์a-zA-Z0-9\s]+)'", line)
print(match)

# if match:
#     # ข้อมูลที่จับได้จาก regex
#     code_group = match[0][0]  # รหัสกลุ่ม
#     group_name = match[0][1]  # ชื่อกลุ่ม
#     code_department = match[0][2]  # รหัสหน่วยงาน
#     department_name = match[0][3]  # ชื่อหน่วยงาน

#     print(f"รหัสกลุ่ม: {code_group}")
#     print(f"ชื่อกลุ่ม: {group_name}")
#     print(f"รหัสหน่วยงาน: {code_department}")
#     print(f"ชื่อหน่วยงาน: {department_name}")
# else:
#     print("ไม่พบข้อมูลที่ตรงกัน")

