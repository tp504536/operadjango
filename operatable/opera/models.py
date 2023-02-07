from django.db import models


class Table(models.Model):
    day_to = (('Пн', 'Пн'),
              ('Вт', 'Вт'),
              ('Ср', 'Ср'),
              ('Чт', 'Чт'),
              ('Пт', 'Пт'),
              ('Сб', 'Суб'),
              ('Вс', 'Вос'))
    date = models.DateField(null=False, verbose_name="Дата")
    day = models.CharField(null=False, max_length=15, verbose_name="День", choices=day_to)

    class Meta:
        verbose_name = "Дату"
        verbose_name_plural = "Общее расписание"


    def __str__(self):
        return self.day
class Tables(models.Model):
    #date = models.TimeField(null=False, verbose_name="Дата")
    opera = models.CharField(null=False, max_length=300, verbose_name='Опера',blank =True)
    balet = models.CharField(null=False, max_length=300, verbose_name='Балет',blank =True)
    scena = models.CharField(null=False, max_length=300, verbose_name='Сцена',blank =True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Опера"


    def __str__(self):
        return self.opera


class Operatable(models.Model):
    day_to = (('Пн', 'Пн'),
              ('Вт', 'Вт'),
              ('Ср', 'Ср'),
              ('Чт', 'Чт'),
              ('Пт', 'Пт'),
              ('Сб', 'Суб'),
              ('Вс', 'Вос'))
    date = models.DateField(null=False, verbose_name="Дата")
    day = models.CharField(null=False, max_length=15, verbose_name="День", choices=day_to)

    class Meta:
        verbose_name = "Дату"
        verbose_name_plural = "Опера"


    def __str__(self):
        return self.day
class Opera(models.Model):
    users = (('Вутирас','Вутирас'),('Мокеева','Мокеева'),('Стародубова','Стародубова'),('Семенищева','Семенищева'),
             ('Леус','Леус'),('Новикова','Новикова'),('Карлова','Карлова'),('Павлова','Павлова'),
             ('Наумова','Наумова'),('Кумылганова','Кумылганова'),('Перхурова','Перхурова'),('Шевченко','Шевченко'),
             ('Рыженкова','Рыженкова'),('Шляпникова','Шляпникова'),('Бабинцева','Бабинцева'),
             ('Ковалевская','Ковалевская'),('Позолотина','Позолотина'),('Никанорова','Никанорова'),
             ('Бирюзова','Бирюзова'),('Пастухова','Пастухова'),('Осовин','Осовин'),('Межов','Межов'),
             ('Манукян','Манукян'),('Чеберяк','Чеберяк'),('Крюков','Крюков'),('Рахимов','Рахимов'),
             ('Ворошнин','Ворошнин'),('Петров','Петров'),('Леус','Леус'),('Бовыкин','Бовыкин'),('Шлыков','Шлыков'),
             ('Девин', 'Девин'), ('Краснов', 'Краснов'), ('Гордеев', 'Гордеев'), ('Миронов', 'Миронов'),
             ('Кульга', 'Кульга'),('Стародубов','Стародубов'),('Семенищев','Семенищев'),('Касимов','Касимов'),
             ('Попов','Попов'),('Решетников','Решетников'),('Коробейников','Коробейников'),('Бударацкий','Бударацкий'),
             ('Трошин','Трошин'),('Морозов','Морозов'))
    prof = (('Банцевич','Банцевич'),('Марков','Марков'),('Решетникова','Решетникова'),
            ('Иванова','Иванова'),('Смирнова','Смирнова'))
    fam = models.CharField(null=False, max_length=15, verbose_name="Фамилия", choices=users)
    dir = models.CharField(null=False, max_length=300, verbose_name='Дирижер',blank =True)
    room = models.CharField(null=False, max_length=300, verbose_name='Класс',blank =True)
    time = models.CharField(null=False, max_length=300, verbose_name='Время',blank =True)
    name_prof = models.CharField(null=False, max_length=300, verbose_name='Название',blank =True)
    pro = models.CharField(null=True, max_length=15, verbose_name="Фамилия", choices=prof)
    table = models.ForeignKey(Operatable, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "Опера"

    def __str__(self):
        return self.fam

