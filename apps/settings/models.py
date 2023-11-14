from django.db import models

# Create your models here.
class InfoUser(models.Model):
    image = models.ImageField(
        upload_to="image_user/",
        verbose_name="фото"

    )
    name = models.CharField(
        max_length=100,
        verbose_name="ФИО"      
    )
    work = models.CharField(
        max_length=50,
        verbose_name="Введите профессию"
    )
    descriptions = models.TextField(
        verbose_name="Введите биографию"

    )
    def __str__(self):
       return self.name
    
    class Meta:
        verbose_name = "информиция пользователя"
        verbose_name_plural = "информиция пользователя"

class About(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name="имя"
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="фамилия"
    )
    age = models.CharField(
        max_length=255,
        verbose_name="возраст"
    )
    nation = models.CharField(
        max_length=255,
        verbose_name="нация"
    )
    addres = models.CharField(
        max_length=255,
        verbose_name="адрес"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="телефон номер"
    )
    email = models.CharField(
        max_length=255,
        verbose_name="почта"
    )
    telegram = models.CharField(
        max_length=255,
        verbose_name="username телеграм"
   
    )
    language = models.CharField(
        max_length=255,
        verbose_name="знание языка"
    )
    year = models.CharField(
        max_length=255,
        verbose_name="годы опыта"
    )
    project = models.CharField(
        max_length=255,
        verbose_name="завершенные проекты"
    )
    clients = models.CharField(
        max_length=255,
        verbose_name="счастливые клиенты"
    )
    awards = models.CharField(
        max_length=255,
        verbose_name="полученные награды"
    )
    def __str__(self):
       return f'({self.first_name} - {self.last_name})'
    
    class Meta:
        verbose_name = "обо мне"
        verbose_name_plural = "обо мне"


class Skiils(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="название"
    )
    number = models.CharField(
        max_length=255,
        verbose_name="процент"
    )

    def __str__(self):
        return f"{self.title} - {self.number}"
    
    class Meta:
        verbose_name = "мои скилы"
        verbose_name = "мой скил"

class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="имя"
    )
    email = models.CharField(
        max_length=255,
        verbose_name="почта"
    )
    message = models.CharField(
        max_length=255,
        verbose_name="сообщение"
    )
    def __str__(self):
        return f"{self.name} -- {self.email}"
    
    class Meta:
        verbose_name = "обратная связь"
        verbose_name_plural = "обратная связь"

class Experience(models.Model):
    year = models.CharField(
        max_length=255,
        verbose_name="год"
    )
    profession = models.CharField(
        max_length=255,
        verbose_name="профессия"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="описание"
    )
    place_of_work= models.CharField(
        max_length=255,
        verbose_name="место работы"
    )
    year2 = models.CharField(
        max_length=255,
        verbose_name="год",
        blank=True, null=True
    )
    profession2 = models.CharField(
        max_length=255,
        verbose_name="профессия",
        blank=True, null=True
    )
    description2 = models.CharField(
        max_length=255,
        verbose_name="описание",
        blank=True, null=True
    )
    place_of_work2= models.CharField(
        max_length=255,
        verbose_name="место работы",
        blank=True, null=True
    )
        
    def __str__(self):
        return f"{self.year} - {self.profession}"
    
    class Meta:
        verbose_name = "стаж"
        verbose_name_plural = "стажи"

class Blog(models.Model):
    image = models.ImageField(
        upload_to='blog/',
        verbose_name="фото"
    )
    
    title = models.CharField(
        max_length=255,
        verbose_name="название"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="описание"
    )
    def __str__(self):
        return f"{self.year} - {self.profession}"
    
    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"


class Portfolio(models.Model):
    project_name = models.CharField(
        max_length=255,
        verbose_name='название проекта'
    )
    project = models.CharField(
        max_length=255,
        verbose_name="проект"
    )
    clients = models.CharField(
        max_length=255,
        verbose_name="клиенты"
    )
    language = models.CharField(
        max_length=255,
        verbose_name="язык"
    )
    preview = models.CharField(
        max_length=255,
        verbose_name="предварительный просмотр"
    )
    def __str__(self):
        return f"{self.project_name} -- {self.project}"
    
    class Meta:
        verbose_name = "портфолио"
        verbose_name_plural = "портфолии"
   