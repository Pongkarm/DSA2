#แบบแรก หาจังหวัดผ่านเลข จากfile result_province.txt
import re

# รับ input จากผู้ใช้
user = input('ใส่จังหวัดที่ต้องการหา เช่น "กรุงเทพมหานคร" หรือ "10": ')

# เปิดไฟล์และค้นหาข้อมูล
with open('result_province.txt', 'r', encoding='utf-8') as file:
 for line in file:
        if re.search(re.escape(user), line):
            # ดึงข้อมูลในวงเล็บ
            match = re.search(r"\('(\d+)', '([^']+)'\)", line)
            if match:
                province_code = match.group(1)  # รหัสจังหวัด
                province_name = match.group(2)  # ชื่อจังหวัด
                print(f"{province_code}, {province_name}")

