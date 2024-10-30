# **Dokumentasi**

# **GRPC Project**
## Langkah-Langkah Instalasi

1. **Kloning repositori**:
   ```bash
   git clone <repository-url>
   cd grpc_project
   ```

2. **Buat dan aktifkan virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Pada Windows: venv\Scripts\activate
   ```

3. **Instal dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan server Django**:
   ```bash
   python manage.py runserver 8000
   ```

5. **Jalankan server gRPC**:
   ```bash
   python grpc_server.py
   ```

6. **Uji Client gRPC**:

   Pada terminal terpisah, aktifkan virtual environment dan jalankan:

   ```bash
   python grpc_client.py
   ```

   Client akan memanggil layanan untuk mengambil data pengguna dan menampilkannya di konsol.

## Struktur Proyek

```
grpc_project/
│
├── grpc_server.py        # Server gRPC
├── grpc_client.py        # Client gRPC untuk pengujian
├── proto/                # Definisi Protobuf
│   └── user.proto
├── users/                # Aplikasi Django untuk data pengguna
│   ├── models.py         # Model pengguna
│   ├── views.py          # View API
│   └── serializers.py    # Serialisasi data
├── grpc_project/         # Pengaturan proyek Django
│   ├── settings.py       # File konfigurasi
│   ├── urls.py           # Routing URL
└── requirements.txt      # Dependensi Python
```

# **SSO Service menggunakan Django Rest Framework dengan JWT**  

## **Arsitektur**  
- **Backend:** Django Rest Framework untuk API REST.
- **JWT Authentication:** Token JWT digunakan untuk menjaga sesi pengguna dan otorisasi permintaan.
- **Modular Service:** Layanan ini berdiri sendiri untuk SSO, memisahkan otentikasi dari layanan utama.
- **Stateless Authentication:** Karena JWT, tidak ada status sesi yang disimpan di server, sehingga membuat aplikasi lebih ringan dan scalable.  
- **Keamanan:** Token JWT dienkripsi untuk mencegah pemalsuan, dan token memiliki waktu kedaluwarsa yang dikontrol.

---

## **Fitur Utama**  
1. **Login**: Pengguna dapat melakukan login dan menerima JWT token.  
2. **Protected Routes**: Beberapa endpoint hanya bisa diakses dengan JWT yang valid.  
3. **Verifikasi Token**: Otomatis memverifikasi token JWT untuk akses aman.  

---

## **Cara Menjalankan Proyek**  

### **1. Kloning Repository**  
```bash
   git clone <repository-url>
   cd sso_service
```

### **2. Buat dan Aktifkan Virtual Environment**  
**Windows:**  
```bash
python -m venv venv
venv\Scripts\activate
```
**Linux/Mac:**  
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Instal Dependensi**  
```bash
pip install -r requirements.txt
```

### **4. Jalankan Server**  
```bash
python manage.py runserver 8000 --settings=sso_service.settings
```

Server akan aktif di:  
```
http://127.0.0.1:8000
```

---

## **Cara Penggunaan API**  

### **1. Mendapatkan Token JWT**  
Gunakan perintah berikut untuk login dan mendapatkan token JWT:  
```bash
curl --noproxy "*" -X POST http://127.0.0.1:8000/api/login/ -d "username=alice&password=12345678"
```

Jika berhasil, respons akan berisi token JWT:  
```json
{
    "access": "<jwt-access-token>",
    "refresh": "<jwt-refresh-token>"
}
```

### **2. Mengakses Endpoint Terproteksi dengan JWT**  
Gunakan token JWT untuk mengakses route yang membutuhkan otentikasi:  
```bash
curl --noproxy "*" -X POST http://127.0.0.1:8000/api/token/verify/ -H "Content-Type: application/json" -d "{\"token\": \"<jwt-access-token>\"}"

```

# **Hash Password**
## **Cara Kerja Hash Password**
Hash password adalah proses konversi password menjadi string acak yang tidak dapat dibaca. Proses ini melibatkan beberapa langkah:
### **1. Pembuatan Salt:** Salt adalah data acak yang ditambahkan ke password sebelum hashing untuk mencegah serangan rainbow table.
### **2. Hashing:** Password digabungkan dengan salt dan di-hash menggunakan algoritma tertentu (dalam hal ini, PBKDF2).
### **3. Penyimpanan:** Hasil hash dan salt disimpan dalam database.

## **Alasan Menggunakan PBKDF2**
### **Keamanan:** PBKDF2 dirancang untuk mengatasi serangan brute-force dengan memperlambat proses hashing melalui penggunaan iterasi yang tinggi.
### **Standardisasi:** PBKDF2 adalah standar hashing yang diakui, yang diimplementasikan secara luas dalam berbagai platform dan framework.
