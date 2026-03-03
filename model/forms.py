from django import forms

class CreateUserForm(forms.Form):
    name = forms.CharField(label="User name", max_length=100)

class Data(forms.Form):
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
    otvet_CHOICES = [
        (1, "Yes"),
        (0, "No"),
        ('','')
    ]

    god_rojdeniya = forms.IntegerField()
    podpisani_documenti = forms.ChoiceField(
        choices=podpisani_documenti_CHOICES,required=False
    )
    pol = forms.ChoiceField(
        choices=POL_CHOICES,
    )

    bil_prostoy = forms.ChoiceField(
        choices=bil_prostoy_CHOICES,
    )
    opit_v_doljnosti = forms.FloatField()
    activnost = forms.FloatField()
    znak_zodiaka=forms.ChoiceField(
        choices=znak_zodiaka_CHOICES,
    )
    vozrast = forms.FloatField()
    ocenka_hr = forms.FloatField()
    uroven_oplati = forms.FloatField()
    oflain_meropriyatiya = forms.FloatField()
    obrazovanie = forms.ChoiceField(
        choices=obrazovanie_CHOICES,
    )
    telefon = forms.FloatField()
    gorod = forms.ChoiceField(
        choices=gorod_CHOICES,
    )
    razmer = forms.ChoiceField(
        choices=razmer_CHOICES,
    )
    zakritie_proekti = forms.FloatField()
    god_nayma = forms.FloatField()
    kursi = forms.FloatField()


'''
    class STATUS_CHOICES(forms.ChoiceField):
        YES= 1, 'Yes'
        NO = 0, 'No'
'''