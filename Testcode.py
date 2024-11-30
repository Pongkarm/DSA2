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

# text = "My email is example@test.com and phone is 123-456-7890."

# # ค้นหาอีเมลและเบอร์โทรศัพท์ในข้อความ
# match = re.search(r"(\S+@\S+)\s.*?(\d{3}-\d{3}-\d{4})", text)

# if match:
#     email = match.group(1)  # กลุ่มแรกที่จับคืออีเมล
#     phone = match.group(2)  # กลุ่มที่สองที่จับคือเบอร์โทรศัพท์
#     print(f"Email: {email}")
#     print(f"Phone: {phone}")



text = "My email is example@test.com and phone is '123'-'456-7890'."

# ค้นหาอีเมลและเบอร์โทรศัพท์ในข้อความ
match = re.findall(r"\d+'", text)

if match:
    email = match
    print(f"Email: {match}")