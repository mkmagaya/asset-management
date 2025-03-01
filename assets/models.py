# from django.db import models

# class Asset(models.Model):
#     asset_tag = models.CharField(max_length=50, unique=True)
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     category = models.CharField(max_length=100)
#     purchase_date = models.DateField()
#     cost = models.DecimalField(max_digits=10, decimal_places=2)
#     location = models.CharField(max_length=100)
#     status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    
#     def __str__(self):
#         return self.name

from django.db import models

class Asset(models.Model):
    DEVICE_TYPES = [('Laptop', 'Laptop'), ('Desktop', 'Desktop')]

    name = models.CharField(max_length=255)
    assigned_user = models.CharField(max_length=255, blank=True, null=True)
    user_company = models.CharField(max_length=255)
    device_type = models.CharField(max_length=10, choices=DEVICE_TYPES)
    asset_code = models.CharField(max_length=255, blank=True, null=True)
    product_number = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    domain_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    
    # Desktop only fields
    keyboard = models.BooleanField(default=False)
    monitor = models.BooleanField(default=False)
    mouse = models.BooleanField(default=False)

    # 🔹 Newly added fields
    category = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    asset_tag = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, default="Available")  # e.g., Available, Assigned, In Repair
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.domain_id:  # Generate Domain ID only for new entries
            company_abbr = self.user_company[:3].upper()
            device_letter = 'L' if self.device_type == 'Laptop' else 'D'
            dept = "ICT"
            serial_suffix = self.serial_number[-4:]
            self.domain_id = f"{company_abbr}-{device_letter}-{dept}-{serial_suffix}"
        super().save(*args, **kwargs)
