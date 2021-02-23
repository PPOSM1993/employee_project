from django.db import models

# Create your models here.

#modelo de datos en el cual se definen los cargos del formulario.
class Position(models.Model):
    title = models.CharField(max_length=50)
    
    
    #Funcion que permite obtener los valores de cada uno de los cargos, provenientes de la base de datos
    #estos serán cargados al combobox del formulario
    def __str__(self):
        return self.title
    


class Employee(models.Model):
    fullname = models.CharField(max_length=150)
    emp_code = models.CharField(max_length=150)
    mobile= models.CharField(max_length=150)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
