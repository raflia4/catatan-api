import json
import os

from fastapi import FastAPI, HTTPException

app = FastAPI()

NAMA_FILE = "catatan.json"

def muat():
    if os.path.exists(NAMA_FILE):
        try:
            with open(NAMA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            os.replace(NAMA_FILE, "catatan_rusak.json")
            print("file rusak, mulai dari kosong")
    return[]

def simpan(data):
    with open (NAMA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.get("/sapa")
def halo():
    return {"pesan": "halo semua"}
@app.get("/tentang")
def tentang():
    return {"nama": "API Catatan", "versi": "1.0"}

@app.get("/catatan")
def lihat_catatan():
    return muat()

@app.post("/catatan")
def tambah_catatan (teks: str):
    catatan = muat()
    catatan.append(teks)
    simpan(catatan)
    return {"pesan": "tersimpan", "total": len(catatan)}

@app.delete("/catatan/{nomor}")
def hapus_catatan(nomor: int):
    catatan = muat()
    if nomor < 1 or nomor > len(catatan):
        raise HTTPException(
            status_code=404,
            detail=f"catatan nomor {nomor} tidak di temukan"
        )

    indeks = nomor - 1
    teks_terhapus = catatan.pop(indeks)
    simpan(catatan)

    return {
        "pesan": "catatan dihapus",
        "teks_terhapus": teks_terhapus,
        "total": len(catatan)
    }

@app.put("/catatan/{nomor}")
def ubah_catatan(nomor: int, teks: str):
    catatan = muat()
    if nomor < 1 or nomor > len(catatan):
        raise HTTPException (status_code=404, detail=f"catatan nomor {nomor} tidak ditemukan")
    teks_lama =catatan [ nomor - 1]
    catatan [nomor -1 ] = teks
    simpan(catatan)

    return {"pesan": "diubah", "teks_lama": teks_lama, "teks_baru": teks}