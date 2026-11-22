from django.db import models
from accountapp.models import Doctor, Patient

# Create your models here.
class appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(
        blank=True,
        upload_to='prescriptions/',
    )

    class status(models.TextChoices):
        PENDING = "PENDING", "En attente"
        COMFIRMED = "CONFIRMED", "Confirmé"
        CANCELED = "CANCELED", "Annulé" 
    status = models.CharField(max_length=10, choices=status.choices, default=status.PENDING)    
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    class Meta:
        ordering = ['-appointment_date']

        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date'],
                name='unique_appointment_per_doctor',
                violation_error_message="This doctor already has an appointment at this date and time."
            ),
        ]
