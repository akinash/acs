# Register your models here.
from django.contrib import admin
from import_export import fields
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import PassEvent



class PassEventResource(resources.ModelResource):
    init_date = fields.Field(attribute='init_date', column_name='Время')
    controller = fields.Field(attribute='controller', column_name='Контроллеры')
    pass_type = fields.Field(attribute='pass_type', column_name='Вход и выход')
    card = fields.Field(attribute='card', column_name='Карта')
    status = fields.Field(attribute='status', column_name='Статус')
    surname = fields.Field(attribute='surname', column_name='Фамилия')
    name = fields.Field(attribute='name', column_name='Имя')
    patronymic = fields.Field(attribute='patronymic', column_name='Отчество')
    department = fields.Field(attribute='department', column_name='Отдел')

    class Meta:
        model = PassEvent
        fields = ('init_date', 'controller', 'pass_type', 'card', 'status', 'surname', 'name', 'patronymic',
                  'department')
        export_order = fields
        import_id_fields = ['init_date']
        widgets = {
            'init_date': {'format': '%d.%m.%Y %k:%M:%S'},
        }


class PassEventAdmin(ImportExportModelAdmin):
    resource_class = PassEventResource


admin.site.register(PassEvent, PassEventAdmin)