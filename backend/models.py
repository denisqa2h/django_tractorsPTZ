from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    Role = models.CharField(max_length=50,blank=False, default="Visitor")
    #Json format
    AccesList = models.CharField(max_length=1000,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username



#Таблица типов инцидентов
class AccidentsType(models.Model):
    TypeName = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.Type

class Buttons(models.Model):
    # Тип кнопки (1-Зеленая, 2-Желтая, 3-Красная)
    Btype = models.IntegerField(blank=False)
    # Метка времени события
    TimeStamp = models.DateTimeField(blank=True, auto_now=True, null=True)
    # Количесвто нажатий зеленой кнопки
    Counter1 = models.IntegerField(blank=True)
    # Количесвто нажатий желтой кнопки
    Counter2 = models.IntegerField(blank=True)
    # Количесвто нажатий красной кнопки
    Counter3 = models.IntegerField(blank=True)

    def __str__(self):
        return (self.Btype,self.TimeStamp, self.Counter1, self.Counter2, self.Counter3)


#Таблица инцидентов
class Accidents(models.Model):
    Post = models.CharField(max_length=20,blank=False)
    Description = models.TextField(blank=True, null=True)
    FixTime = models.DateTimeField(auto_now_add=True)
    EndTime = models.DateTimeField(blank=True, null=True)

    Type = models.ForeignKey(AccidentsType,on_delete=models.CASCADE, blank=True, null=True)


    # #Внешний ключ на таблицу событий кнопок
    # BEvent = models.ForeignKey(ButtonsEvent,on_delete=models.CASCADE)


