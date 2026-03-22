#!/usr/bin/env python3
"""
TOZ YAPI - FAVICON OLUŞTURUCU
Mevcut logodan tüm favicon boyutlarını oluşturur
"""

import os
from PIL import Image, ImageDraw

# Logo dosyası
LOGO_PATH = r"C:\Users\Admin\Desktop\TOZYAPIWEB\Web\webSiteLogo\TozEcoLogo.png"
OUTPUT_FOLDER = r"C:\Users\Admin\Desktop\TOZYAPIWEB\Web"

# Gerekli favicon boyutları
FAVICON_SIZES = {
    "favicon.ico": (16, 24, 32, 48, 64),  # Multi-size ICO
    "favicon-16x16.png": (16, 16),
    "favicon-32x32.png": (32, 32),
    "apple-touch-icon.png": (180, 180),
    "android-chrome-192x192.png": (192, 192),
    "android-chrome-512x512.png": (512, 512),
}

def create_favicon_sizes():
    """Tüm favicon boyutlarını oluştur"""
    
    print("=" * 60)
    print("TOZ YAPI - FAVICON OLUŞTURUCU")
    print("=" * 60)
    print()
    
    # Logo kontrolü
    if not os.path.exists(LOGO_PATH):
        print(f"HATA: Logo bulunamadı: {LOGO_PATH}")
        print("Lütfen logo dosyasını kontrol edin.")
        return False
    
    print(f"Logo: {LOGO_PATH}")
    print()
    
    # Logoyu aç
    try:
        logo = Image.open(LOGO_PATH)
        print(f"Logo boyutu: {logo.size[0]}x{logo.size[1]} px")
        print(f"Logo modu: {logo.mode}")
        print()
    except Exception as e:
        print(f"HATA: Logo açılamadı: {e}")
        return False
    
    # Her boyut için favicon oluştur
    created_files = []
    
    for filename, size in FAVICON_SIZES.items():
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        
        try:
            # Logoyu yeniden boyutlandır
            if isinstance(size, tuple) and len(size) == 2:
                resized = logo.resize(size, Image.Resampling.LANCZOS)
            else:
                continue
            
            # Kaydet
            if filename.endswith(".ico"):
                # ICO format - multiple sizes
                sizes = [(s, s) for s in size]
                resized.save(output_path, format="ICO", sizes=sizes)
            else:
                # PNG format
                resized.save(output_path, format="PNG")
            
            created_files.append(filename)
            print(f"✓ Oluşturuldu: {filename} ({size[0]}x{size[1]})")
        
        except Exception as e:
            print(f"✗ HATA ({filename}): {e}")
    
    print()
    print("-" * 60)
    print()
    
    if created_files:
        print(f"BAŞARILI! {len(created_files)} favicon dosyası oluşturuldu:")
        for f in created_files:
            print(f"  - {f}")
        print()
        
        # HTML'e eklenecek kod
        print("HTML'E EKLENECEK KODLAR:")
        print("-" * 60)
        print("""
<!-- Favicon -->
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
<link rel="android-chrome" sizes="192x192" href="android-chrome-192x192.png">
<link rel="android-chrome" sizes="512x512" href="android-chrome-512x512.png">
        """)
        print("-" * 60)
        print()
        
        return True
    else:
        print("HATA: Hiçbir favicon oluşturulamadı!")
        return False

if __name__ == "__main__":
    success = create_favicon_sizes()
    if success:
        print("Favicon'lar index.html'in bulunduğu klasöre kaydedildi.")
        print("index.html dosyasına <head> bölümüne favicon linklerini ekleyin.")
    else:
        print("\nİşlem başarısız oldu. Lütfen logo dosyasını kontrol edin.")
    
    input("\nTamamlamak için Enter'a basın...")
