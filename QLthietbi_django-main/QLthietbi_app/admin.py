from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Phong, LoaiThietBi, ThietBi
#from .forms import ThietBiForm
from django import forms

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'ho', 'ten', 'gioi_tinh', 'chuc_vu', 'ngay_sinh', 'email', 'sdt', 'ngay_vao_lam', 'is_staff', 'is_active')
    list_filter = ('chuc_vu', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Thông tin cá nhân', {'fields': ('ho', 'ten', 'gioi_tinh', 'chuc_vu', 'ngay_sinh', 'email', 'sdt', 'ngay_vao_lam')}),
        ('Quyền hạn', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'ho', 'ten', 'password1', 'password2', 'sdt', 'gioi_tinh', 'ngay_sinh', 'chuc_vu', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('username', 'email', 'ho', 'ten')
    ordering = ('id',)
    
admin.site.register(CustomUser, CustomUserAdmin)

class ThietBiInlineFormset(forms.models.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = True
    
class ThietBiInline(admin.TabularInline):
    model = ThietBi

class PhongAdmin(admin.ModelAdmin):
    inlines = [ThietBiInline]
    list_display = ('id_phong', 'ten_phong', 'so_tang')

class LoaiThietBiAdmin(admin.ModelAdmin):
    list_display = ('id_loai_thiet_bi', 'ten_loai_thiet_bi')

class ThietBiAdmin(admin.ModelAdmin):
    list_display = ['id_thiet_bi', 'ten_thiet_bi','hinh_anh', 'loai_thiet_bi', 'phong', 'ngay_mua', 'gia_mua', 'tinh_trang', 'ngay_bao_tri', 'mo_ta']
    list_filter = ('loai_thiet_bi', 'tinh_trang', 'ngay_bao_tri')
    search_fields = ('ten_thiet_bi', 'loai_thiet_bi', 'tinh_trang')
    ordering = ('id_thiet_bi',)
    list_per_page = 10

admin.site.register(Phong, PhongAdmin)
admin.site.register(LoaiThietBi, LoaiThietBiAdmin)
admin.site.register(ThietBi, ThietBiAdmin)








