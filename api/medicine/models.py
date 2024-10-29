from django.db import models



class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Generic(Timestamp):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self) -> str:
        return self.name
    

class Manufacturer(Timestamp):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = "Manufacturers/Brands"

    def __str__(self) -> str:
        return self.name


class Medicine(Timestamp):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    generic = models.ForeignKey(Generic, on_delete=models.CASCADE)
    generic_unit = models.CharField(
        max_length=20,
        help_text='Amount of generic such as 600gm, 700gm'
    )
    name = models.CharField(max_length=150)
    no_of_tablets = models.IntegerField(help_text='Number of tablets in a strip')
    price = models.IntegerField()
    batch_number = models.CharField(max_length=10)
    description = models.TextField()

    class Meta:
        ordering = ('name', )

    def __str__(self) -> str:
        return f"{self.name} - {self.generic.name} {self.generic_unit}"