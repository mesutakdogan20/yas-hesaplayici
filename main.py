"""
Yas Hesaplayici
Dogum tarihinizden bugune kadar gecen sureyi hesaplar.
"""

from datetime import datetime


def yas_hesapla(dogum_tarihi: datetime) -> dict:
    """Dogum tarihinden bugune kadar gecen sureyi hesaplar."""
    bugun = datetime.now()
    
    # Yil farki
    yil = bugun.year - dogum_tarihi.year
    
    # Ay ve gun ayarlama
    ay = bugun.month - dogum_tarihi.month
    gun = bugun.day - dogum_tarihi.day
    
    if gun < 0:
        ay -= 1
        gun += 30  # Yaklasik
    
    if ay < 0:
        yil -= 1
        ay += 12
    
    # Toplam gun
    toplam_gun = (bugun - dogum_tarihi).days
    
    return {
        "yil": yil,
        "ay": ay,
        "gun": gun,
        "toplam_gun": toplam_gun
    }


def main():
    print("=" * 45)
    print("           YAS HESAPLAYICI")
    print("=" * 45)
    
    tarih_str = input("\nDogum tarihini gir (GG.AA.YYYY): ")
    
    try:
        dogum = datetime.strptime(tarih_str, "%d.%m.%Y")
    except ValueError:
        print("\nHata: Tarih formati yanlis. Ornek: 15.03.1990")
        return
    
    sonuc = yas_hesapla(dogum)
    
    print("\n" + "-" * 45)
    print(f"Yasin: {sonuc['yil']} yil, {sonuc['ay']} ay, {sonuc['gun']} gun")
    print(f"Toplam: {sonuc['toplam_gun']:,} gun yasamissin")
    print("-" * 45)


if __name__ == "__main__":
    main()