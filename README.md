## Giriş

Bu proje boyunca, bir şehir içerisinde bulunan N (20) adet konumun gezilebilmesi için en düşük maliyetli mesafeyi bulma işlemi yapılmıştır diğer bir adıyla Gezgin Satıcı Probleminin Genetik Algoritma ile çözümlenmesi yapılmıştır.


## Amaç

Projenin temel amacı genetik algoritmanın bize sağladığı kromozom-crossover-popülasyon gibi kavramları kullanarak en uygun çözüm (rota)’nın bulunmasıdır. Genetik Algoritmalar optimal olarak çözümler sağlamasa da, Zaman aralığında iyi bir yaklaşım sağlarlar. Özellikle TSP gibi problemlerinin çözümünde fayda sağlarlar.

## Kavramlar

Genetik Algoritma çalışma biçimi ile tamamen seçim, çaprazlama ve mutasyon işlemlerine bağlıdır. 

Gezgin satıcı problemi (TSP-Traveling Salesman Problem) aralarındaki uzaklıkları bilinen n adet noktanın (şehir veya düğüm) her birinden yalnız bir kez geçen en kısa yolu veya en az maliyetli turu bulmayı hedeflemektedir

## Genetik Algoritma Nedir?

Genetik algoritmalar, doğada gözlemlenen evrimsel mekanizmalara benzer mekanizmalar kullanarak çalışan en iyileştirme yöntemidir. Çok boyutlu uzayda belirli bir maliyet fonksiyonuna göre en iyileştirme amacıyla iterasyonlar yapan ve her iterasyonda en iyi sonucu üreten kromozomun hayatta kalması prensibine dayanan en iyi çözümü arama yöntemidir.

Genetik Algoritmanın geleneksel optimizasyon ve arama tekniklerinden farkı şu şekildedir;

•	Parametrelerin kendisi ile değil parametrelerin kodlanmış şekliyle işlem yapmaktadır.
•	Çoğu optimizasyon tekniği tek noktadan arama yaparken GA noktaların popülasyonu üzerine işlem yapar. Arama yaparken tek noktadan ziyade çözümlerin popülasyonu kullanmak optimuma ulaşma şansını artırır ve lokalden kaçmayı sağlar.
•	GA değerlendirmede amaç fonksiyonu bilgisini kullanır bunun dışında yardımcı bilgi gerektirmez.
•	Olasılıksal geçiş kurallarını kullanır.



Genetik Algoritma kullanmanın bize sağladığı avantajlar ise:

1. Çözüm uzayı daha geniştir.
2. Global optimumu keşfetmek daha kolaydır.
3. Fonksiyon evrimlerini kullanır.
4. Farklı problemler için kolaylıkla değiştirilebilir.
5. Büyük anlaşılması zor arama uzayını kolaylıkla anlamaktadır.
6. Uygunluk yüzeyi (Fitness Landscape) karmaşıktır.
7. Yanıt yüzey (Response surface) hakkında herhangi bir bilgi   gerektirmez.
8. Lokal optimuma düşme konusunda dirençlidir.
9. Büyük boyutlu problemlere uygulanabilir.

    

Kolay GA yapısı evrimsel programlama yapısına eştir. t iterasyonu süresince potansiyel çözümlerin popülasyonunu sürdürmektedir. Çözüm uygunluk değerine göre değerlendirilir.Yeni popülasyon t+1 iterasyonda daha uygun fertlerin tercihi ile oluşmaktadır. Bu yeni popülasyondaki fertler çaprazlama ve değişinim ile başkalaşıma uğrar yeni çözümler oluşmaktadır

Genetik algoritma da izlenecek adımlar şu şekildedir;

•	Toplulukta bulunan fert rakamını tanımlamakla başlanır. Fert rakamı ile alakalı kesin birsayı yoktur. Probleme bağlı olarak değişmektedir gözlem ve tahlil ile tanımlanır
•	Kromozom diziler/fertler ne kadar iyi olduğuna uygunluk değerinin hesaplanmasıyla karar verilir.
•	Yeni popülasyon daha uygun bireylerin seçimi ile oluşur. Bu seçim için orantılı rulettekerleği, sıraya dayalı rulet tekerleği ve turnuva seçimi gibi farklı seçim yöntemleri kullanılmaktadır.
•	Bu yeni popülasyondaki bireyler çaprazlama ve mutasyon ile değişime uğrar ve yeni çözümler oluşur
•	GA belirli bir nesil sayısı veya durdurma kriteri sağlanana kadar defalarca çalıştırılır.GA işleyişi sonucunda en iyi kromozom (dizi, birey) çözüm olarak alınır.

## Genetik Algoritma’nın Parametreleri?

•	Popülasyon Büyüklüğü:En önemli kararlardan biri kullanıcı tarafından belirlenenpopülasyon büyüklüğüdür. Probleme bağlı olarak değişmektedir. Popülasyon büyüklüğü GA‘nın genel performansını ve GA’nın etkinliğini etkilemektedir. Algoritmanın performansı iki şekilde etkilenmektedir.
•	Çaprazlama Oranı: Çaprazlamanın amacı mevcut iyi kromozomları birleştirerek dahaiyi kromozom oluşturmaktır. Temel parametrelerden biri olan çaprazlama olasılığı (Pc). Ne sıklıkla çaprazlamanın yapılacağını tanımlayan bir parametredir.
•	Mutasyon Oranı: Mutasyon yapılmasının nedeni; birbirini izleyen daha uygunbireylerin atılmasından gelmektedir. Kromozomlarda rasgele değişiklikler yapılarak Gas arama uzayında yeni kısımlara ulaşılmasını sağlar. Aynı zamanda önemli özelliklerin erken kaybolmamasının ve böylece eşleşme havuzunda çeşitliliğin korunmasın sağlamaktadır

Bu kısıma kadar genetik algoritma nedir, genetik algoritma ile problem çözerken kullandığım kavramların açıklaması bize sağladığı fayda ve zararlardan bahsettim. Bu aşamadan sonra genetik algoritma ile gezgin satıcı problemini çözerken oluşturduğum data-set’in nasıl oluşturulduğu kullandığım fonksiyonlar ve seçim yöntemleri hakkında bilgi vereceğim. Genetik Algoritma ile gezgin satıcı problemini çözerken Python dilini kullandım.

Python seçmemin amacı gezgin satıcı problemi ve genetik algoritma hakkında daha çok kaynağın bulunması ve aynı zamanda programın yapısı amacı matematiksel ve algoritmasal programlar için uygun olmasıdır. Python’ın en çok kullanıldığı alanların başında veri biliminin gelmesidir.
