import datetime

from django.db import models

from django.contrib.auth.models import User

class Valuta(models.Model):
	name_valut = models.CharField('Название валюты', max_length = 50, unique=True)
	mark_valut = models.CharField('Значок валюты', max_length = 3, unique=True)
	type_risk = models.IntegerField('Тип риска',default = 0)
	date_add = models.DateTimeField('Дата добавления/обновления', null = True, auto_now = True)

	def __str__(self):
		return self.name_valut

	class Meta:
		verbose_name = 'Валюта'
		verbose_name_plural = 'Валюты'
		db_constraints = {
        'prime_risk': 'check ((type_risk <= 3) and (type_risk >= 0))',
    }

class Country(models.Model):
	name_country = models.CharField('Название страны', max_length = 30, unique=True)
	type_risk = models.IntegerField('Тип риска',default = 0)
	date_add = models.DateTimeField('Дата добавления/обновления', null = True, auto_now = True)

	def __str__(self):
			return self.name_country

	class Meta:
		verbose_name = 'Страна'
		verbose_name_plural = 'Страны'
		db_constraints = {
        'prime_risk': 'check ((type_risk <= 3) and (type_risk >= 0))',
    }

class Employee(models.Model):
	user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
	born_date = models.DateField('Дата рождения', blank = True)
	country_id = models.ForeignKey(Country, verbose_name="Страна", db_column= 'country_id', on_delete = models.PROTECT, blank = True)
	date_add_param = models.DateTimeField('Дата добавления/обновления', null = True, auto_now = True)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = 'Пользователь доп. параметры'
		verbose_name_plural = 'Пользователи доп. параметры'
		db_constraints = {
        'age_over_18': 'check (date_part($$year$$,age(born_date::date)) >= 14)',
    }


class Transaction(models.Model):
	user_id = models.ForeignKey(User, verbose_name="Пользователь", db_column= 'user_id', on_delete = models.PROTECT)
	count = models.FloatField('Сумма перевода')
	type_valuta_id = models.ForeignKey(Valuta, verbose_name="Валюта", db_column= 'type_valuta_id', on_delete = models.PROTECT)
	level_risk = models.CharField('Уровень риска', max_length = 10, blank = True)
	date_order = models.DateTimeField('Дата транзакции', null = True, auto_now = True)

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Транзакция'
		verbose_name_plural = 'Транзакции'
		db_constraints = {
        'agree_risk': 'check (level_risk in ($$Низкий$$,$$Средний$$,$$Высокий$$,$$$$))',
        'count_not_zero':'check (count > 0)',
    }