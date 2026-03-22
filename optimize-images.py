#!/usr/bin/env python3
"""
TOZ YAPI - GÖRSEL OPTİMİZASYON SCRIPTİ
Büyük PNG dosyalarını WebP formatına çevirir
Kalite: %85, Hedef boyut: <500 KB
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("PIL/Pillow kütüphanesi bulunamadı!")
    print("Yüklemek için: pip install Pillow")
    sys.exit(1)

# Klasör yolu
HERO_FOLDER = r"C:\Users\Admin\Desktop\TOZYAPIWEB\Web\assets\images\hero"

# Optimize edilecek dosyalar (mevcut büyük PNG'ler)
LARGE_FILES = {
    "hero-kapi-pencere-dograma.png": 5.9 * 1024 * 1024,  # 5.9 MB
    "hero-bahce-cit.png": 5.3 * 1024 * 1024,  # 5.3 MB
    "hero-havuz-kapama.png": 4.6 * 1024 * 1024,  # 4.6 MB
    "hero-sundurma-carport.png": 3.1 * 1024 * 1024,  # 3.1 MB
    "hero-akilli-cam.png": 1.6 * 1024 * 1024,  # 1.6 MB
    "hero-giyotin.png": 1.6 * 1024 * 1024,  # 1.6 MB
}

def get_file_size(filepath):
    """Dosya boyutunu MB cinsinden döndür"""
    return os.path.getsize(filepath) / (1024 * 1024)

def optimize_image(input_path, output_path, quality=85):
    """
    PNG dosyasını WebP'ye çevir
    
    Args:
        input_path: Giriş PNG dosyası
        output_path: Çıkış WebP dosyası
        quality: Kalite (0-100, önerilen: 85)
    """
    try:
        img = Image.open(input_path)
        
        # RGBA ise RGB'ye çevir (WebP transparency destekler ama bazı durumlarda sorun olur)
        if img.mode in ("RGBA", "LA"):
            # Transparency koru
            img.save(output_path, "WEBP", quality=quality, lossless=False)
        else:
            img.convert("RGB").save(output_path, "WEBP", quality=quality, lossless=False)
        
        original_size = get_file_size(input_path)
        new_size = get_file_size(output_path)
        savings = ((original_size - new_size) / original_size) * 100
        
        return True, original_size, new_size, savings
    
    except Exception as e:
        return False, 0, 0, str(e)

def main():
    print("=" * 60)
    print("TOZ YAPI - GÖRSEL OPTİMİZASYONU")
    print("=" * 60)
    print()
    
    # Klasör kontrolü
    if not os.path.exists(HERO_FOLDER):
        print(f"HATA: Klasör bulunamadı: {HERO_FOLDER}")
        sys.exit(1)
    
    os.chdir(HERO_FOLDER)
    
    print(f"Klasör: {HERO_FOLDER}")
    print()
    print("Optimize edilecek dosyalar:")
    for filename, estimated_size in LARGE_FILES.items():
        print(f"  - {filename} ({estimated_size/(1024*1024):.1f} MB)")
    
    print()
    print("-" * 60)
    print()
    
    # İstatistikler
    total_original = 0
    total_new = 0
    success_count = 0
    error_count = 0
    
    # Dosyaları işle
    for filename in LARGE_FILES.keys():
        input_path = os.path.join(HERO_FOLDER, filename)
        output_filename = filename.replace(".png", ".webp")
        output_path = os.path.join(HERO_FOLDER, output_filename)
        
        if not os.path.exists(input_path):
            print(f"[ATLANDI] {filename} bulunamadı")
            continue
        
        print(f"[İŞLENİYOR] {filename}...")
        
        success, orig_size, new_size, result = optimize_image(input_path, output_path)
        
        if success:
            total_original += orig_size
            total_new += new_size
            success_count += 1
            
            print(f"  ✓ Başarılı!")
            print(f"    Orijinal: {orig_size:.2f} MB")
            print(f"    Yeni:     {new_size:.2f} MB")
            print(f"    Tasarruf: {result:.1f}%")
        else:
            error_count += 1
            print(f"  ✗ HATA: {result}")
        
        print()
    
    # Özet
    print("=" * 60)
    print("OPTİMİZASYON TAMAMLANDI")
    print("=" * 60)
    print()
    print(f"Başarılı: {success_count} dosya")
    print(f"Hatalı:   {error_count} dosya")
    print()
    
    if total_original > 0:
        total_savings = ((total_original - total_new) / total_original) * 100
        print(f"Toplam Tasarruf:")
        print(f"  Önce: {total_original:.2f} MB")
        print(f"  Sonra: {total_new:.2f} MB")
        print(f"  Azalma: {total_savings:.1f}%")
        print(f"  Kazanılan: {(total_original - total_new):.2f} MB")
    
    print()
    print("-" * 60)
    print()
    print("ÖNERİLER:")
    print("  1. WebP dosyalarını test edin")
    print("  2. Orijinal PNG'leri yedekleyin veya silin")
    print("  3. HTML'de <picture> tag kullanın (fallback için)")
    print()
    print("HTML ÖRNEĞİ:")
    print('  <picture>')
    print('    <source srcset="hero-image.webp" type="image/webp">')
    print('    <img src="hero-image.png" alt="Hero Image">')
    print('  </picture>')
    print()

if __name__ == "__main__":
    main()
