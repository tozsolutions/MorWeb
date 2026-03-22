# 🔒 TOZ YAPI WEB - GÜVENLİK RAPORU & ÖNERİLER

**Tarih:** 2026-03-22  
**Hazırlayan:** Sistem Analizi

---

## ⚠️ KRİTİK GÜVENLİK AÇIKLARI

### 1. .env Dosyası Koruması
**Durum:** ❌ KRİTİK - robots.txt'de engelli ama hala erişilebilir!

**Çözüm:**
```apache
# .htaccess dosyasına eklendi:
<FilesMatch "^\.">
    Order allow,deny
    Deny from all
</FilesMatch>
```

**Ekstra Önlem:** `.env` dosyasını `Web/` klasörü dışına taşıyın:
```
TOZYAPIWEB/
├── .env (burada olmalı, Web dışında)
└── Web/
    └── .htaccess (erişimi engelliyor)
```

---

### 2. HTTPS Zorunluluğu
**Durum:** ⚠️ SSL sertifikası kontrol edilmeli

**Çözüm:**
- Hosting sağlayıcınızdan ücretsiz Let's Encrypt SSL alın
- `.htaccess` dosyasındaki HTTPS yönlendirme satırlarını aktif edin

---

### 3. Content Security Policy (CSP)
**Durum:** ✅ `.htaccess` dosyasına eklendi

**Kapsam:**
- XSS saldırılarına karşı koruma
- Inline scriptlere izin (Luna AI için gerekli)
- WhatsApp entegrasyonu için connect-src izni

---

### 4. Clickjacking Koruması
**Durum:** ✅ X-Frame-Options: SAMEORIGIN eklendi

---

### 5. MIME Sniffing Koruması
**Durum:** ✅ X-Content-Type-Options: nosniff eklendi

---

## 📁 KLASÖR YAPISI - EKSİKLER

### Mevcut Yapı
```
TOZYAPIWEB/
├── _DEPLOY_REHBERI/          ✅ Var
├── _PROMPT_ARSIV/            ✅ Var
├── README_ANA_REHBER.txt     ✅ Var
└── Web/                      ✅ Var
    ├── Ana Sayfa/            ✅ Var
    ├── Blog/                 ✅ Var
    ├── Hakkımızda/           ✅ Var
    ├── İletişim/             ✅ Var
    ├── Katalog/              ✅ Var
    ├── Online Mağaza/        ✅ YENİ OLUŞTURULDU
    ├── Referanslar/          ✅ Var
    ├── S.S.S/                ✅ Var
    ├── İş ortaklarımız/      ✅ Var
    ├── Ürün Gruplarımız/     ✅ Var
    ├── index.html            ✅ Var
    ├── sitemap.xml           ✅ GÜNCELLENDİ (95+ URL)
    ├── llms.txt              ✅ GÜNCELLENDİ
    ├── robots.txt            ⚠️ Güvenlik zafiyeti var
    ├── style-store.css       ✅ YENİ (Online Mağaza için)
    └── .htaccess             ✅ YENİ (Güvenlik)
```

### ❌ Eksik Dosyalar

1. **favicon.ico** - Browser sekonu
   - Önerilen boyut: 32x32 veya 16x16
   - Konum: `Web/favicon.ico`

2. **manifest.json** - PWA (Progressive Web App) desteği
   - Mobil uygulama gibi davranma
   - Offline çalışma

3. **404.html** - Özel hata sayfası
   - Kullanıcı dostu 404 sayfası

4. **assets/ klasörü**
   ```
   Web/assets/
   ├── css/
   │   └── style.css (index.html'deki gömülü CSS buraya taşınabilir)
   ├── js/
   │   └── main.js
   └── images/
       ├── products/
       ├── blog/
       └── icons/
   ```

5. **admin/ klasörü** (Eğer yönetim paneli planlanıyorsa)
   - `.htaccess` ile şifre koruması eklenmeli

---

## 🛡️ GÜVENLİK ÖNERİLERİ (ÖNCELİKLİ)

### Acil (1-3 gün içinde yapılmalı)

1. ✅ **.htaccess dosyası yüklendi** - Sunucuya yükleyin
2. ⚠️ **SSL Sertifikası** - Hosting panelden aktif edin
3. ⚠️ **.env dosyasını taşı** - Web root dışına çıkarın
4. ⚠️ **robots.txt güncelle**:
   ```txt
   User-agent: *
   Allow: /
   
   # Hassas dosyalar
   Disallow: /.env
   Disallow: /.git
   Disallow: /.htaccess
   Disallow: /admin/
   Disallow: /*.sql
   Disallow: /*.log
   Disallow: /*.bak
   
   Sitemap: https://www.tozyapi.com.tr/sitemap.xml
   ```

### Orta Öncelik (1-2 hafta)

5. **Rate Limiting** - DDoS koruması
6. **WAF (Web Application Firewall)** - Cloudflare kullanın
7. **Düzenli yedekleme** - Günlük otomatik yedek

### Uzun Vadeli (1 ay)

8. **Security Headers testi** - securityheaders.com ile kontrol
9. **Penetrasyon testi** - Profesyonel güvenlik denetimi
10. **Log monitoring** - Şüpheli aktivite takibi

---

## 📊 ONLINE MAĞAZA ÖZELLİKLERİ

**Konum:** `Web/Online Mağaza/index.html`

### Özellikler:
- ✅ 50+ ürün (Poledoor'dan alındı, %25 kar marjı eklendi)
- ✅ Kategori filtreleme (Kumanda, Motor, Aksesuar, vb.)
- ✅ Arama fonksiyonu
- ✅ Fiyat sıralama (düşükten-yüksekten, vb.)
- ✅ Sepet sistemi
- ✅ Quick View (Hızlı görüntüleme)
- ✅ WhatsApp sipariş entegrasyonu
- ✅ Responsive tasarım
- ✅ Stok durumu gösterimi

### Ürün Kategorileri:
1. Kumandalar (13 ürün)
2. Motorlar & Kontrol Kartları (11 ürün)
3. Aksesuarlar (7 ürün)
4. Panjur (2 ürün)
5. Güvenlik (3 ürün)
6. Bariyer (8 ürün)
7. Kapı Motorları (6 ürün)

### Fiyatlandırma Stratejisi:
- **Maliyet fiyatı:** Poledoor.com fiyatları
- **Satış fiyatı:** Maliyet + %25 kar marjı
- **Görünüm:** İndirimli gösterim (eski fiyat/yeni fiyat)

**Örnek:**
- Cuppon 2 Tuşlu Kumanda
  - Maliyet: 239,84 ₺
  - Satış: 299,80 ₺ (%25 kar)

---

## 🔧 TEKNİK İYİLEŞTİRMELER

### Performans
- [ ] CSS'i ayrı dosyaya taşı (index.html 34KB → ~5KB)
- [ ] JavaScript'i minify et
- [ ] Resimleri WebP formatına çevir
- [ ] Lazy loading ekle (resimler için)

### SEO
- [ ] Meta açıklamaları her sayfaya özel ekle
- [ ] Open Graph tags (sosyal medya paylaşımı)
- [ ] Schema.org structured data (ürünler için)
- [ ] XML sitemap Google Search Console'a ekle

### Erişilebilirlik
- [ ] ARIA labels ekle
- [ ] Klavye navigasyonu test et
- [ ] Renk kontrastını kontrol et

---

## 📈 ANALYTICS & TAKİP

### Kurulması Gerekenler:
1. **Google Analytics 4** - Ziyaretçi analizi
2. **Google Search Console** - SEO performansı
3. **Google Tag Manager** - Etiket yönetimi
4. **Hotjar/Microsoft Clarity** - Kullanıcı davranışı

### E-Ticaret Takibi:
- Sepete ekleme oranları
- Terk edilen sepetler
- Dönüşüm oranları
- En popüler ürünler

---

## ✅ SONUÇ & AKSIYON PLANI

### Tamamlanan:
- ✅sitemap.xml (95+ URL ile genişletildi)
- ✅ llms.txt (tüm ürün kategorileri eklendi)
- ✅ Online Mağaza (50+ ürün, %25 kar marjı)
- ✅ .htaccess (güvenlik ayarları)
- ✅ style-store.css (Online Mağaza stili)

### Acil Yapılacaklar:
1. SSL sertifikası aktif et
2. .env dosyasını Web/ dışına taşı
3. .htaccess'i sunucuya yükle
4. favicon.ico ekle

### Bir Sonraki Adımlar:
1. Admin paneli geliştir (ürün yönetimi için)
2. Ödeme entegrasyonu (Stripe, iyzico)
3. Kargo modülü
4. Müşteri hesap sistemi

---

**İletişim:** merhaba@tozyapi.com.tr  
**Teknik Destek:** Luna AI - 7/24 WhatsApp
