from django.db import models
from django.contrib.auth.models import User

# The second part it's going to be display in the front-end and the first part it's going to be used in the back-end
MEAL_TYPE: tuple = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts'),
)

STATUS: tuple = (
    (0, 'Unavailable'),
    (1, 'Available')
)


class Item(models.Model):
    meal = models.CharField(max_length=500, unique=True)  # Com isto, não vou ter valores duplicados
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    # É mais inteligente definir choices, pois vai ser sempre igual, as escolhas são limitadas!!!
    category = models.CharField(choices=MEAL_TYPE, max_length=200)
    # This field establishes a many-to-one relationship between the model that contains this field and the `User` model.
    # This allows you to associate an author with each instance of the model, and retrieve the related `User` instance
    # when needed.
    # on_delete permite a possibilidade de remover um User. Isto é, se um certo cozinheiro já não está no restaurante, é
    # possível retirar todas os seus meals do menu!!
    # Se tivesse colocado on_delete=models.PROTECT, iria ser impossível apagar the data!!!
    # on_delete=models.SET_NULL permite colocar Null no author
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
