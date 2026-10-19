
from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):

    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Documents', 'Documents'),
        ('Books', 'Books'),
        ('Clothing', 'Clothing'),
        ('Accessories', 'Accessories'),
        ('Other', 'Other'),
    ]

    REPORT_TYPE_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]

    STATUS_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
        ('Returned', 'Returned'),
    ]

    item_name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    report_type = models.CharField(
        max_length=10,
        choices=REPORT_TYPE_CHOICES
    )
    location = models.CharField(max_length=200)
    item_date = models.DateField()
    contact_details = models.CharField(max_length=200)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Lost'
    )
    reported_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='item_reports'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.report_type == 'Found' and self.status == 'Lost':
            self.status = 'Found'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item_name

