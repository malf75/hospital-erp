from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from hospital.dados import *

def paciente_directory_path(instance, filename):
    return f'media/images/paciente/{instance.id}/{filename}'

def funcionario_directory_path(instance, filename):
    return f'media/images/funcionario/{instance.id}/{filename}'

def anexos_directory_path(instance, filename):
    return f'media/anexos/paciente/{instance.id}/{filename}'

class Plano(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=False)

class Paciente(models.Model):
    foto = models.ImageField(null=True, blank=True, upload_to=paciente_directory_path)
    nome = models.CharField(max_length=200, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    sexo = models.CharField(max_length=50, choices=sexo_choices, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=True)
    rg = models.CharField(max_length=20, null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(blank=True)
    endereco = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)
    cep = models.CharField(max_length=50, null=False, blank=False)
    plano_saude = models.ManyToManyField(Plano, blank=False)
    numero_carteira = models.CharField(max_length=50, null=False, blank=False)
    data_cadastro = models.DateTimeField(default=timezone.now(), blank=False, null=False)
    status = models.CharField(max_length=50, choices=status, blank=False, null=False)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.OneToOneField(Paciente, null=True, blank=False, on_delete=models.CASCADE)
    motivo_consulta = models.CharField(max_length=50, null=False, blank=False)
    diagnostico = models.TextField(null=False, blank=False)
    prescricao = models.TextField(null=False, blank=False)
        
class Cirurgia(models.Model):
    paciente = models.OneToOneField(Paciente, null=True, blank=False, on_delete=models.CASCADE)
    procedimento = models.CharField(max_length=50, null=False, blank=False)
    data_cirurgia = models.DateTimeField(null=False, blank=False)
    local = models.TextField(null=False, blank=False)
    medico_cirurgiao = models.CharField(max_length=50, null=False, blank=False)
    
class Exame(models.Model):
    paciente = models.OneToOneField(Paciente, null=True, blank=False, on_delete=models.CASCADE)
    tipo_exame = models.CharField(max_length=50, blank=False, null=False)
    resultado = models.TextField(null=True, blank=True)
    data_exame = models.DateTimeField(null=False, blank=False)
    medico_solicitante = models.CharField(max_length=50, null=False, blank=False)
    
class Tratamento(models.Model):
    paciente = models.OneToOneField(Paciente, null=True, blank=False, on_delete=models.CASCADE)
    tipo_tratamento = models.CharField(max_length=50, null=False, blank=False)
    frequencia = models.CharField(max_length=50, null=False, blank=False)
    duracao = models.CharField(max_length=50, null=False, blank=False)
    avaliacao_periodica = models.DateField(null=False, blank=False)

class HistoricoMedico(models.Model):
    id = id = models.IntegerField(primary_key=True, null=False, unique=True, blank=False)
    paciente = models.OneToOneField(Paciente, null=True, blank=False, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now(), blank=False, null=False)
    exame = models.ManyToManyField(Exame, blank=False)
    consulta = models.ManyToManyField(Consulta, blank=False)
    cirurgia = models.ManyToManyField(Cirurgia, blank=False)
    tratamento = models.ManyToManyField(Tratamento, blank=False)
    anexos = models.FileField(upload_to=anexos_directory_path, null=True, blank=True)

def cria_historico(sender, instance, created, **kwargs):
    if created:
        historico_paciente = HistoricoMedico(paciente=instance)
        historico_paciente.save()

post_save.connect(cria_historico, sender=Paciente)