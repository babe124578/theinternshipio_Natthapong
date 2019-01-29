นายณัฐพงศ์ เจียมจินตนารมย์
Mr. Natthapong Jiemjintanarom

Email: natthapong41@gmail.com

Tel: 0928963699

ได้ใช้ตัวแปลง XML to JSON จากเวปไซต์ https://www.journaldev.com/19392/python-xml-to-json-dict 
ซึ่งในส่วนอื่นๆนอกจากนี้ได้คิดเอง มีบางส่วนที่ได้ค้นหาจาก stackoverflow เช่น strip() และ splitlines()

วิธีรันโปรแกรม
  1.หากติดตั้ง python อยู่แล้วให้ลง module xmltodict เเละ json เพิ่ม ดังนี้ 
    1.1 เปิด cmd แล้วพิมพ์ pip install xmltodict และ json ให้เปลี่ยน xmltodict เป็น json
  2.รันโปรแกรมผ่าน cmd โดย cd ไปที่ directory ที่มี main.py อยู่ (.../weather/main.py)
  3.ใส่ชื่อไฟล์ นามสกุล .xml เข้าไป (มี .xml หรือไม่มีก็ได้) แล้วกด Enter
  4.โปรแกรมจะprintผลลัพธ์ออกมาและ Generate file JSON ใน directory เดียวกับ main.py
