# 🔤 İSİMLENDİRME STANDARDİZASYONU

**Tarih:** 2026-03-22  
**Öncelik:** Yüksek (SEO ve URL yapısı için kritik)

---

## ❌ SORUNLU KLASÖRLER

### Türkçe Karakter İçerenler:
```
Ürün Gruplarımız        → urun-gruplari
İletişim                → iletisim
İş ortaklarımız         → is-ortaklarimiz
S.S.S                   → sss
Referanslar             → referanslar (zaten iyi)
Hakkımızda              → hakkimizda (zaten iyi)
Online Mağaza           → online-magaza
Katalog                 → katalog (zaten iyi)
```

### Alt Kategoriler:
```
Ürün Gruplarımız/
├── (ALÜMİNYUM - PVC - AHŞAP )KAPI...  → kapi-pencere-dograma
├── AÇIK HAVA MUTFAKLARI               → acik-hava-mutfaklari
├── AKILLI CAM UYGULAMALARI            → akilli-cam-uygulamalari
├── BAHÇE VE ÇİT SİSTEMLERİ            → bahce-ve-cit-sistemleri
├── DIŞ CEPHE JALUZİSİ -BRISOLEY-      → dis-cephe-jaluzisi-brisoley
├── HAVUZ KAPAMA ÇÖZÜMLERİ             → havuz-kapama-cozumleri
├── ISITMA VE SOGUTMA SİSTEMLERİ       → isitma-ve-sogutma-sistemleri
├── KAPI SİSTEMLERİ                    → kapi-sistemleri
├── KEPENK SİSTEMLERİ                  → kepenk-sistemleri
├── KIŞ BAHÇESİ                        → kis-bahcesi
├── PANJUR SİSTEMLERİ                  → panjur-sistemleri
├── PERGOLA ROLLING ROOF...            → pergola-rolling-roof-bioclimatic
├── SUNDURMA ve ARAÇ PARKI             → sundurma-ve-arac-parki
├── TURNIKE VE BARIYER SİSTEMLER       → turnike-ve-bariyer-sistemleri
├── YERLİ VE İTHAL SİNEKLİK            → yerli-ve-ithal-sineklik
└── ZİP PERDE GİYOTİN...               → zip-perde-giyotin-ruzgar-kirici
```

---

## ✅ ÇÖZÜM SEÇENEKLERİ

### Seçenek 1: Klasörleri Yeniden Adlandır (Önerilen)

Windows'ta manuel olarak:
1. Her klasöre sağ tık → Yeniden adlandır
2. Yukarıdaki tabloyu kullan
3. HTML dosyalarındaki linkleri güncelle

### Seçenek 2: URL Rewrite (.htaccess)

`.htaccess` dosyasına ekle:

```apache
# Türkçe karakterli URL'leri düzelt
RewriteEngine On
RewriteRule ^ürün-grupplarimiz/?$ /urun-gruplari [R=301,L]
RewriteRule ^İletişim/?$ /iletisim [R=301,L]
RewriteRule ^İş-ortaklarimiz/?$ /is-ortaklarimiz [R=301,L]
RewriteRule ^S\.S\.S/?$ /sss [R=301,L]
RewriteRule ^Online-Mağaza/?$ /online-magaza [R=301,L]
```

### Seçenek 3: Sembolik Linkler (Linux Sunucu)

SSH ile bağlan:
```bash
cd /var/www/tozyapi
ln -s "Ürün Gruplarımız" urun-gruplari
ln -s "İletişim" iletisim
ln -s "İş ortaklarımız" is-ortaklarimiz
```

---

##  HTML GÜNCELLEMESİ

### index.html Dosyasında:

**Önce:**
```html
<a href="Ürün Gruplarımız/kapi-pencere.html">Kapi-Pencere</a>
```

**Sonra:**
```html
<a href="urun-gruplari/kapi-pencere.html">Kapi-Pencere</a>
```

---

## 🔄 OTOMATIK SCRIPT (PowerShell)

Windows için:

```powershell
# Klasör yeniden adlandırma script'i
$basePath = "C:\Users\Admin\Desktop\TOZYAPIWEB\Web"

$replacements = @{
    "Ürün Gruplarımız" = "urun-gruplari"
    "İletişim" = "iletisim"
    "İş ortaklarımız" = "is-ortaklarimiz"
    "S.S.S" = "sss"
    "Online Mağaza" = "online-magaza"
}

foreach ($old in $replacements.Keys) {
    $oldPath = Join-Path $basePath $old
    $newPath = Join-Path $basePath $replacements[$old]
    
    if (Test-Path $oldPath) {
        Rename-Item -Path $oldPath -NewName $replacements[$old]
        Write-Host "✓ $old → $($replacements[$old])"
    }
}
```

---

## ⚠️ DİKKAT EDİLECEKLER

1. **SEO Etkisi:** 
   - Eski URL'lere 301 redirect ekle
   - Google Search Console'da değişiklik bildir

2. **Backlinkler:**
   - Dış backlink'ler eski URL'lere işaret edebilir
   - Redirect kuralları ekle

3. **Internal Linking:**
   - Tüm HTML dosyalarındaki linkleri güncelle
   - Find & replace kullan

4. **Sitemap.xml:**
   - Yeni URL'lerle güncelle
   - Search Console'a submit et

---

## ✅ KONTROL LİSTESİ

- [ ] Klasörler yeniden adlandırıldı
- [ ] .htaccess redirect kuralları eklendi
- [ ] index.html linkleri güncellendi
- [ ] blog-template.html güncellendi
- [ ] sitemap.xml güncellendi
- [ ] robots.txt kontrol edildi
- [ ] 301 redirect'ler test edildi

---

##  ÖNERİLEN SIRALAMA

1. **Önce** `.htaccess` dosyasına redirect ekle
2. **Sonra** klasörleri yeniden adlandır
3. **Ardından** HTML dosyalarını güncelle
4. **En son** test et (tüm linkleri kontrol et)

---

**Not:** Builder'a teslim etmeden önce bu işlemin yapılması SEO için kritiktir!

**Son Güncelleme:** 2026-03-22
