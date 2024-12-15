def hitung_biaya_parkir(jam, jenis_kendaraan):
    tarif_awal = 3000
    tambahan_24_jam = 10000

    # Tarif per jam setelah 2 jam
    if jenis_kendaraan.lower() == "motor":
        tarif_tambahan_per_jam = 1000
    elif jenis_kendaraan.lower() == "mobil":
        tarif_tambahan_per_jam = 1500
    else:
        return "Jenis kendaraan tidak valid. Masukkan 'motor' atau 'mobil'."

    # Menghitung biaya
    if jam <= 2:
        total = tarif_awal
    else:
        total = tarif_awal + (jam - 2) * tarif_tambahan_per_jam

    # Tambahan biaya jika lebih dari 24 jam
    if jam > 24:
        total += tambahan_24_jam

    return total

# Input dari user
try:
    jenis_kendaraan = input("Masukkan jenis kendaraan (Motor/Mobil): ").strip().lower()
    jam_parkir = int(input("Masukkan durasi parkir (jam): "))

    if jam_parkir < 0:
        print("Durasi parkir tidak bisa negatif.")
    else:
        biaya = hitung_biaya_parkir(jam_parkir, jenis_kendaraan)
        if isinstance(biaya, str):
            print(biaya)
        else:
            print(f"Biaya parkir untuk {jenis_kendaraan.capitalize()} selama {jam_parkir} jam adalah: Rp {biaya}")
except ValueError:
    print("Harap masukkan angka yang valid untuk durasi parkir.")
