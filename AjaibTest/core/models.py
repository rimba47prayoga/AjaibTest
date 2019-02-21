from django.db import models


class SimpleUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()


class TransactionBalance(models.Model):
    amount = models.IntegerField()

    class Meta:
        db_table = "transaction_balance"
