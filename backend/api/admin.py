from django.contrib import admin
from .models import Direction, Doctor


class DirectionAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ['sort_num']


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'experience', 'get_directions')
    filter_horizontal = ('directions',)
    list_filter = ('directions', 'experience')
    search_fields = ('name', 'directions__name')
    ordering = ['sort_num']

    def get_directions(self, obj):
        return ", ".join([d.name for d in obj.directions.all()])
    get_directions.short_description = 'Directions'


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Direction, DirectionAdmin)
