from django.db import models
class alternatif(models.Model):
    kodealternatif = models.CharField(max_length=25, primary_key=True)
    namaalternatif = models.CharField(max_length=25)
    angka= (
        (1, 'Lebih dari 15 JT'),
        (2, '8-15 JT'),
        (3, '5-8 JT'),
        (4, '3-5 JT'),
        (5, 'Kurang dari 3 JT'),
    )
    ram = (
        (1, '4 GB'),
        (2, '6 GB'),
        (3, '8 GB'),
        (4, '12 GB'),
        (5, '16 GB'),
    )
    ssd = (
        (1, 'Kurang dari 256GB'),
        (2, '320 GB'),
        (3, '512 TB'),
        (4, '1 TB'),
        (5, 'Lebih dari 1 TB'),
    )
    prosesor = (
        (1, 'Pentium'),
        (2, 'Celeron'),
        (3, 'Core i3'),
        (4, 'Core i5 atau Ryzen 5'),
        (5, 'Core i7 atau Ryzen 7'),
    )
    ukuranlayar = (
        (1, 'Kurang dari 13 Inci'),
        (2, '13 - 14,9 inci'),
        (3, '15 - 15,6 inci'),
        (4, '15,6 - 17 inci'),
        (5, 'Lebih dari 17 Inci'),
    )
    vga = (
        (1, '2 GB'),
        (2, '4 GB'),
        (3, '6 GB'),
        (4, '8 GB'),
        (5, '12 GB'),
    )
    garansi = (
        (1, 'Toko'),
        (3, 'Distributor'),
        (5, 'Resmi'),
    )
    c1 = models.FloatField(choices=angka, default=1)
    c2 = models.FloatField(choices=ram, default=1)
    c3 = models.FloatField(choices=ssd, default=1)
    c4 = models.FloatField(choices=prosesor, default=1)
    c5 = models.FloatField(choices=ukuranlayar, default=1)
    c6 = models.FloatField(choices=vga, default=1)
    c7 = models.FloatField(choices=garansi, default=1)

    def __str__(self):
        return "{}". format(self.kodealternatif)
    
class normalisasi(models.Model):
    kodealternatif = models.CharField(max_length=3)
    c1norm = models.IntegerField()
    c2norm = models.IntegerField()
    c3norm = models.IntegerField()
    c4norm = models.IntegerField()
    c5norm = models.IntegerField()
    c6norm = models.IntegerField()
    c7norm = models.IntegerField()

    def __str__(self):
        return "{}". format(self.kodealternatif)