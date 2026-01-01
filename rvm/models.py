from django.db import models
import uuid
from django.db import models
from django.utils import timezone


class RVM(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    machine_code = models.CharField(max_length=50, unique=True)
    location_name = models.CharField(max_length=255, db_index=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE, db_index=True)
    last_usage_at = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        indexes = [
            models.Index(fields=["status", "-last_usage_at"]),
        ]

    def _str_(self):
        return f"{self.machine_code} - {self.location_name} ({self.status})"

# Create your models here.
