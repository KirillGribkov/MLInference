from django.db import models


# Create your models here.
class DataModel(models.Model):
    POL_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    podpisani_documenti_CHOICES = [
        ("Да", "Да"),
        ("Нет", "Нет"),
        ("", ""),
    ]
    bil_prostoy_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No")
    ]
    znak_zodiaka_CHOICES = [
        ("Рыбы", "Козерог"),
        ("Козерог", "Козерог"),
        ("Близнецы", "Близнецы"),
        ("Рак", "Рак"),
        ("Телец", "Телец"),
        ("Дева", "Дева"),
        ("Стрелец", "Стрелец"),
        ("Весы", "Весы"),
        ("Овен", "Овен"),
        ("Водолей", "Водолей"),
        ("Лев", "Лев"),
        ("Скорпион", "Скорпион"),
    ]
    obrazovanie_CHOICES = [
        ("Bachelors", "Bachelors"),
        ("Masters", "Masters"),
        ("PHD", "PHD"),
    ]

    gorod_CHOICES = [
        ("Pune", "Pune"),
        ("New Delhi", "New Delhi"),
        ("Bangalore", "Bangalore"),
    ]
    razmer_CHOICES = [
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "Xl"),
        ("XXL", "XXl")
    ]


    class STATUS_CHOICES(models.IntegerChoices):
        YES= 1, 'Yes'
        NO = 0, 'No'

    god_rojdeniya = models.IntegerField(null=True,blank=True)
    podpisani_documenti = models.CharField(
        max_length=3,
        choices=podpisani_documenti_CHOICES,
        default="",
        null=True, 
        blank=True
    )
    pol = models.CharField(
        max_length=6,
        choices=POL_CHOICES,
        default="Female",
        null=False, 
        blank=False
    )

    bil_prostoy = models.CharField(
        max_length=3,
        choices=bil_prostoy_CHOICES,
        default="Yes",
        null=False, 
        blank=False
    )
    opit_v_doljnosti = models.FloatField(null=False, blank=False)
    activnost = models.FloatField(null=False, blank=False)
    znak_zodiaka=models.CharField(
        max_length=8,
        choices=znak_zodiaka_CHOICES,
        default="Скорпион",
        null=False, 
        blank=False
    )
    vozrast = models.FloatField(null=False, blank=False)
    ocenka_hr = models.FloatField(null=False, blank=False)
    uroven_oplati = models.FloatField(null=False, blank=False)
    oflain_meropriyatiya = models.FloatField(null=False, blank=False)
    obrazovanie = models.CharField(
        max_length=9,
        choices=obrazovanie_CHOICES,
        default="Bachelors",
        null=False, 
        blank=False
    )
    telefon = models.FloatField(null=False, blank=False)
    gorod = models.CharField(
        max_length=9,
        choices=gorod_CHOICES,
        default="Pune",
        null=False, 
        blank=False
    )
    razmer = models.CharField(
        max_length=3,
        choices=razmer_CHOICES,
        default="XS",
        null=False, 
        blank=False
    )
    zakritie_proekti = models.FloatField(null=False, blank=False)
    god_nayma = models.FloatField(null=False, blank=False)
    kursi = models.FloatField(null=False, blank=False)

    otvet = models.IntegerField(choices=STATUS_CHOICES,null=False, blank=False)
    real = models.IntegerField(choices=STATUS_CHOICES,null=True, blank=True)
    def __str__(self):
        return self.name
    
class DataModelABTest(models.Model):
    POL_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    podpisani_documenti_CHOICES = [
        ("Да", "Да"),
        ("Нет", "Нет"),
        ("", ""),
    ]
    bil_prostoy_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No")
    ]
    znak_zodiaka_CHOICES = [
        ("Рыбы", "Козерог"),
        ("Козерог", "Козерог"),
        ("Близнецы", "Близнецы"),
        ("Рак", "Рак"),
        ("Телец", "Телец"),
        ("Дева", "Дева"),
        ("Стрелец", "Стрелец"),
        ("Весы", "Весы"),
        ("Овен", "Овен"),
        ("Водолей", "Водолей"),
        ("Лев", "Лев"),
        ("Скорпион", "Скорпион"),
    ]
    obrazovanie_CHOICES = [
        ("Bachelors", "Bachelors"),
        ("Masters", "Masters"),
        ("PHD", "PHD"),
    ]

    gorod_CHOICES = [
        ("Pune", "Pune"),
        ("New Delhi", "New Delhi"),
        ("Bangalore", "Bangalore"),
    ]
    razmer_CHOICES = [
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "Xl"),
        ("XXL", "XXl")
    ]


    class STATUS_CHOICES(models.IntegerChoices):
        YES= 1, 'Yes'
        NO = 0, 'No'
    model_number = models.IntegerField(null=False,blank=False)
    god_rojdeniya = models.IntegerField(null=True,blank=True)
    podpisani_documenti = models.CharField(
        max_length=3,
        choices=podpisani_documenti_CHOICES,
        default="",
        null=True, 
        blank=True
    )
    pol = models.CharField(
        max_length=6,
        choices=POL_CHOICES,
        default="Female",
        null=False, 
        blank=False
    )

    bil_prostoy = models.CharField(
        max_length=3,
        choices=bil_prostoy_CHOICES,
        default="Yes",
        null=False, 
        blank=False
    )
    opit_v_doljnosti = models.FloatField(null=False, blank=False)
    activnost = models.FloatField(null=False, blank=False)
    znak_zodiaka=models.CharField(
        max_length=8,
        choices=znak_zodiaka_CHOICES,
        default="Скорпион",
        null=False, 
        blank=False
    )
    vozrast = models.FloatField(null=False, blank=False)
    ocenka_hr = models.FloatField(null=False, blank=False)
    uroven_oplati = models.FloatField(null=False, blank=False)
    oflain_meropriyatiya = models.FloatField(null=False, blank=False)
    obrazovanie = models.CharField(
        max_length=9,
        choices=obrazovanie_CHOICES,
        default="Bachelors",
        null=False, 
        blank=False
    )
    telefon = models.FloatField(null=False, blank=False)
    gorod = models.CharField(
        max_length=9,
        choices=gorod_CHOICES,
        default="Pune",
        null=False, 
        blank=False
    )
    razmer = models.CharField(
        max_length=3,
        choices=razmer_CHOICES,
        default="XS",
        null=False, 
        blank=False
    )
    zakritie_proekti = models.FloatField(null=False, blank=False)
    god_nayma = models.FloatField(null=False, blank=False)
    kursi = models.FloatField(null=False, blank=False)

    otvet = models.IntegerField(choices=STATUS_CHOICES,null=False, blank=False)
    real = models.IntegerField(choices=STATUS_CHOICES,null=True, blank=True)
    def __str__(self):
        return self.name
    