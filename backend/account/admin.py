from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile


class ProfileInline(admin.TabularInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"


class UserAdmin(UserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(UserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [ProfileInline]
        return super(UserAdmin, self).change_view(*args, **kwargs)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
