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
        verbose_name_plural = "Расписание"


    def __str__(self):
        return self.day
class Tables(models.Model):
    date = models.TimeField(null=False, verbose_name="Дата")
    opera = models.TextField(null=False, max_length=300, verbose_name='Опера',blank =True)
    balet = models.TextField(null=False, max_length=300, verbose_name='Балет',blank =True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Опера-Балет"
        ordering = ('-date',)

    def __str__(self):
        return self.opera
# class Opera(models.Model):
#     nome = models.CharField(max_length=100)
#     data_nascimento = models.DateTimeField(blank=True, null=True)
#     table = models.ForeignKey(Table, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name_plural = "Опера"
#
#     def __str__(self):
#         return self.nome
#
#
# class Bal(models.Model):
#     nome = models.CharField(max_length=100)
#     data_nascimento = models.DateTimeField(blank=True, null=True)
#     table = models.ForeignKey(Table, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name_plural = "Балет"
#
#     def __str__(self):
#         return self.nome


class Scene(models.Model):
    data_nascimento = models.DateField(blank=True, null=True)
    nome = models.TextField(max_length=100)


    class Meta:
        verbose_name_plural = "Сцена"
        verbose_name = "Дату"

    def __str__(self):
        return self.nome