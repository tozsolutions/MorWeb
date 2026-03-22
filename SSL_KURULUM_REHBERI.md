# 🔒 SSL SERTİFİKASI KURULUM REHBERİ

**Toz Yapı Teknolojileri**  
**Tarih:** 2026-03-22

---

## 📋 GENEL BAKIŞ

Bu rehber, Toz Yapı web sitesi için SSL sertifikası kurulumunu adım adım açıklar.

### Hedef:
```
HTTP (Güvensiz) → HTTPS (Güvenli)
http://www.tozyapi.com.tr → https://www.tozyapi.com.tr
```

---

## 🎯 YÖNTEM 1: LET'S ENCRYPT (ÜCRETSİZ - ÖNERİLEN)

### Gereksinimler:
- ✅ Hosting hesabı (cPanel/Plesk)
- ✅ Domain sahipliği (tozyapi.com.tr)
- ✅ SSH erişimi (opsiyonel, kolay kurulum için)

### Adım 1: Hosting Panelinden Kurulum (En Kolay)

#### cPanel Kullanıcıları İçin:

1. **cPanel'e Giriş Yap**
   ```
   https://your-hosting.com:2083/cpanel
   Kullanıcı: tozyapi
   Şifre: ********
   ```

2. **SSL/TLS Bölümüne Git**
   - Ana sayfada "Security" bölümünü bul
   - "SSL/TLS" ikonuna tıkla

3. **Let's Encrypt SSL Seç**
   ```
   SSL/TLS Status → Manage SSL sites
   ↓
   tozyapi.com.tr seç
   ↓
   "Run AutoSSL" butonuna tıkla
   ```

4. **Bekle ve Doğrula**
   - Kurulum 5-10 dakika sürer
   - Yeşil kilit işareti görünür

#### Plesk Kullanıcıları İçin:

1. **Plesk Panel Giriş**
   ```
   https://your-hosting.com:8443
   ```

2. **Let's Encrypt Eklentisi**
   ```
   Domains → tozyapi.com.tr
   ↓
   Let's Encrypt sekmesi
   ↓
   "Get It Free" butonuna tıkla
   ```

3. **Sertifika Ayarları**
   ```
   ✓ Secure tozyapi.com.tr
   ✓ Secure www.tozyapi.com.tr
   Email: merhaba@tozyapi.com.tr
   ```

---

### Adım 2: .htaccess HTTPS Yönlendirmesi

**.htaccess dosyasını düzenle:**

```apache
# HTTPS ZORUNLU YAPMAK İÇİN BU SATIRLARI AÇIN (.htaccess içinde)

<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</IfModule>
```

**Mevcut .htaccess dosyanızda bu satırlar zaten var, sadece yorumdan çıkarın!**

---

### Adım 3: Kurulum Doğrulama

#### Tarayıcıda Kontrol:
1. Chrome'da aç: `https://www.tozyapi.com.tr`
2. Adres çubuğunda 🔒 kilidi gör
3. "Secure" yazısını kontrol et

#### Online Araçlar:
- **Why No Padlock?** - whynopadlock.com
- **SSL Labs Test** - sslabs.com/ssltest
- **Jitbit SSL Checker** - jitbit.com/sslcheck

**Beklenen Sonuç:**
```
✓ Valid SSL Certificate
✓ Certificate Authority: Let's Encrypt
✓ Expires: 90 gün sonra (otomatik yenilenir)
✓ Grade: A+
```

---

## 🛠️ YÖNTEM 2: MANUEL KURULUM (SSH ile)

### Gereksinimler:
- SSH erişimi
- Root/Admin yetkisi
- Certbot yüklü

### Komutlar:

```bash
# 1. Certbot yükle
sudo apt-get update
sudo apt-get install certbot python3-certbot-apache

# 2. Sertifika al
sudo certbot --apache -d tozyapi.com.tr -d www.tozyapi.com.tr

# 3. Email gir (merhaba@tozyapi.com.tr)
# 4. Terms of Service kabul et (Y)
# 5. Newsletter aboneliği (N)

# 6. Otomatik yönlendirme sorulursa: 2 (Redirect)
```

### Otomatik Yenileme Kontrolü:

```bash
# Certbot otomatik yenileme kontrolü
sudo systemctl status certbot.timer

# Manuel test
sudo certbot renew --dry-run
```

---

## ⚙️ YÖNTEM 3: HOSTING SAĞLAYICI ÜZERİNDEN

### Popüler Sağlayıcılar:

#### Turhost:
```
1. Müşteri paneli → Hosting Yönetimi
2. SSL Sertifikaları → Let's Encrypt
3. "Aktif Et" butonuna tıkla
4. 10 dakika bekle
```

#### Güzel Hosting:
```
1. cPanel → Security → SSL/TLS
2. "Manage SSL sites"
3. Domain seç → AutoSSL çalıştır
```

#### Natro:
```
1. Hosting Yönetim Paneli
2. Uygulamalar → SSL Sertifikası
3. Let's Encrypt → Kur
```

#### İsimtescil:
```
1. Hosting → SSL Yönetimi
2. Ücretsiz SSL → Aktif et
3. Onayla
```

---

## 🔧 KURULUM SONRASI AYARLAR

### 1. Mixed Content Düzeltme

**Sorun:** HTTPS sayfasında HTTP kaynaklar

**Çözüm:** index.html'de tüm URL'leri güncelle

```html
<!-- ÖNCE (Hatalı) -->
<script src="http://cdn.example.com/script.js"></script>

<!-- SONRA (Doğru) -->
<script src="https://cdn.example.com/script.js"></script>
<!-- veya -->
<script src="//cdn.example.com/script.js"></script>
```

**Toz Yapı için durum:** ✅ Tüm kaynaklar relative path, sorun yok!

---

### 2. Search Console Güncelleme

```
1. Google Search Console'a git
2. HTTPS property ekle: https://www.tozyapi.com.tr
3. Sitemap gönder: https://www.tozyapi.com.tr/sitemap.xml
4. HTTP property'den redirect ayarla
```

---

### 3. Analytics Güncelleme

```
1. Google Analytics → Admin
2. Property Settings
3. Default URL: https://www.tozyapi.com.tr olarak değiştir
```

---

### 4. Social Media Update

**Facebook/Instagram:**
```
Profil → Website → https://www.tozyapi.com.tr
```

**Google My Business:**
```
Bilgi → Web sitesi → HTTPS olarak güncelle
```

---

## 📊 SSL SERTİFİKASI DETAYLARI

### Let's Encrypt Özellikleri:

| Özellik | Değer |
|---------|-------|
| **Tip** | Domain Validation (DV) |
| **Geçerlilik** | 90 gün |
| **Yenileme** | Otomatik (60 günde bir) |
| **Domain** | tozyapi.com.tr + www |
| **Wildcard** | Hayır (*.tozyapi.com.tr yok) |
| **Fiyat** | Ücretsiz |

### Sertifika Bilgileri:

```
Issued To: tozyapi.com.tr
Issued By: Let's Encrypt Authority X3
Valid From: [Bugünün tarihi]
Valid Until: [90 gün sonrası]
Key Size: 2048 bit
Signature Algorithm: SHA-256 with RSA
```

---

## ⚠️ SORUN GİDERME

### Problem 1: Sertifika Yüklenmiyor

**Sebep:** DNS henüz yayılmamış

**Çözüm:**
```bash
# DNS kontrolü
nslookup tozyapi.com.tr
dig tozyapi.com.tr

# Nameserver'lar doğru mu?
tozyapi.com.tr → ns1.your-hosting.com
tozyapi.com.tr → ns2.your-hosting.com
```

---

### Problem 2: Mixed Content Warning

**Sebep:** Sayfada HTTP kaynaklar var

**Çözüm:**
```
Chrome DevTools → Console → Mixed Content hatalarını gör
↓
index.html'de ilgili satırları bul
↓
http:// yerine https:// kullan
```

---

### Problem 3: Redirect Loop

**Sebep:** Çift yönlendirme hatası

**Çözüm:**
```apache
# .htaccess'i kontrol et
# Birden fazla RewriteRule olmasın

# Sadece bu olsun:
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

---

### Problem 4: Eski HTTP Bağlantılar

**Çözüm:** Cloudflare kullan

```
1. Cloudflare hesabı oluştur (ücretsiz)
2. tozyapi.com.tr domainini ekle
3. Nameserver'ları değiştir
4. SSL/TLS → Full (Strict) seç
5. Always Use HTTPS → Aktif et
```

---

## 🎯 BAŞARI KRİTERLERİ

Kurulum başarılı olduğunda:

- ✅ `https://www.tozyapi.com.tr` açılıyor
- ✅ Tarayıcıda 🔒 kilit simgesi var
- ✅ "Secure" yazısı görünüyor
- ✅ SSL Labs testi: A+ notu
- ✅ Mixed content hatası yok
- ✅ Tüm sayfalar HTTPS'e yönlendiriyor

---

## 📞 DESTEK

### Hosting Sağlayıcı İletişim:

**Turhost:**
- 📞 0850 885 12 12
- 💬 support@turhost.com

**Güzel Hosting:**
- 📞 0850 755 12 12
- 💬 destek@guzel.net.tr

**Natro:**
- 📞 0850 811 12 12
- 💬 bilgi@natro.com

### Let's Encrypt Kaynakları:

- 🌐 letsencrypt.org
- 📖 certbot.eff.org
- 💬 community.letsencrypt.org

---

## ✅ KONTROL LİSTESİ

Kurulum sırasında şunları yap:

- [ ] Hosting panelinde SSL aktif et
- [ ] .htaccess HTTPS yönlendirmesi aç
- [ ] https://www.tozyapi.com.tr test et
- [ ] Mixed content kontrolü yap
- [ ] Google Search Console güncelle
- [ ] Google Analytics URL'sini değiştir
- [ ] Sosyal medya linklerini güncelle
- [ ] SSL Labs testi yap (A+ hedefle)

---

**Son Güncelleme:** 2026-03-22  
**Zorluk:** ⭐⭐☆☆☆ (Orta-Kolay)  
**Tahmini Süre:** 15-30 dakika
