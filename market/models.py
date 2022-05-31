from django.db import models

# Create your models here.
from auth_person.models import Person


class Product(models.Model):
    name = models.CharField(max_length=99)
    type = models.CharField(max_length=99)
    img = models.ImageField(upload_to='files/image/product_img/%Y-%m-%d/')
    price = models.DecimalField(max_digits=19, decimal_places=2)
    count = models.IntegerField()


class Buy(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    count_product = models.IntegerField()
    date = models.DateField(auto_now=True)
    summary = models.DecimalField(max_digits=19, decimal_places=2)

    def set_summary(self):
        self.summary = self.product.price * (self.product.price * 15 / 100)

    def buy(self):
        if self.person.balance <= 0:
            raise ValueError('Your balance <=0')
        if self.person.balance < self.summary:
            raise ValueError('Your balance < summary buy')
        if self.summary <= 0:
            raise ValueError('summary <= 0')
        if self.count_product > self.product.count:
            raise ValueError('count product > product count')
        self.person.balance = self.person.balance - self.summary
        self.product.count = self.product.count - self.count_product
        if self.product.count <= 0:
            self.product.delete()
        self.person.save()
        self.product.save()
        return True
