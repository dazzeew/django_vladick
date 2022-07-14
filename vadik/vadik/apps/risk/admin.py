from django.contrib import admin

from .models import Valuta, Transaction, Country, Employee

class ValutaAdmin(admin.ModelAdmin):
	list_display = ('name_valut', 'mark_valut', 'type_risk', 'date_add')
	list_filter = ('type_risk','date_add')
	search_fields = ['name_valut']
	date_hierarchy = 'date_add'

class CountryAdmin(admin.ModelAdmin):
	list_display = ('name_country', 'type_risk','date_add')
	list_filter = ('type_risk','date_add')
	search_fields = ['name_country']
	date_hierarchy = 'date_add'

class TransactionAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'count','type_valuta_id','level_risk','date_order')
	list_filter = ('type_valuta_id','level_risk','date_order')
	search_fields = ['user_id__username']
	date_hierarchy = 'date_order'

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('user', 'date_add_param')
	list_filter = ('user', 'date_add_param')
	search_fields = ['user__username']
	date_hierarchy = 'date_add_param'

admin.site.register(Valuta,ValutaAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(Employee,EmployeeAdmin)