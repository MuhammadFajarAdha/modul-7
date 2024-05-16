# modul-7
def hitung_kecepatan_akhir(kecepatan_awal, percepatan, waktu):
    """Menghitung kecepatan akhir dalam GLBB."""
    kecepatan_akhir = kecepatan_awal + percepatan * waktu
    return kecepatan_akhir

def hitung_jarak(kecepatan_awal, percepatan, waktu):
    """Menghitung jarak yang ditempuh dalam GLBB."""
    jarak = kecepatan_awal * waktu + 0.5 * percepatan * waktu**2
    return jarak

def main():
    n = int(input("Masukkan jumlah inputan: "))
    
    data = []
    
    for i in range(n):
        print(f"\nInput ke-{i+1}:")
        kecepatan_awal = float(input("Masukkan kecepatan awal (m/s): "))
        percepatan = float(input("Masukkan percepatan (m/s^2): "))
        waktu = float(input("Masukkan waktu (s): "))
        
        kecepatan_akhir = hitung_kecepatan_akhir(kecepatan_awal, percepatan, waktu)
        jarak = hitung_jarak(kecepatan_awal, percepatan, waktu)
        
        data.append([kecepatan_awal, percepatan, waktu, kecepatan_akhir, jarak])
    
    print("\nHasil Perhitungan:")
    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Kecepatan Awal", "Percepatan", "Waktu", "Kecepatan Akhir", "Jarak"
    ))
    
    for row in data:
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
            row[0], row[1], row[2], row[3], row[4]
        ))

if __name__ == "__main__":
    main()
