# 📊 GOOGLE ANALYTICS 4 KURULUM REHBERİ

**Toz Yapı Teknolojileri**  
**Tarih:** 2026-03-22

---

## 🎯 GENEL BAKIŞ

Google Analytics 4 (GA4) ile web sitesi trafiğini, kullanıcı davranışlarını ve dönüşümleri takip edin.

---

## 📝 ADIM 1: GOOGLE ANALYTICS HESABI OLUŞTURMA

### 1.1 Google Hesabı ile Giriş

```
1. analytics.google.com adresine git
2. "Başla" veya "Sign In" butonuna tıkla
3. Google hesabınla giriş yap (veya yeni hesap oluştur)
```

### 1.2 Analytics Hesabı Oluştur

```
Hesap Adı: Toz Yapı Teknolojileri
✓ Veri Paylaşım Ayarları (tümünü işaretle)
→ Sonraki
```

### 1.3 Property Oluştur

```
Property Name: Toz Yapı Web
Reporting Time Zone: Turkey
Currency: Turkish Lira (TRY)
→ Sonraki
```

### 1.4 İşletme Bilgileri

```
Industry Category: Home & Garden / Construction
Business Size: 10-50 employees
→ Sonraki
```

### 1.5 İşletme Hedefleri

```
✓ Online satışlar
✓ Form gönderimleri
✓ Telefon aramaları
✓ Katalog indirmeleri
→ Oluştur
```

---

## 🔧 ADIM 2: DATA STREAM OLUŞTURMA

### 2.1 Web Stream Ekle

```
Admin (⚙️) → Data Streams → Add Stream → Web
```

### 2.2 Website Bilgileri

```
Website URL: https://www.tozyapi.com.tr
Stream Name: Toz Yapı Ana Site
→ Create Stream
```

### 2.3 Measurement ID Al

**ÖNEMLİ:** Bu ID'yi kaydedin!

```
Measurement ID: G-XXXXXXXXXX
(10 karakterli kod, örn: G-A1B2C3D4E5)
```

---

## 💻 ADIM 3: HTML'E KOD EKLEME

### 3.1 Google Tag Manager (ÖNERİLEN)

#### GTM Hesabı Oluştur:

```
1. tagmanager.google.com
2. "Create Account"
3. Account Name: Toz Yapı Teknolojileri
4. Container Name: tozyapi-web
5. Target Platform: Web
```

#### GTM Kodunu Al:

```
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
<!-- End Google Tag Manager -->
```

#### index.html'e Ekle:

**`<head>` bölümünün EN ÜSTÜNE:**

```html
<!DOCTYPE html>
<html lang="tr">
<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){...})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
<!-- End Google Tag Manager -->

<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
...
```

**`<body>` bölümünün EN ÜSTÜNE:**

```html
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<nav>
...
```

---

### 3.2 Direkt GA4 Kodu (Alternatif)

Eğer GTM kullanmak istemiyorsanız, direkt GA4 kodunu kullanın:

```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**index.html `<head>` bölümüne ekleyin.**

---

## 📈 ADIM 4: GELİŞMİŞ TAKİP AYARLARI

### 4.1 Form Takibi (Teklif Formları)

```javascript
// Form submission tracking
document.querySelector('form').addEventListener('submit', function(e) {
  gtag('event', 'form_submit', {
    'event_category': 'Engagement',
    'event_label': 'Teklif Formu',
    'value': 1
  });
});
```

### 4.2 WhatsApp Tıklama Takibi

```javascript
// WhatsApp link takibi
document.querySelectorAll('a[href*="wa.me"]').forEach(link => {
  link.addEventListener('click', function() {
    gtag('event', 'whatsapp_click', {
      'event_category': 'Contact',
      'event_label': 'WhatsApp Button'
    });
  });
});
```

### 4.3 Telefon Tıklama Takibi

```javascript
// Telefon link takibi
document.querySelectorAll('a[href^="tel:"]').forEach(link => {
  link.addEventListener('click', function() {
    gtag('event', 'phone_call', {
      'event_category': 'Contact',
      'event_label': 'Phone Number'
    });
  });
});
```

### 4.4 Katalog İndirme Takibi

```javascript
// PDF download tracking
document.querySelectorAll('a[href$=".pdf"]').forEach(link => {
  link.addEventListener('click', function() {
    gtag('event', 'download', {
      'event_category': 'Resources',
      'event_label': 'Catalog PDF',
      'value': 1
    });
  });
});
```

---

## 🛒 ADIM 5: E-TİCARET TAKİBİ (ONLINE MAĞAZA)

### 5.1 Ürün Görüntüleme

```javascript
// Online Mağaza ürün detay sayfası
gtag('event', 'view_item', {
  'currency': 'TRY',
  'value': 299.80,
  'items': [{
    'item_id': 'SKU_12345',
    'item_name': 'Cuppon 2 Tuşlu Kumanda',
    'category': 'Kumandalar',
    'brand': 'Cuppon',
    'price': 299.80,
    'quantity': 1
  }]
});
```

### 5.2 Sepete Ekleme

```javascript
// Sepete ekleme butonu
gtag('event', 'add_to_cart', {
  'currency': 'TRY',
  'value': 299.80,
  'items': [{
    'item_id': 'SKU_12345',
    'item_name': 'Cuppon 2 Tuşlu Kumanda',
    'category': 'Kumandalar',
    'brand': 'Cuppon',
    'price': 299.80,
    'quantity': 1
  }]
});
```

### 5.3 Satın Alma (Checkout)

```javascript
// Sipariş tamamlandığında
gtag('event', 'purchase', {
  'transaction_id': 'T12345',
  'value': 1500.00,
  'currency': 'TRY',
  'items': [{
    'item_id': 'SKU_12345',
    'item_name': 'Cuppon 2 Tuşlu Kumanda',
    'category': 'Kumandalar',
    'brand': 'Cuppon',
    'price': 299.80,
    'quantity': 5
  }]
});
```

---

## 🎯 ADIM 6: HEDEFLER (CONVERSIONS) OLUŞTURMA

### GA4 Admin Panelinde:

```
1. Admin → Conversions
2. "New conversion event"
3. Event name seç:
   - form_submit (Teklif formu)
   - whatsapp_click (WhatsApp tıklama)
   - phone_call (Telefon tıklama)
   - download (Katalog indirme)
4. Mark as conversion
```

### Önemli Hedefler:

| Hedef | Event Name | Değer |
|-------|------------|-------|
| Teklif Formu | `form_submit` | 100 TRY |
| WhatsApp Mesajı | `whatsapp_click` | 50 TRY |
| Telefon Araması | `phone_call` | 75 TRY |
| Katalog İndirme | `download` | 25 TRY |
| Online Satış | `purchase` | Gerçek tutar |

---

## 📱 ADIM 7: GOOGLE SEARCH CONSOLE ENTEGRASYONU

### 7.1 Search Console'a Kayıt

```
1. search.google.com/search-console
2. "Add Property"
3. Domain: tozyapi.com.tr
4. DNS kaydı ile doğrula (TXT record)
```

### 7.2 Analytics ile Bağla

```
Analytics Admin → Property → Product Links
↓
Search Console Link → Connect
↓
tozyapi.com.tr property seç → Submit
```

---

## 🔍 ADIM 8: DOĞRULAMA VE TEST

### 8.1 Realtime Raporu Kontrol

```
1. analytics.google.com
2. Reports → Realtime
3. Yeni sekmede tozyapi.com.tr'yi aç
4. Active users artmalı (1+)
```

### 8.2 Google Tag Assistant (Chrome Extension)

```
1. Chrome Web Store → "Tag Assistant Legacy"
2. Install extension
3. tozyapi.com.tr'yi aç
4. Tag Assistant'ta kontrol et:
   ✓ Google Analytics 4
   ✓ Google Tag Manager (varsa)
   Status: Success
```

### 8.3 Network Tab Kontrolü

```
1. Chrome DevTools → Network
2. tozyapi.com.tr'yi yenile
3. "collect" isteğini ara
4. Payload kontrol et:
   - tid=G-XXXXXXXXXX (Measurement ID)
   - dl=https://www.tozyapi.com.tr (Document location)
```

---

## 📊 ADIM 9: RAPORLAMA VE DASHBOARD

### Önemli Metrikler:

| Metrik | Açıklama | Hedef |
|--------|----------|-------|
| **Users** | Toplam ziyaretçi | 1000+/ay |
| **Sessions** | Toplam oturum | 3000+/ay |
| **Pageviews** | Sayfa görüntüleme | 10,000+/ay |
| **Bounce Rate** | Hemen çıkma oranı | <%50 |
| **Avg. Session** | Ortalama oturum süresi | >2 dakika |
| **Conversions** | Hedef tamamlama | 50+/ay |

### Günlük Kontrol Listesi:

- [ ] Realtime users aktif mi?
- [ ] Dün kaç ziyaretçi vardı?
- [ ] Hangi sayfalar popüler?
- [ ] Conversion rate nedir?
- [ ] Mobil/desktop dağılımı?

---

## 🎨 ADIM 10: TOZ YAPI ÖZEL AYARLARI

### Custom Dimensions Oluştur:

```
Admin → Property → Custom Definitions → Custom Dimensions

1. Product Category
   - Scope: Event
   - Event parameter: item_category

2. Brand
   - Scope: Event
   - Event parameter: brand

3. User Type
   - Scope: User
   - User property: user_type
```

### Custom Reports:

```
Explore → Blank Report

Dimensions:
- Page path
- Event name
- Device category

Metrics:
- Views
- Event count
- Conversions

Filters:
- Event name = form_submit OR whatsapp_click
```

---

## ⚠️ SORUN GİDERME

### Problem 1: Veri Gelmiyor

**Çözüm:**
```
1. Kod doğru yerleştirilmiş mi kontrol et
2. AdBlock kullanıyor musun? (Devre dışı bırak)
3. 24-48 saat bekle (veri işleme süresi)
4. Realtime raporunu kontrol et
```

### Problem 2: Duplicate Tracking

**Çözüm:**
```
1. Birden fazla GA4 kodu var mı kontrol et
2. GTM + direct code karışımı olmasın
3. Tag Assistant ile test et
```

### Problem 3: Cross-Domain Tracking

**Durum:** Online mağaza farklı domain'de

**Çözüm:**
```javascript
gtag('config', 'G-XXXXXXXXXX', {
  'linker': {
    'domains': ['tozyapi.com.tr', 'shop.tozyapi.com.tr']
  }
});
```

---

## 📞 DESTEK KAYNAKLARI

### Resmi Dokümantasyon:
- 📖 developers.google.com/analytics
- 📖 support.google.com/analytics

### Topluluk:
- 💬 Reddit: r/GoogleAnalytics
- 💬 Stack Overflow: google-analytics-4 tag

### Toz Yapı İletişim:
- 📧 merhaba@tozyapi.com.tr
- 📱 +90 536 773 14 04

---

## ✅ KURULUM KONTROL LİSTESİ

- [ ] Google Analytics hesabı oluştur
- [ ] Property oluştur (G-XXXXXXXXXX al)
- [ ] GTM container oluştur (opsiyonel)
- [ ] Tracking kodunu index.html'e ekle
- [ ] Form tracking ekle
- [ ] WhatsApp tracking ekle
- [ ] Phone tracking ekle
- [ ] E-commerce tracking ekle (online mağaza)
- [ ] Conversions ayarla
- [ ] Search Console bağla
- [ ] Test et (Realtime + Tag Assistant)
- [ ] Custom dimensions oluştur
- [ ] Dashboard oluştur

---

**Son Güncelleme:** 2026-03-22  
**Zorluk:** ⭐⭐⭐☆☆ (Orta)  
**Tahmini Süre:** 30-60 dakika
