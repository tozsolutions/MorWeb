#!/usr/bin/env python3
"""
TOZ YAPI - ÜRÜN GÖRSELLERİ ORGANİZASYONU
Tüm ürün görsellerini assets/products/ klasörüne kategorize eder
"""

import os
import shutil
from pathlib import Path

# Kaynak ve hedef klasörler
SOURCE_FOLDER = r"C:\Users\Admin\Desktop\TOZYAPIWEB\Web"
DESTINATION_FOLDER = r"C:\Users\Admin\Desktop\TOZYAPIWEB\Web\assets\images\products"

# Kategori eşleştirmaları (klasör adı → product slug)
CATEGORIES = {
    "KAPI SİSTEMLERİ": "kapi-sistemleri",
    "Otomatik Kapılar": "otomatik-kapilar",
    "Garaj Kapıları": "garaj-kapilari",
    "PVC Kapılar": "pvc-kapilar",
    "Akustık Kapılar": "akustik-kapilar",
    "Bahçe Kapıları": "bahce-kapilari",
    "Yangın Kapıları": "yangin-kapilari",
    
    "KEPENK SİSTEMLERİ": "kepenk-sistemleri",
    "Alüminyum Kepenk": "aluminyum-kepenk",
    "Katlanır Kepenk": "katanir-kepenk",
    "Kayar Katlanır Kepenk": "kayar-katanir-kepenk",
    "Şeffaf Kepenk": "seffaf-kepenk",
    "Balistik Kepenk": "balistik-kepenk",
    
    "PANJUR SİSTEMLERİ": "panjur-sistemleri",
    "Ahşap Panjur": "ahsap-panjur",
    "Gizli Panjur": "gizli-panjur",
    "Makaslı Panjur": "makasli-panjur",
    "Monoblok Panjur": "monoblok-panjur",
    
    "PERGOLA ROLLING ROOF BIOCLOMATIC TENTE": "pergola-bioclimatic",
    "BIO-CLOMATIC": "bio-clomatic",
    "CAM TAVAN": "cam-tavan",
    "PERGOLA": "pergola",
    "ROLLING ROOF": "rolling-roof",
    "TENTE": "tente",
    
    "ZİP PERDE GİYOTİN RÜZGAR KIRICI SÜRME SİSTEMLERİ": "zip-perde-sistemleri",
    "GİYOTİN SİSTEMLERİ": "giyotin",
    "RÜZGAR KIRICI SİSTEMLERİ": "ruzgar-kirici",
    "SÜRME SİSTEMLERİ": "surme",
    "ZİP PERDE SİSTEMLERİ": "zip-perde",
    
    "HAVUZ KAPAMA ÇÖZÜMLERİ": "havuz-kapama",
    "KIŞ BAHÇESİ": "kis-bahcesi",
    "DIŞ CEPHE JALUZİSİ -BRISOLEY-": "brisoley",
    "BAHÇE VE ÇİT SİSTEMLERİ": "bahce-cit",
    "AKILLI CAM UYGULAMALARI": "akilli-cam",
    "SUNDURMA ve ARAÇ PARKI (carport)": "sundurma-carport",
    "TURNIKE VE BARIYER SİSTEMLER": "turnike-bariyer",
    "YERLİ VE İTHAL SİNEKLİK SİSTEMLERİ": "sineklik",
}

def create_category_folders():
    """Her kategori için klasör oluştur"""
    for category, slug in CATEGORIES.items():
        cat_folder = os.path.join(DESTINATION_FOLDER, slug)
        os.makedirs(cat_folder, exist_ok=True)
        print(f"✓ Klasör oluşturuldu: {slug}")

def find_and_copy_images():
    """Tüm görselleri bul ve uygun klasörlere kopyala"""
    
    # Görsel uzantıları
    IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}
    
    # İstatistikler
    total_found = 0
    total_copied = 0
    total_skipped = 0
    
    print("\n" + "=" * 60)
    print("GÖRSELLER ARANIYOR...")
    print("=" * 60 + "\n")
    
    # Tüm klasörleri gez
    for root, dirs, files in os.walk(SOURCE_FOLDER):
        # assets klasörünü atla (zaten orada)
        if 'assets' in root:
            continue
        
        for file in files:
            ext = Path(file).suffix.lower()
            if ext not in IMAGE_EXTENSIONS:
                continue
            
            total_found += 1
            source_path = os.path.join(root, file)
            
            # Hangi kategoriye ait olduğunu bul
            relative_path = os.path.relpath(root, SOURCE_FOLDER)
            category_slug = None
            
            # Kategori eşleştirme
            for category, slug in CATEGORIES.items():
                if category in relative_path or category.upper() in relative_path.upper():
                    category_slug = slug
                    break
            
            if not category_slug:
                # Genel products klasörüne kopyala
                category_slug = "diger"
                other_folder = os.path.join(DESTINATION_FOLDER, category_slug)
                os.makedirs(other_folder, exist_ok=True)
            
            # Hedef path
            dest_folder = os.path.join(DESTINATION_FOLDER, category_slug)
            dest_path = os.path.join(dest_folder, file)
            
            # Zaten varsa atlama
            if os.path.exists(dest_path):
                print(f"⊘ ATLANDI: {file} (zaten var)")
                total_skipped += 1
                continue
            
            # Kopyala
            try:
                shutil.copy2(source_path, dest_path)
                print(f"✓ KOPYALANDI: {file} → {category_slug}/")
                total_copied += 1
            except Exception as e:
                print(f"✗ HATA: {file} - {e}")
    
    return total_found, total_copied, total_skipped

def main():
    print("=" * 60)
    print("TOZ YAPI - ÜRÜN GÖRSELLERİ ORGANİZASYONU")
    print("=" * 60)
    print()
    
    # Kaynak kontrol
    if not os.path.exists(SOURCE_FOLDER):
        print(f"HATA: Kaynak klasör bulunamadı: {SOURCE_FOLDER}")
        return
    
    # Hedef klasörleri oluştur
    print("Klasörler oluşturuluyor...")
    os.makedirs(DESTINATION_FOLDER, exist_ok=True)
    create_category_folders()
    
    print("\n" + "=" * 60)
    print("GÖRSELLER KOPYALANIYOR...")
    print("=" * 60 + "\n")
    
    # Görselleri kopyala
    found, copied, skipped = find_and_copy_images()
    
    # Özet
    print("\n" + "=" * 60)
    print("TAMAMLANDI!")
    print("=" * 60)
    print()
    print(f"Bulunan:  {found} görsel")
    print(f"Kopyalanan: {copied} görsel")
    print(f"Atlanan:  {skipped} görsel")
    print()
    
    # Kategori özeti
    print("Kategori Özeti:")
    print("-" * 60)
    
    for category, slug in CATEGORIES.items():
        cat_folder = os.path.join(DESTINATION_FOLDER, slug)
        if os.path.exists(cat_folder):
            count = len([f for f in os.listdir(cat_folder) 
                        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])
            if count > 0:
                print(f"  {slug}: {count} görsel")
    
    print()
    print("-" * 60)
    print()
    print("SONRAKİ ADIMLAR:")
    print("  1. assets/products/ klasörünü kontrol et")
    print("  2. Online Mağaza'da bu görselleri kullan")
    print("  3. Gereksiz kopyaları sil")
    print()

if __name__ == "__main__":
    main()
