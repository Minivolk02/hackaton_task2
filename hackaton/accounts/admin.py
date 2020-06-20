from django.contrib import admin
from .models import *
from .forms import UserProfileCreationForm, UserProfileChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = UserProfile
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'),
         {'fields': ('avatar', 'email', 'first_name', 'last_name', 'middle_name', 'birth_date', 'user_position', 'user_department')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'activity')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'middle_name', 'birth_date'),
        }),
    )
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'middle_name', 'is_staff', 'user_position', 'user_department', 'activity')
    list_display_links = ('id', 'username', 'email')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Department, DepartmentAdmin)