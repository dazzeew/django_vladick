from datetime import date,datetime

from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from .models import Valuta, Transaction, Country, Employee, User


@receiver(post_save, sender = Transaction)
def post_save_transaction(created,**kwargs):
	if created:
		instance = kwargs['instance']
		transaction = Transaction.objects.get(id = instance.id)
		user_id = User.objects.get(username = instance.user_id)
		user = Employee.objects.get(user_id = user_id.id)
		valuta = Valuta.objects.get(name_valut = instance.type_valuta_id).type_risk
		if Employee.objects.get(user_id = user_id.id).country_id is not None:
			country = Country.objects.get(name_country = user.country_id).type_risk
		else:
			country = 3
		lvl_risk = country + valuta + calculate_risk(user,user_id) + (1 if transaction.count < 100 else (2 if ((transaction.count >= 100) and transaction.count <= 1000) else 3))
		print(lvl_risk)
		if (lvl_risk) < 7:
			transaction.level_risk = 'Низкий'
		elif ((lvl_risk >= 7) and (lvl_risk < 11)):
			transaction.level_risk = 'Средний'
		else:
			transaction.level_risk = 'Высокий'
		transaction.save()
		# print('Окей')

def calculate_risk(user,user_id):
	now = date.today()
	born = user.born_date
	join = user_id.date_joined
	lvl_risk = 0
	if user.born_date is not None:
		if (now.month <= born.month) and (now.day <= born.day):
			age = now.year - born.year
		else:
			age = now.year - born.year - 1
		if (age <= 18):
			lvl_risk += 3
		elif (age > 18) and (age <= 25):
			lvl_risk += 2
		else:
			lvl_risk += 1
	else:
		risk += 3
	if (now.month <= join.month) and (now.day <= join.day):
		age_join = now.year - join.year
	else:
		age_join = now.year - join.year - 1
	if (age_join <= 1):
		lvl_risk += 3
	elif (age_join <= 2):
		lvl_risk += 2
	else:
		lvl_risk += 1
	return lvl_risk 

# @receiver(pre_save, sender = Employee)
# def pre_save_employee(**kwargs):
# 	instance = kwargs['instance']
# 	if Employee.objects.filter(id = instance.id).born_date == '':
# 		print ('Пустое')
# 	else:
# 		print('Не пустое')
	# Employee.objects.filter(id = instance.id).update(date_add_param = datetime.today())

# @receiver(post_save, sender = Country)
# def post_save_employee(**kwargs):
# 	instance = kwargs['instance']
# 	Country.objects.filter(id = instance.id).update(date_add = datetime.today())

# @receiver(post_save, sender = Valuta)
# def post_save_employee(**kwargs):
# 	instance = kwargs['instance']
# 	Valuta.objects.filter(id = instance.id).update(date_add = datetime.today())