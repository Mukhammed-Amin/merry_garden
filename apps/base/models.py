from django.db import models

# Create your models here.
class Admin(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    phone = models.CharField(max_length=30, verbose_name='Phone number')
    email = models.EmailField(verbose_name='Email')
    location = models.CharField(max_length=255, verbose_name='Location')
    instagram = models.URLField(verbose_name='Instagram')
    twitter = models.URLField(verbose_name='Twitter')
    youtube = models.URLField(verbose_name='YouTube')
    facebook = models.URLField(verbose_name='Facebook')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

class Banner(models.Model):
    banner_title = models.CharField(max_length=20, verbose_name='Banner_title')
    banner_text = models.TextField(verbose_name='Banner text')
    price = models.IntegerField(verbose_name='Price')
    background = models.ImageField(upload_to='banner', verbose_name='Background')
    main_image = models.ImageField(upload_to='main_image', verbose_name='Main image')
    quote = models.TextField(verbose_name="Quote")
    image_1 = models.ImageField(upload_to='image_1', verbose_name='Image 1')
    image_2 = models.ImageField(upload_to='image_2', verbose_name='Image 2')
    mini_description = models.TextField(verbose_name='Mini description')

    def __str__(self) -> str:
        return f"{self.banner_title}"
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    background = models.ImageField(upload_to='back_about_us', verbose_name='Background')
    image_1 = models.ImageField(upload_to='about_us', verbose_name='Name 1')
    image_2 = models.ImageField(upload_to='about_us', verbose_name='Name 2')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    image = models.ImageField(upload_to='news', verbose_name='Image')

    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

class Contact(models.Model):
    id =  models.IntegerField(primary_key= True, blank= True, null= False, verbose_name= 'ID')
    background = models.ImageField(upload_to='contact', verbose_name='Background')
    description = models.TextField(verbose_name='Description')

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class ContactPost(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='Fullname')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=100, verbose_name='Phone number')
    theme = models.CharField(max_length=100, verbose_name='Theme')
    message = models.TextField(verbose_name='Message')

    def __str__(self) -> str:
        return self.fullname
    
    class Meta:
        verbose_name = 'Contact reservation'
        verbose_name_plural = 'Contacts reservation'

class Footer(models.Model):
    id =  models.IntegerField(primary_key= True, blank= True, null= False, verbose_name= 'ID')
    image = models.ImageField(upload_to='footer', verbose_name='Image')
    mini_description = models.TextField(verbose_name='Description')

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Footer Info'
        verbose_name_plural = 'Footer Infos'

class FooterPost(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='Fullname')
    phone = models.CharField(max_length=100, verbose_name='Phone number')
    date = models.CharField(max_length=30, verbose_name='Date')
    adults_quantity = models.IntegerField(verbose_name='Quantity of adults')
    childs_quantity = models.IntegerField(verbose_name='Quantity of children')

    def __str__(self) -> str:
        return self.fullname
    
    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

class Facilties(models.Model):
    icons = (('world', 'world'), ('car', 'car'), ('bed', 'bed'))

    facilty = models.CharField(max_length=25, verbose_name='Facilty')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='facilties', verbose_name='Image')
    icon = models.CharField(max_length=5, choices=icons, verbose_name='Icons')

    def __str__(self) -> str:
        return self.facilty
    
    class Meta:
        verbose_name = 'Facilty'
        verbose_name_plural = 'Facilties'

class Team(models.Model):
    image = models.ImageField(upload_to='team', verbose_name='Image')
    fullname = models.CharField(max_length=100, verbose_name='Full name')
    job = models.CharField(max_length=100, verbose_name='Job')
    email = models.EmailField(verbose_name='Email')
    instagram = models.URLField(verbose_name='Instagram')
    twitter = models.URLField(verbose_name='Twitter')
    facebook = models.URLField(verbose_name='Facebook')
    pinterest = models.URLField(verbose_name='Pinterest')

    def __str__(self) -> str:
        return self.fullname
    
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'