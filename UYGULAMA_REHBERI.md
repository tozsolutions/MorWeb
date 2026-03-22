# 🚀 TOZ YAPI WEB - UYGULAMA REHBERİ

**Tüm İşlemler Adım Adım**  
**Tarih:** 2026-03-22

---

## 📋 İÇİNDEKİLER

1. [SSL Sertifikası Kurulumu](#1-ssl-sertifikası-kurulumu)
2. [Görsel Optimizasyonu (WebP)](#2-görsel-optimizasyonu-webp)
3. [.htaccess Sunucuya Yükleme](#3-htaccess-sunucuya-yükleme)
4. [Favicon Oluşturma](#4-favicon-oluşturma)
5. [Google Analytics Kurulumu](#5-google-analytics-kurulumu)
6. [Blog Sayfaları HTML Dönüşümü](#6-blog-sayfaları-html-dönüşümü)
7. [Ürün Görselleri Organizasyonu](#7-ürün-görselleri-organizasyonu)

---

## 1. SSL SERTİFİKASI KURULUMU

### Gereksinimler:
- Hosting hesabı (cPanel/Plesk)
- Domain: tozyapi.com.tr

### Adımlar:

#### A) cPanel Üzerinden (En Kolay):

```bash
1. cPanel'e giriş yap
2. Security → SSL/TLS
3. "Manage SSL sites"
4. tozyapi.com.tr seç
5. "Run AutoSSL" tıkla
6. 10 dakika bekle
```

#### B) Plesk Üzerinden:

```bash
1. Plesk Panel giriş
2. Domains → tozyapi.com.tr
3. Let's Encrypt sekmesi
4. "Get It Free" tıkla
5. Email gir: merhaba@tozyapi.com.tr
6. Onayla
```

#### C) .htaccess HTTPS Yönlendirmesi:

**.htaccess dosyasında şu satırları açın (yorumdan çıkarın):**

```apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</IfModule>
```

### Doğrulama:

```
✓ https://www.tozyapi.com.tr açılıyor mu?
✓ Tarayıcıda 🔒 kilit simgesi var mı?
✓ sslabs.com/ssltest ile test et (Grade A+ hedefle)
```

**Detaylı Rehber:** `SSL_KURULUM_REHBERI.md`

---

## 2. GÖRSEL OPTİMİZASYONU (WebP)

### Gereksinimler:

**Python Script ile (Önerilen):**
```bash
pip install Pillow
```

**veya**

**Batch Script ile:**
- WebP binary indir: https://developers.google.com/speed/webp/download

### Adımlar:

#### A) Python Script ile:

```bash
cd C:\Users\Admin\Desktop\TOZYAPIWEB\Web
python optimize-images.py
```

**Otomatik olarak şunları yapar:**
- 6 büyük PNG dosyasını bulur
- WebP formatına çevirir
- %85 kalite kullanır
- Özet rapor gösterir

#### B) Manuel (Online Araç):

```
1. squoosh.app aç
2. Dosyaları sürükle:
   - hero-kapi-pencere-dograma.png
   - hero-bahce-cit.png
   - hero-havuz-kapama.png
   - hero-sundurma-carport.png
   - hero-akilli-cam.png
   - hero-giyotin.png
3. Format: WebP, Quality: 85
4. Download all
```

### Sonuç:

```
Önce: ~22 MB
Sonra: ~3 MB
Tasarruf: 86%
```

### HTML Güncelleme:

```html
<picture>
  <source srcset="assets/images/hero/hero-image.webp" type="image/webp">
  <img src="assets/images/hero/hero-image.png" alt="Hero Image">
</picture>
```

---

## 3. .HTACCESS SUNUCUYA YÜKLEME

### Dosya Konumu:

```
C:\Users\Admin\Desktop\TOZYAPIWEB\Web\.htaccess
```

### Adımlar:

#### A) FTP ile Yükleme:

```bash
1. FileZilla veya WinSCP aç
2. Hosting bilgileri ile bağlan:
   Host: ftp.tozyapi.com.tr
   User: tozyapi
   Pass: ********
3. Local: C:\Users\Admin\Desktop\TOZYAPIWEB\Web\.htaccess
4. Remote: /public_html/.htaccess
5. Upload (ASCII mode)
```

#### B) cPanel File Manager:

```bash
1. cPanel → File Manager
2. public_html klasörüne git
3. Upload → .htaccess dosyasını seç
4. Upload tamamla
5. Permissions: 644 olmalı
```

### Doğrulama:

```bash
# .htaccess yüklendi mi?
https://www.tozyapi.com.tr/.htaccess
# 403 Forbidden veya 404 vermeli (erişim engelli)

# HTTPS yönlendirmesi çalışıyor mu?
http://www.tozyapi.com.tr
# Otomatik https://'e yönlendirmeli
```

**Dosya İçeriği:** Zaten hazır, sadece yükleyin!

---

## 4. FAVICON OLUŞTURMA

### Gereksinimler:

```bash
pip install Pillow
```

### Adımlar:

#### A) Python Script ile:

```bash
cd C:\Users\Admin\Desktop\TOZYAPIWEB\Web
python generate-favicon.py
```

**Otomatik olarak oluşturur:**
- favicon.ico (multi-size)
- favicon-16x16.png
- favicon-32x32.png
- apple-touch-icon.png (180x180)
- android-chrome-192x192.png
- android-chrome-512x512.png

#### B) Online Araç:

```
1. realfavicongenerator.net aç
2. Logo dosyasını yükle (TozEcoLogo.png)
3. Tüm platformlar için ayarla
4. Download package
5. Web/ klasörüne çıkar
```

### HTML Güncelleme:

**index.html `<head>` bölümüne ekleyin:**

```html
<!-- Favicon -->
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
<link rel="android-chrome" sizes="192x192" href="android-chrome-192x192.png">
<link rel="android-chrome" sizes="512x512" href="android-chrome-512x512.png">
```

---

## 5. GOOGLE ANALYTICS KURULUMU

### Adımlar:

#### A) Analytics Hesabı Oluştur:

```bash
1. analytics.google.com git
2. "Başla" tıkla
3. Google hesabı ile giriş
4. Account: Toz Yapı Teknolojileri
5. Property: Toz Yapı Web
6. Data Stream: Web → tozyapi.com.tr
7. Measurement ID al: G-XXXXXXXXXX
```

#### B) Tracking Kodunu Ekle:

**blog-template.html ve diğer sayfalara:**

```html
<head>
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
...
</head>
```

#### C) Google Tag Manager (Opsiyonel ama önerilen):

```bash
1. tagmanager.google.com
2. Account: Toz Yapı
3. Container: tozyapi-web
4. GTM kodunu al: GTM-XXXXXXX
5. index.html'e ekle (head ve body üstüne)
```

### Event Tracking:

**WhatsApp tıklama takibi ekleyin:**

```javascript
document.querySelectorAll('a[href*="wa.me"]').forEach(link => {
  link.addEventListener('click', function() {
    gtag('event', 'whatsapp_click', {
      'event_category': 'Contact',
      'event_label': 'WhatsApp Button'
    });
  });
});
```

### Doğrulama:

```
✓ Realtime raporu kontrol et (analytics.google.com)
✓ Tag Assistant Chrome extension ile test et
✓ 24-48 saat sonra veri gelmeye başlar
```

**Detaylı Rehber:** `GOOGLE_ANALYTICS_KURULUMU.md`

---

## 6. BLOG SAYFALARI HTML DÖNÜŞÜMÜ

### Mevcut Durum:

```
Blog/
├── AKILLI EV SİSTEMLERİ ve ENTEGRASYONLAR/
│   └── resimler
├── ALÜMİNYUM SİSTEMLER HAKKINDA/
│   ├── ..._english.html
│   └── ..._turkce.html
└── SÜRME DOĞRAMALAR HAKKINDA/
    └── ...html
```

### Adımlar:

#### A) Template Kullanarak Yeni Sayfa Oluştur:

```bash
1. blog-template.html dosyasını aç
2. Placeholder'ları değiştir:
   - {BLOG_TITLE} → Yazı başlığı
   - {BLOG_DESCRIPTION} → Meta açıklama
   - {BLOG_IMAGE} → Hero görsel path
   - {BLOG_CONTENT} → Tam içerik
3. Kaydet: blog/{slug}.html
```

#### B) Örnek Dönüşüm:

**Kaynak:** `Blog/ALÜMİNYUM SİSTEMLER HAKKINDA/..._turkce.html`

**Hedef:** `Blog/aluminyum-sistemler-hakkinda.html`

```bash
1. blog-template.html kopyala
2. Şablon değişkenlerini doldur:
   Title: Alüminyum Sistemler Hakkında
   Category: Mimari Çözümler
   Date: 2026-03-22
   Read Time: 5 dk
3. İçeriği kopyala (HTML formatında)
4. Resimleri assets/images/blog/ klasörüne taşı
5. Kaydet
```

#### C) Tüm Blog Yazıları İçin:

1. **Akıllı Ev Sistemleri** → `blog/akilli-ev-sistemleri.html`
2. **Alüminyum Sistemler** → `blog/aluminyum-sistemler.html`
3. **Sürme Doğramalar** → `blog/surme-dogramalar.html`

### Ana Blog Sayfası Oluştur:

**File:** `Blog/index.html`

```html
<!DOCTYPE html>
<html lang="tr">
<head>
<title>Blog | Toz Yapı Teknolojileri</title>
...
</head>
<body>
<h1>Toz Yapı Blog</h1>
<div class="blog-grid">
  <a href="akilli-ev-sistemleri.html">Akıllı Ev Sistemleri</a>
  <a href="aluminyum-sistemler.html">Alüminyum Sistemler</a>
  <a href="surme-dogramalar.html">Sürme Doğramalar</a>
</div>
</body>
</html>
```

---

## 7. ÜRÜN GÖRSELLERİ ORGANİZASYONU

### Adımlar:

#### A) Python Script ile (Otomatik):

```bash
cd C:\Users\Admin\Desktop\TOZYAPIWEB\Web
python organize-product-images.py
```

**Otomatik olarak:**
- Tüm ürün görsellerini bulur
- Kategori bazlı klasörlere ayırır
- `assets/images/products/` klasörüne kopyalar

#### B) Manuel Organizasyon:

**Klasör Yapısı:**

```
assets/images/products/
├── kapi-sistemleri/
│   ├── akustik-kapilar/
│   ├── otomatik-kapilar/
│   └── garaj-kapilari/
├── kepenk-sistemleri/
│   ├── aluminyum-kepenk/
│   ├── seffaf-kepenk/
│   └── katanir-kepenk/
├── panjur-sistemleri/
├── pergola-bioclimatic/
└── ...
```

#### C) Online Mağaza Entegrasyonu:

**Online Mağaza'da ürün görsellerini güncelle:**

```javascript
// productsDB içindeki image path'lerini güncelle
const productsDB = [
  {
    id: 1,
    name: "Cuppon 2 Tuşlu Kumanda",
    image: "../assets/images/products/kumandalar/cuppon-2btn.webp",
    ...
  }
];
```

### Optimizasyon:

```bash
# Tüm ürün görsellerini WebP'ye çevir
python optimize-products.py  # (benzer script oluştur)
```

---

## ✅ TAMAMLAMA KONTROL LİSTESİ

### SSL:
- [ ] cPanel'de SSL aktif
- [ ] .htaccess HTTPS yönlendirmesi açık
- [ ] https://www.tozyapi.com.tr çalışıyor
- [ ] SSL Labs testi: A+

### Görsel Optimizasyonu:
- [ ] 6 büyük PNG WebP'ye çevrildi
- [ ] HTML'de picture tag kullanıldı
- [ ] Toplam boyut %80+ azaldı

### .htaccess:
- [ ] Sunucuya yüklendi
- [ ] Permissions: 644
- [ ] Güvenlik kuralları aktif

### Favicon:
- [ ] 6 favicon dosyası oluşturuldu
- [ ] index.html'e eklendi
- [ ] Tüm tarayıcılarda görünüyor

### Google Analytics:
- [ ] Measurement ID alındı (G-XXXXXXXXXX)
- [ ] Tracking kodu eklendi
- [ ] Realtime raporu çalışıyor
- [ ] Event tracking aktif

### Blog:
- [ ] 3 blog yazısı HTML'e dönüştürüldü
- [ ] blog-template.html kullanıldı
- [ ] Görseller optimize edildi
- [ ] Internal linking eklendi

### Ürün Görselleri:
- [ ] assets/products/ klasörü oluşturuldu
- [ ] Kategorilere ayrıldı
- [ ] Online Mağaza güncellendi
- [ ] WebP optimizasyonu yapıldı

---

## 📊 PERFORMANS METRİKLERİ

### Hedefler:

| Metrik | Önce | Sonra | İyileştirme |
|--------|------|-------|-------------|
| **Sayfa Boyutu** | ~2 MB | ~500 KB | %75 |
| **Yükleme Süresi** | 5-8 sn | 1-2 sn | %75 |
| **Görsel Boyutu** | ~100 MB | ~15 MB | %85 |
| **SEO Score** | ?/100 | 90+/100 | +? |
| **Security** | C | A+ | +2 grade |

### Test Araçları:

- **PageSpeed Insights:** pagespeed.web.dev
- **GTmetrix:** gtmetrix.com
- **SSL Labs:** sslabs.com/ssltest
- **Security Headers:** securityheaders.com

---

## 🆘 SORUN GİDERME

### Problem: SSL çalışmıyor

**Çözüm:**
```
1. DNS yayılımını bekle (24-48 saat)
2. Mixed content kontrolü (DevTools Console)
3. Cache temizle
```

### Problem: WebP desteklenmiyor

**Çözüm:**
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Fallback">
</picture>
```

### Problem: Analytics veri gelmiyor

**Çözüm:**
```
1. 24-48 saat bekle
2. Tracking ID doğru mu kontrol et
3. AdBlock devre dışı bırak
4. Realtime raporu kontrol et
```

---

## 📞 DESTEK

**Toz Yapı Teknolojileri**
- 📍 Bilkent Center AVM No:3, Çankaya/Ankara
- 📱 +90 536 773 14 04
- ✉️ merhaba@tozyapi.com.tr
- 🌐 www.tozyapi.com.tr

**Teknik Dokümantasyon:**
- `SSL_KURULUM_REHBERI.md`
- `GOOGLE_ANALYTICS_KURULUMU.md`
- `HERO_IMAJLARI_DURUMU.md`
- `GUVENLIK_RAPORU.md`

---

**Son Güncelleme:** 2026-03-22  
**Durum:** ✅ Tüm araçlar ve rehberler hazır  
**Sıradaki:** Adımları sırayla uygula!
