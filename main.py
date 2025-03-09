import threading
import time

# ฟังก์ชันสำหรับจำลองการโหลดข้อมูล
def load_data(count):
    print(f"Loading {count}%...")
    time.sleep(1)  # ใช้เวลา 1 วินาทีในการโหลดแต่ละขั้น
    print(f"Completed {count}%")

# ฟังก์ชันแสดงข้อความต้อนรับ
def print_welcome_message():
    print("Welcome to the data loading simulation!")
    time.sleep(2)  # หน่วงเวลา 2 วินาที
    print("Starting to load data...")

# ฟังก์ชันหลักที่จะโหลดข้อมูลจาก 1% ถึง 100%
def load_all_data():
    for i in range(1, 101):  # เริ่มตั้งแต่ 1% ไปจนถึง 100%
        thread = threading.Thread(target=load_data, args=(i,))
        thread.start()
        thread.join()  # รอให้ thread ทำงานเสร็จในแต่ละครั้ง


# สร้าง thread สำหรับแสดงข้อความต้อนรับ
thread2 = threading.Thread(target=print_welcome_message)
thread2.start()

# รอให้ thread ต้อนรับทำงานเสร็จ
thread2.join()

# เริ่มการโหลดข้อมูล
load_all_data()

print("All data has been loaded!")
