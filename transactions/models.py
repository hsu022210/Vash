from django.db import models

# Create your models here.

class Transaction(models.Model):
    user_send = models.CharField(max_length=50)
    user_receive = models.CharField(max_length=50)
    deal_time = models.DateTimeField(auto_now=True)
    deal_type_pay_not_request = models.BooleanField()
    deal_amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.deal_amount
