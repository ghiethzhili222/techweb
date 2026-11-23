from django.contrib import admin
from accountapp.models import Doctor, Patient
from .models import appointment
@admin.action(description="Confirm selected appointments")
def confirm_appointment(modeladmin, request, queryset):
    queryset.update(status='CONFIRMED')
    
@admin.register(appointment)
class appointementAdminPers(admin.ModelAdmin):
    actions = [confirm_appointment]
    list_display = ("id", "reason", "status", "appointment_date", "doctor", "patient")
    list_filter = ("status", "appointment_date", "doctor", "patient")
    list_editable = ("status",)
    list_per_page = 2
    ordering = ("-appointment_date",)
    fieldsets = (
        ("description", {"fields": ("reason", "status")}),
        ("date and time", {"fields": ("appointment_date", "duration_minutes")}),
        ("doctor and patient", {"fields": ("doctor", "patient")}),
        ("creation and update", {"fields": ("created_at", "updated_at")}),
        
    )
    readonly_fields = ("created_at", "updated_at")