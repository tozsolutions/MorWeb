@echo off
REM TOZ YAPI - GÖRSEL OPTİMİZASYON SCRIPTİ (Windows)
REM Büyük PNG dosyalarını WebP formatına çevirir

echo ========================================
echo TOZ YAPI - GORSEL OPTIMIZASYONU
echo ========================================
echo.

REM Gerekli araclar kontrolü
where cwebp >nul 2>nul
if %errorlevel% neq 0 (
    echo HATA: cwebp araci bulunamadi!
    echo.
    echo Lutfen WebP aracini yukleyin:
    echo https://developers.google.com/speed/webp/download
    echo.
    pause
    exit /b 1
)

echo WebP araci bulundu, optimizasyon basliyor...
echo.

cd "C:\Users\Admin\Desktop\TOZYAPIWEB\Web\assets\images\hero"

REM Optimize edilecek dosyalar
set FILES=hero-kapi-pencere-dograma.png hero-bahce-cit.png hero-havuz-kapama.png hero-sundurma-carport.png hero-akilli-cam.png hero-giyotin.png

echo Optimize edilecek dosyalar:
echo - hero-kapi-pencere-dograma.png (5.9 MB)
echo - hero-bahce-cit.png (5.3 MB)
echo - hero-havuz-kapama.png (4.6 MB)
echo - hero-sundurma-carport.png (3.1 MB)
echo - hero-akilli-cam.png (1.6 MB)
echo - hero-giyotin.png (1.6 MB)
echo.
echo Toplam tasarruf hedefi: ~22 MB -^> ~3 MB (%%86 azalma)
echo.

for %%f in (%FILES%) do (
    if exist "%%f" (
        echo [ISLENİYOR] %%f
        cwebp -q 85 "%%f" -o "%%~nf.webp"
        if exist "%%~nf.webp" (
            echo [BASARILI] %%~nf.webp olusturuldu
        ) else (
            echo [HATA] %%f donusumu basarisiz
        )
        echo.
    ) else (
        echo [ATLANDI] %%f bulunamadi
        echo.
    )
)

echo ========================================
echo OPTIMIZASYON TAMAMLANDI
echo ========================================
echo.
echo Olusturulan WebP dosyalari:
dir *.webp /B
echo.
echo Orijinal dosyalar korundu, isterseniz silebilirsiniz.
echo.
pause
