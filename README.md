# API Catatan

API catatan sederhana dengan FastAPI, data disimpan di file JSON.
Versi API dari aplikasi catatan terminal di repo `catatan-cli`.

## Endpoint

| Metode | Alamat | Fungsi |
|---|---|---|
| GET | `/catatan` | Lihat semua catatan |
| POST | `/catatan?teks=...` | Tambah catatan |
| PUT | `/catatan/{nomor}?teks=...` | Ubah catatan |
| DELETE | `/catatan/{nomor}` | Hapus catatan |

## Cara menjalankan

```powershell
py -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Buka `http://127.0.0.1:8000/docs` untuk mencoba semua endpoint.