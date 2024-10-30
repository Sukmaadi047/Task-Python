Dokumentasi **proyek gRPC**

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

## Contoh Penggunaan

Setelah server Django dan gRPC berjalan, jalankan client untuk melihat output berikut:

```bash
Detail Pengguna:
ID: 1
Nama: Alice
Email: alice@example.com
```

## Troubleshooting

1. **Pastikan kedua server (Django dan gRPC) sudah berjalan**.  
   - Gunakan terminal terpisah untuk menjalankan masing-masing layanan.

2. **Verifikasi aktivasi virtual environment**:
   - Jika ada dependensi yang hilang, pastikan Anda berada di virtual environment yang benar.

3. **Mengatasi error umum**:
   - Jika port sudah terpakai, coba jalankan server pada port yang berbeda:
     ```bash
     python manage.py runserver 8001
     python grpc_server.py --port=50052
     ```
