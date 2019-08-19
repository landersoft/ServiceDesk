from django.db import models

# Create your models here.


class CCMM(models.Model):
    sigla = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100, null = True)
    def __str__(self):
        return str(self.sigla)


class Analista(models.Model):
    correo = models.EmailField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return str(self.correo)


class Asignatario(models.Model):
    nombre = models.CharField(max_length=100,primary_key=True)
    correo = models.EmailField(null=True, blank=True)

    def __str__(self):
        return str(self.nombre)


class Grupo(models.Model):
    nombre = models.CharField(max_length=100,primary_key=True)
    correo = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return str(self.nombre)



class Ticket(models.Model):
    

    SI = 'Si'
    NO = 'No'
    SOL_CAU = [
        (SI, 'SI'),
        (NO,'NO'),
    ]

    ABIERTO = 'AB'
    CERRADO = 'CE'
    PENDIENTE ='PE'
    estado = [
        (ABIERTO, 'En Curso'),
        (CERRADO, 'Cerrado'),
        (PENDIENTE, 'Pendiente')
    ]
    
    fecha = models.DateField()
    ccmm = models.ForeignKey(CCMM, on_delete=models.CASCADE)
    ticket = models.CharField(max_length=10)
    analista = models.ForeignKey(Analista, on_delete=models.CASCADE)
    resumen = models.CharField(max_length=250)
    asignatario = models.ForeignKey(Asignatario,on_delete=models.CASCADE)
    estado = models.CharField(max_length=2, choices=estado, default= ABIERTO)
    grupo_resolutor = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    fecha_derivacion = models.DateField(null=True, blank=True)
    solucionable_cau = models.CharField(max_length=2, choices=SOL_CAU, default = NO)
    comentario = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ["asignatario"]
        verbose_name = 'Tickets'
        verbose_name_plural = 'Tickets'

        def __str__(self):
            return str(self.asignatario)



