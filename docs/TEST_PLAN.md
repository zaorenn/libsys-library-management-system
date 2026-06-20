# Lumina Test Planı

Bu belge otomatik testlerin kapsamını ve teslim öncesi uygulanacak kısa arayüz kontrolünü tanımlar.

## Otomatik test kapsamı

`pytest -q` komutu aşağıdaki risk alanlarını gerçek ve geçici bir SQLite veritabanı üzerinde doğrular:

| Alan | Doğrulanan davranış |
|---|---|
| Veritabanı | Foreign key etkinliği, şema sürümü, trigger varlığı ve `integrity_check` |
| Kimlik doğrulama | bcrypt hash, doğru/yanlış parola, onay bekleyen hesap, büyük-küçük harf duyarsız e-posta |
| Validasyon | E-posta, güçlü parola, telefon, ISBN, yayın yılı ve kopya sayısı |
| Kitap CRUD | Ekleme, okuma, güncelleme, arşivleme, benzersiz ISBN ve kapak URL koruması |
| Üye CRUD | Kayıt, onay, giriş ve güvenli arşivleme |
| Ödünç akışı | Stok azaltma/artırma, çift iade koruması, aynı kitabı tekrar alma engeli ve 3 kitap sınırı |
| Veri bütünlüğü | Stok dışı doğrudan SQL eklemesini trigger ile reddetme |
| Gecikme | Geciken gün başına 5 TL ceza hesabı |
| Talepler | Tekrarlanan kitap/profil talebi ve e-posta çakışması |
| Bildirim | Bildirimin yalnız sahibi tarafından okundu işaretlenebilmesi |

## Manuel arayüz duman testi

Teslim öncesinde şu akışlar iki uygulamada bir kez uygulanır:

1. `python main.py` ile katalog açılır; arama, tema değişimi ve ziyaretçi görünümü kontrol edilir.
2. Demo üye ile giriş yapılır; kitap alınır, profil ekranında görülür ve iade edilir.
3. `python admin_app.py` ile yönetici girişi yapılır.
4. Kitap ekleme, düzenleme ve arşivleme akışı kontrol edilir.
5. Üye onayı, kitap isteği ve profil talebi ekranları açılır.
6. Pencere 960×680 ile 1920×1080 aralığında yeniden boyutlandırılır; kritik kontrollerin erişilebilir kaldığı doğrulanır.

## Kabul ölçütleri

- `pytest -q`: tüm testler başarılı.
- `ruff check .`: sıfır hata/uyarı.
- `python -m compileall -q .`: sözdizimi hatası yok.
- `PRAGMA integrity_check`: `ok`.
