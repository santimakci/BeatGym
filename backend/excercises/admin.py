from django.contrib import admin

from excercises.models import Excercise, ExcerciseName
@admin.register(Excercise)
class UserAdmin(admin.ModelAdmin):

    list_display = ('pk', 'excercise_name', 'series', 'repetitions')

@admin.register(ExcerciseName)
class UserAdmin(admin.ModelAdmin):

    list_display = ('pk', 'name')
