# =====================================================================
# 1. İLKİN DƏYİŞƏNLƏR VƏ TİPLƏR (Variables & Types)
# =====================================================================
magaza_adi: str = "Araz Supermarket"
musteri_adi: str = "Elnur"
musteri_balansi: float = 45.00

# Müştərinin səbətindəki məhsulların ilkin qiymətləri
sebetdeki_mehsullar = [1.50, 5.50, 12.0, 22.0]


# =====================================================================
# 2. YADDAŞA QƏNAƏT (Generator Expression)
# =====================================================================
# Məhsullara tək-tək ID paylayacaq yumru mötərizəli generatorumuz:
id_generatoru = (kod for kod in range(1, 100000))


# =====================================================================
# 3. DEKORATOR (Decorators)
# =====================================================================
# Qəbzin alt və üst bəzək xətlərini avtomatik çəkən funksiya:
def qebz_bezek(funksiya):
    def icra_et(*args, **kwargs):
        print("\n========= QƏBZ =========")
        neticet = funksiya(*args, **kwargs)
        print("=======================")
        return neticet
    return icra_et


# =====================================================================
# 4. ƏSAS FUNKSİYA STRUKTURU (Type Hints, *args, **kwargs)
# =====================================================================
@qebz_bezek
def sebeti_hesabla(
    magaza: str, 
    musteri: str, 
    balans: float, 
    *qiymetler: float, 
    **elave_info: str
) -> None:
    
    print(f"Mağaza: {magaza}")
    print(f"Müştəri: {musteri}")
    
    # Müştərinin əlavə kart və tarix məlumatlarını (kwargs) ekrana çıxar:
    for kalit, deyer in elave_info.items():
        print(f"{kalit.capitalize()}: {deyer}")
    print("-" * 24)

    # -----------------------------------------------------------------
    # 👇 SƏNİN NÖVBƏN! (Daxili Məntiqi Sən Yaz)
    # -----------------------------------------------------------------
    # TAPŞIRIQ 1: 'qiymetler' siyahısından istifadə edərək List Comprehension yaz.
    # Qiyməti 10 AZN-dən çox olanlara 10% endirim et (qiymet * 0.9). Yeni siyahı yarat.

    qiymetler=[i*0.9 if i>=10 else i for i in sebetdeki_mehsullar]
    print(qiymetler)
    print("-" * 24)
    
    
    # TAPŞIRIQ 2: Bir dövr (for loop) qur və yeni siyahıdakı qiymətləri topla.
    # Hər dövrdə 'next(id_generatoru)' çağıraraq hər məhsulun ID-sini ekrana yaz.

    umumi_mebleg = 0.0

    for qiymet in qiymetler:
        mehsul_id = next(id_generatoru)
        print(f"{mehsul_id}  {qiymet}")
        umumi_mebleg+=qiymet

    print(str(umumi_mebleg)+" AZN")
   

    
    # TAPŞIRIQ 3: Yekun məbləği tapdıqdan sonra if/else şərti yaz.
    # Əgər məbləğ balansdan çoxdursa "Balansda kifayət qədər vəsait yoxdur!" yaz,
    # azdırsa satışı təsdiqlə və qalıq pulu göstər.

    if umumi_mebleg > balans:
        print("Balansda kifayət qədər vəsait yoxdur!")
    else:
        qaliq = balans - umumi_mebleg
        print(f"{int(qaliq*100)/100} Satış təsdiqləndi!")
    
    pass # Bu 'pass' sözünü silib yerinə kodlarını yaza bilərsən


# =====================================================================
# KODU İŞƏ SALMAQ ÜÇÜN ÇAĞIRIŞ
# =====================================================================
# Sən yuxarıdakı boşluğu doldurandan sonra bu funksiya işə düşəcək:
sebeti_hesabla(
    magaza_adi, 
    musteri_adi, 
    musteri_balansi, 
    *sebetdeki_mehsullar, 
    kart="Bonus", 
    tarix="2026"
)