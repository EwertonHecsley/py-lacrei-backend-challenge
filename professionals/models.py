from django.db import models

class Professsional(models.Model):
    name = models.CharField("Nome Social", max_length=100)
    profession = models.CharField("Profissão", max_length=100)
    address = models.CharField("Endereço", max_length=200)
    contact = models.CharField("Contato", max_length=100)
    
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.profession}"
    
