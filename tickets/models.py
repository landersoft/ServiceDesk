from django.db import models

# Create your models here.
class Ticket(models.Model):
    

    SI = 'Si'
    NO = 'No'
    SOL_CAU = [
        (SI, 'SI'),
        (NO,'NO'),
    ]

    ABIERTO = 'AB'
    CERRADO = 'CE'
    PROCESO ='EP'
    estado = [
        (ABIERTO, 'Abierto'),
        (CERRADO, 'Cerrado'),
        (PROCESO, 'En Proceso')
    ]


    TALCA = 'ITA'
    TOBALABA = 'ITO'


    centros = [
        (TALCA, 'ITA'),
        (TOBALABA, 'ITO'),
        
    ]


    afortoul ='afortoul-ext@adexus.cl'
    cpalacios ='cpalacios-ext@adexus.cl'
    fgarcia ='fgarcia-ext@adexus.cl'
    gmoreno = 'gmoreno-ext@adexus.cl'
    icuevas = 'icuevas-ext@adexus.cl'
    jrausseo = 'jrausseo-ext@adexus.cl'
    kgomez = 'kgomez-ext@adexus.cl'
    rlopez = 'rlopez-ext@adexus.cl'
    rmontoya = 'rmontoya-ext@adexus.cl'
    rparra = 'rparra-ext@adexus.cl'
    ssepulveda = 'ssepulveda-ext@adexus.cl'
    tcabello = 'tcabello-ext@adexus.cl'
    usuariobupa = 'usuario@bupa.cl'
    vithal ='vithal-ext@adexus.cl'
    yquintero = 'yquintero-ext@adexus.cl'
    N2 = 'N2'
    hjouayed = 'hjouayed-ext@adexus.cl'
    spadron = 'spadron-ext@adexus.cl'
    mlovera = 'mlovera-ext@adexus.cl'
    agarcia = 'agarcia-ext@adexus.cl'
    asegura = 'asegura-ext@adexus.cl'

    analista = [
        (afortoul, 'afortoul-ext@adexus.cl'),
        (cpalacios, 'cpalacios-ext@adexus.cl'),
        (fgarcia ,'fgarcia-ext@adexus.cl'),
        (gmoreno , 'gmoreno-ext@adexus.cl'),
        (icuevas , 'icuevas-ext@adexus.cl'),
        (jrausseo , 'jrausseo-ext@adexus.cl'),
        (kgomez , 'kgomez-ext@adexus.cl'),
        (rlopez , 'rlopez-ext@adexus.cl'),
        (rmontoya , 'rmontoya-ext@adexus.cl'),
        (rparra , 'rparra-ext@adexus.cl'),
        (ssepulveda , 'ssepulveda-ext@adexus.cl'),
        (tcabello , 'tcabello-ext@adexus.cl'),
        (usuariobupa , 'usuario@bupa.cl'),
        (vithal ,'vithal-ext@adexus.cl'),
        (yquintero , 'yquintero-ext@adexus.cl'),
        (N2 , 'N2'),
        (hjouayed , 'hjouayed-ext@adexus.cl'),
        (spadron , 'spadron-ext@adexus.cl'),
        (mlovera , 'mlovera-ext@adexus.cl'),
        (agarcia , 'agarcia-ext@adexus.cl'),
        (asegura , 'asegura-ext@adexus.cl'),

        
    ]


    Eduardo_Lizarde = 'Eduardo Lizarde'
    Erwin_Vasquez = 'Erwin Vasquez'
    Flavio_Caniumil = 'Flavio Caniumil'
    Luis_Alfaro = 'Luis Alfaro'
    Miguel_Aguilera = 'Miguel Aguilera'
    Mauricio_Alarcon = 'Mauricio Alarcon'
    Rodrigo_Lander = 'Rodrigo Lander'
    Nurieth_Vega = 'Nurieth Vega'
    Francisco_Salinas = 'Francisco Salinas'
    Oscar_Retamal = 'Oscar Retamal'
    Constanza_Aguilar = 'Constanza Aguilar'
    Marcelo_Romero = 'Marcelo Romero'
    Francisco_Labarca = 'Francisco Labarca'
    Felipe_Mella = 'Felipe Mella'
    Fernando_Sanchez = 'Fernando Sanchez'
    Carlos_Caceres = 'Carlos Caceres'
    Oscar_Muñoz = 'Oscar Muñoz'
    Manuel_Pereira = 'Manuel Pereira'
    Claudio_Reyes = 'Claudio Reyes'
    Cesar_Cortez = 'Cesar Cortez'
    Alejandro_Jeria = 'Alejandro Jeria'

    asignatario = [

        
        (Eduardo_Lizarde ,'Eduardo Lizarde'),
        (Erwin_Vasquez ,'Erwin Vasquez'),
        (Flavio_Caniumil ,'Flavio Caniumil'),
        (Luis_Alfaro ,'Luis Alfaro'),
        (Miguel_Aguilera ,'Miguel Aguilera'),
        (Mauricio_Alarcon , 'Mauricio Alarcon'),
        (Rodrigo_Lander , 'Rodrigo Lander'),
        (Nurieth_Vega , 'Nurieth Vega'),
        (Francisco_Salinas , 'Francisco Salinas'),
        (Oscar_Retamal , 'Oscar Retamal'),
        (Constanza_Aguilar , 'Constanza Aguilar'),
        (Marcelo_Romero , 'Marcelo Romero'),
        (Francisco_Labarca , 'Francisco Labarca'),
        (Felipe_Mella , 'Felipe Mella'),
        (Fernando_Sanchez , 'Fernando Sanchez'),
        (Carlos_Caceres , 'Carlos Caceres'),
        (Oscar_Muñoz , 'Oscar Muñoz'),
        (Manuel_Pereira , 'Manuel Pereira'),
        (Claudio_Reyes , 'Claudio Reyes'),
        (Cesar_Cortez , 'Cesar Cortez'),
        (Alejandro_Jeria , 'Alejandro Jeria'),
    ]




    BUPA_CL_NIVEL2 = 'BUPA-CL-NIVEL 2'
    BUPA_CL_CLINICA = 'BUPA-CL-CLINICA'
    BUPA_CL_SOPORTE_ONSITE_CASA_MATRIZ = 'BUPA-CL-SOPORTE ONSITE CASA MATRIZ'
    BUPA_CL_SOPORTE_ONSITE_LA_CONCEPCION = 'BUPA-CL-SOPORTE ONSITE CASA MATRIZ'
    BUPA_CL_SOPORTE_ONSITE_MONEDA = 'BUPA-CL-SOPORTE ONSITE MONEDA'
    ADX_CL_BUPA_SOPORTE_TERRENO_METROPOLITANO = 'ADX-CL-BUPA-SOPORTE TERRENO METROPOLITANO'
    ADX_CL_BUPA_SOPORTE_TERRENO_REGIONAL = 'ADX-CL-BUPA-SOPORTE TERRENO REGIONAL'
    ADX_CL_BUPA_MESA_DE_AYUDA = 'ADX-CL-BUPA-MESA DE AYUDA'
    TOTALPACK = 'TOTALPACK'
    BUPA_CL_TELECOMUNICACIONES = 'BUPA-CL-TELECOMUNICACIONES'
    BUPA_CL_AMBIENTES_COLABORATIVOS_IT = 'BUPA-CL-AMBIENTES COLABORATIVOS IT'
    BUPA_CL_SEGURIDAD_DE_LA_INFORMACION_IT = 'BUPA-CL-SEGURIDAD DE LA INFORMACION IT' 





    grupo = [
        (BUPA_CL_NIVEL2 , 'BUPA-CL-NIVEL 2'),
        (BUPA_CL_CLINICA , 'BUPA-CL-CLINICA'),
        (BUPA_CL_SOPORTE_ONSITE_CASA_MATRIZ ,'BUPA-CL-SOPORTE ONSITE CASA MATRIZ'),
        (BUPA_CL_SOPORTE_ONSITE_LA_CONCEPCION , 'BUPA-CL-SOPORTE ONSITE CASA MATRIZ'),
        (BUPA_CL_SOPORTE_ONSITE_MONEDA , 'BUPA-CL-SOPORTE ONSITE MONEDA'),
        (ADX_CL_BUPA_SOPORTE_TERRENO_METROPOLITANO ,'ADX-CL-BUPA-SOPORTE TERRENO METROPOLITANO'),
        (ADX_CL_BUPA_SOPORTE_TERRENO_REGIONAL , 'ADX-CL-BUPA-SOPORTE TERRENO REGIONAL'),
        (ADX_CL_BUPA_MESA_DE_AYUDA , 'ADX-CL-BUPA-MESA DE AYUDA'),
        (TOTALPACK , 'TOTALPACK'),
        (BUPA_CL_TELECOMUNICACIONES , 'BUPA-CL-TELECOMUNICACIONES'),
        (BUPA_CL_AMBIENTES_COLABORATIVOS_IT , 'BUPA-CL-AMBIENTES COLABORATIVOS IT'),
        (BUPA_CL_SEGURIDAD_DE_LA_INFORMACION_IT , 'BUPA-CL-SEGURIDAD DE LA INFORMACION IT'), 

    ]














    fecha = models.DateField()
    ccmm = models.CharField(max_length=5,choices=centros, default = TALCA)
    ticket = models.CharField(max_length=10)
    analista = models.EmailField(choices = analista)
    resumen = models.CharField(max_length=250)
    asignatario = models.CharField(max_length=100, choices=asignatario)
    estado = models.CharField(max_length=2, choices=estado, default= ABIERTO)
    grupo_resolutor = models.CharField(max_length=20, choices=grupo, default = BUPA_CL_NIVEL2)
    fecha_derivacion = models.DateField()
    solucionable_cau = models.CharField(max_length=2, choices=SOL_CAU, default = NO)
    comentario = models.CharField(max_length=250, null=True)

    class Meta:
        ordering = ["asignatario"]
        verbose_name = 'Tickets'
        verbose_name_plural = 'Tickets'

        def __str__(self):
            return str(self.asignatario)