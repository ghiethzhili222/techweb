from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from accountapp.models import Doctor, Patient


class appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(
        blank=True,
        upload_to='prescriptions/',
    )

    class status(models.TextChoices):
        PENDING = "PENDING", "En attente"
        CONFIRMED = "CONFIRMED", "Confirmé"
        CANCELED = "CANCELED", "Annulé"

    status = models.CharField(
        max_length=10,
        choices=status.choices,
        default=status.PENDING,
    )
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')

    def clean(self):
        super().clean()
        if self.appointment_date and self.appointment_date < timezone.now():
            raise ValidationError("Appointment date cannot be in the past.")

    class Meta:
        ordering = ['-appointment_date']

        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date'],
                name='unique_appointment_per_doctor',
                violation_error_message="This doctor already has an appointment at this date and time."
            ),
        ]

    def __str__(self):
        return (
            f"Appointment with Dr. {self.doctor} for {self.patient} "
            f"on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"
        )