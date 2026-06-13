## Layihənin Adı: "Ağıllı Market Səbəti" (Smart Basket)

**Ssenari:** Bir supermarket üçün müştərinin səbətini idarə edən, endirimlər tətbiq edən və qəbz çıxaran kiçik bir proqram yazırsan.

İş bölgüsünü elə edək ki, hər mövzu öz yerini tapsın:

### 📑 Tapşırıq Planı:

-   **01\. Dəyişənlər və İdarəetmə (Variables, types, control flow):**
    
    -   Müştərinin adını, balansındakı pulu (`float`) və mağazanın adını dəyişənlərdə saxla.
        
    -   Bir `if/else` şərti yaz: Əgər səbətin ümumi məbləği müştərinin balansından çoxdursa, "Balansda kifayət qədər vəsait yoxdur!" yazsın, azdırsa satışı təsdiqləsin.
        
-   02\. Funksiyalar və Dekorator (Functions, \*args/**kwargs, decorators):**
    
    -   **Decorator:** Bir dənə `@qebz_bezek` adlı dekorator yaz. Bu dekorator istənilən funksiyadan əvvəl ekrana `========= QƏBZ =========` və funksiya bitəndə `=======================` xətlərini çəksin.
        
    -   **\*args və kwargs:** Elə bir funksiya yaz ki, `*args` ilə məhsulların qiymətlərini qəbul etsin, `kwargs` ilə isə müştərinin əlavə məlumatlarını (məsələn: `kart_tipi="Bonus"`, `tarix="2026"`) qəbul edib ekranda göstərsin.
        
-   **03\. Qısaltmalar (List & dict comprehensions):**
    
    -   Əlində bir məhsul siyahısı olsun (məsələn: `[1.20, 5.50, 12.0, 20.0]`).
        
    -   _List Comprehension_ istifadə edərək, qiyməti 10 AZN-dən baha olan məhsullara 10% endirim tətbiq et və yeni siyahı yarat.
        
-   **04\. Yaddaşa qənaət (Generator expressions):**
    
    -   Təsəvvür et marketdə milyon dənə məhsul kodu var. Yumru mötərizədən `()` istifadə edərək bir generator yarat və `next()` funksiyası ilə müştərinin aldığı məhsullara avtomatik unikal ID nömrələri (məsələn: 1, 2, 3...) payla.
        
-   **05\. Tip İpucları (Type hints):**
    
    -   Yazdığın bütün funksiyalarda arqumentlərin və geri qayıdan cavabın tipini mütləq qeyd et (məsələn: `def hesabla(qiymet: float) -> float:`). _Unutma, Pydantic yoxdur, sadəcə ipucu olaraq yazırsan._