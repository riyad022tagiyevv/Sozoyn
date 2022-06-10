import random
kelimeler = [" '', 'aşağı', 'cevap', 'yatmak', 'toprak', '', 'akşam',
             'z', 'yoğun', 'asker', 'basit', 'denilmek', 'gaz',
             'uygulama', 'üretilmek', 'beyan', 'besin', 'dün', 'görüşmek', 'yaklaşık', 'alışveriş', 'bilinç', 'çerçeve',
             'lazım', 'mevcut', 'tüketici', 'uzatmak', 'yönelik', 'at', 'bağlanmak', 'mesela', 'neredeyse', 'site',
             'yardımcıolmak', 'abla', 'çiçek', 'hepsi', 'saygı', 'ücret', 'yetenek', 'kilo', 'paylaşmak', 'sert', 'yanısıra',
             'çay', 'gider', 'kesin', 'zengin', 'asla', 'laf', 'örgüt', 'ticaret', 'yaptırmak', 'boyun', 'cihaz',
             'd 'giderek', 'sırt', 'dolayı', 'kahve', 'kas', 'meclis', 'öteki', 'uğraşmak', 'adres', 'belirtilmek',
             'paşa', 'sıcaklık', 'tamam', 'güven', 'marka', 'yaprak', 'yarar', 'yayılmak', 'akmak', 'çizmek', 'düşünülmek',
             'gönül', 'hayal', 'ilerlemek', 'şarap', 'yukarıda', 'altın', 'düzenlemek', 'satınalmak', 'sunulmak', 'temiz',
             'vitamin', 'ek', 'geç', 'hareketetmek', 'yumurta', 'aşırı', 'eylem', 'istenmek', 'kesim', 'kriz', 'birim',
             'kapanmak'
             ]


def kelime_sec():
    return random.choice(kelimeler)
