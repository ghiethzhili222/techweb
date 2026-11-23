from datetime import timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from .models import appointment


class AppointmentModelTests(TestCase):
    def test_past_appointment_is_invalid(self):
        appointment_instance = appointment(
            appointment_date=timezone.now() - timedelta(minutes=1),
        )

        with self.assertRaisesMessage(
            ValidationError,
            "Appointment date cannot be in the past.",
        ):
            appointment_instance.clean()
