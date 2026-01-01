from django.shortcuts import render
from rest_framework import serializers


# Create your views here.

from datetime import timedelta
from django.db.models import F
from django.utils import timezone
from rest_framework.generics import ListAPIView

from .models import RVM
from .serializer import RVMSerializer


class ActiveRVMListAPIView(ListAPIView):
    serializer_class = RVMSerializer

    def get_queryset(self):
        qs = RVM.objects.filter(status=RVM.Status.ACTIVE)

        # Bonus: filter by location
        location = self.request.query_params.get("location")
        if location:
            qs = qs.filter(location_name__icontains=location.strip())

        # Bonus: filter by recent activity (past N hours)
        used_within_hours = self.request.query_params.get("used_within_hours")
        if used_within_hours is not None:
            try:
                hours = int(used_within_hours) if used_within_hours.strip() else 24
                cutoff = timezone.now() - timedelta(hours=hours)
                qs = qs.filter(last_usage_at__gte=cutoff)
            except ValueError:
                pass

        # Order: most recent activity first, nulls last
        return qs.order_by(F("last_usage_at").desc(nulls_last=True))

