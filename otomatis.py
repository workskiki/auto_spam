import pyautogui
import time
import subprocess
from datetime import datetime

# ===== CONFIGURASI =====
TARGET_NAME = "Pak Adi"  # Ganti dengan nama kontak
MESSAGE = "Selamat Siang"  # Pesan yang dikirim
COUNT = 5  # Jumlah pengiriman
DELAY = 3  # Jeda antar pesan (detik)

# ===== FUNGSI AJAIB =====
def open_whatsapp_directly():
    """Buka WhatsApp Desktop secara ajaib tanpa mouse"""
    try:
        # Method 1: Pake protocol handler (Work untuk Store version)
        subprocess.run(["start", "whatsapp:"], shell=True)
        
        # Method 2: Pake path langsung (Untuk non-Store)
        # subprocess.Popen(r"C:\Users\YourUser\AppData\Local\WhatsApp\WhatsApp.exe")
        
        print("🔮 Membuka WhatsApp...")
        time.sleep(10)  # Tunggu WhatsApp loading
    except:
        print("🚨 WhatsApp tidak ditemukan! Pastikan sudah terinstall")

def focus_chat():
    """Auto-fokus ke chat target tanpa klik manual"""
    try:
        # 1. Buka pencarian (Ctrl+F)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(2)
        
        # 2. Ketik nama kontak
        pyautogui.write(TARGET_NAME)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)
        
        # 3. Auto-klik area chat (koordinat ajaib)
        pyautogui.click(x=800, y=700)  # Ganti dengan koordinatmu!
        time.sleep(1)
    except:
        print("👻 Gagal fokus ke chat, coba manual ya!")

def send_messages():
    """Kirim pesan beruntun"""
    print(f"\n✨ Mulai mengirim {COUNT} pesan ke {TARGET_NAME}")
    for i in range(COUNT):
        pyautogui.write(f"{MESSAGE}")
        pyautogui.press('enter')
        print(f"📤 Pesan {i+1} terkirim!")
        time.sleep(DELAY)

# ===== MAIN PROGRAM =====
if __name__ == "__main__":
    print("""
    WA-AUTO SENDER v2.0
    (Tanpa sentuh mouse!)
    """)
    
    # 1. Buka WhatsApp
    open_whatsapp_directly()
    
    # 2. Fokus ke chat target
    focus_chat()
    
    # 3. Mulai pengiriman
    send_messages()
    
    print("\n✅ Selesai! Jangan lupa dibales ya~")
