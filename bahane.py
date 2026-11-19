#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VAROLUŞSAL KRİZ BAHANE ÜRETİCİSİ
Dünyanın en ciddi olmayan en ciddi programı.
Güncellendi: Daha absürt bahaneler eklendi.
"""

import random
import time

bahaneler = [
    "çünkü bugün kuantum çoraplarım birbirleriyle tartışıyordu ve ben arabuluculuk yaptım",
    "çünkü çay bardağım bana 'sen de bir gün buhar olacaksın' dedi ve ben bunu sindiremedim",
    "çünkü klavye tuşlarım varoluşsal kriz geçiriyordu ve onlara terapi uyguladım",
    "çünkü bilgisayarımın fanı 'ben de yoruluyorum' diye ağladı ve ben onu teselli ettim",
    "çünkü mouse'um kayboldu ve ben onu ararken kendi varlığımı sorguladım",
    "çünkü internet bağlantım 'bugün anlam yok' dedi ve ben ona hak verdim",
    "çünkü sandalyem 'oturma, kalk, yürü, yaşa' diye felsefe yaptı",
    "çünkü penceremden giren rüzgar bana 'bugün hiçbir şey yapma' diye fısıldadı",
    "çünkü kahve makinem 'sen de bir gün tükeneceksin' dedi ve ben onunla empati kurdum",
    "çünkü takvimimdeki günler birbirine 'biz de anlamsızız' diye şikayet etti",
    "çünkü monitörüm 'ben de senin gibi yoruldum' dedi ve birlikte mola verdik",
    "çünkü USB kablom 'ben de bağlanmak istemiyorum' diye isyan etti"
]

def uret_bahane(is_adi):
    print(f"\n'{is_adi}' işini yapamadın...")
    print("Derin düşünce modu aktif...")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print()
    
    bahane = random.choice(bahaneler)
    print(f"\nResmi Bahane: {is_adi} yapamadım {bahane}.")
    print("\nBu bahane mahkemece geçerli sayılmıştır. (Hayır sayılmamıştır.)")

def main():
    print("=" * 50)
    print("   VAROLUŞSAL KRİZ BAHANE ÜRETİCİSİ v1.1")
    print("   'Neden bugün hiçbir şey yapmadım?' sorusuna cevap")
    print("=" * 50)
    
    is_adi = input("\nYapmadığın işi yaz (boş bırakırsan 'hiçbir şey' kabul edilir): ").strip()
    if not is_adi:
        is_adi = "hiçbir şey"
    
    uret_bahane(is_adi)
    
    print("\nİyi günler dileriz. Ya da dilemeyiz. Zaten her şey anlamsız.")

if __name__ == "__main__":
    main()

# Gizli not: #demokrasibahaneuretecilerebırakilmamali
# (Bu yorum siyasi değildir, sadece kod yorumudur.)
