from django.contrib import admin
from . import models


@admin.register(models.Quarter)
class Quarter(admin.ModelAdmin):
    ...

@admin.register(models.Administration)
class AdministrationAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Commissioner)
class Commissioner(admin.ModelAdmin):
    ...

@admin.register(models.UserCom)
class UserComAdmin(admin.ModelAdmin):
    ...

@admin.register(models.House)
class HouseAdmin(admin.ModelAdmin):
    ...


@admin.register(models.PictureHouse)
class PictureHouseAdmin(admin.ModelAdmin):
    ...


@admin.register(models.DataLocation)
class DataLocationAdmin(admin.ModelAdmin):
    ...
