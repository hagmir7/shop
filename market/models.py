from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.forms.models import model_to_dict



class IpAddress(models.Model):
    ip = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    ip_add = models.GenericIPAddressField()

    def __str__(self):
        return self.ip


user_type = (('Male', 'Male'), ('Female', 'Female'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar', default='user-default.png', blank=True)
    likes = models.ManyToManyField(User, related_name='user_likes', blank=True)
    phone = models.IntegerField()
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    views = models.ManyToManyField(IpAddress, related_name='user_views', blank=True)
    gerand = models.CharField(choices=user_type, max_length=50)
    is_blocked = models.BooleanField(default=False, blank=True)
    is_admin = models.BooleanField(default=False, blank=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)
    verificated = models.BooleanField(default=False)



class Stor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    admins = models.ManyToManyField(User, related_name='admin_stor')
    name = models.CharField(verbose_name="Stor name ", max_length=100)
    likes = models.ManyToManyField(User, related_name='stor_likes', blank=True)
    category = models.CharField(max_length=300)
    description = models.TextField()
    avatar = models.ImageField(upload_to='avatar_stor')
    cover = models.ImageField(upload_to='cover_stor')
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    views = models.ManyToManyField(IpAddress, related_name='stor_views')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    admin = models.ManyToManyField(User, related_name='group_admin')
    date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='group_cover', blank=True)
    description = models.TextField(max_length=700)
    category = models.CharField(max_length=600)


    def __str__(self):
        return self.name

        
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stor = models.ForeignKey(Stor, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)

    image_1 = models.ImageField(upload_to='proudct_image')
    image_2 = models.ImageField(upload_to='proudct_image')
    image_3 = models.ImageField(upload_to='proudct_image', blank=True)
    image_4 = models.ImageField(upload_to='proudct_image', blank=True)
    image_5 = models.ImageField(upload_to='proudct_image', blank=True)

    price = models.FloatField()
    old_price = models.FloatField()
    views = models.ForeignKey(IpAddress, on_delete=models.CASCADE)
    is_kg = models.FloatField(blank=True, null=True)
    is_g = models.FloatField(blank=True, null=True)
    is_l = models.FloatField(blank=True, null=True)
    shiping_info = models.TextField()
    descriptioin = models.TextField()
    likes = models.ManyToManyField(User, related_name='product_likes', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(blank=True, null=True)


    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    city = models.CharField(max_length=100, blank=True, null=True)
    code_postal = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    is_verify = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name


class ProductCat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    proudcts = models.ManyToManyField(ProductCat, related_name='products_cart', blank=True)

    def __str__(self):
        return self.user



class OrderCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='order_cart')
    date = models.DateTimeField(auto_now_add=True)
    is_verify = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.user


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    image_1 = models.ImageField(upload_to='post_image', blank=True)
    image_2 = models.ImageField(upload_to='post_image', blank=True)
    image_3 = models.ImageField(upload_to='post_image', blank=True)
    image_4 = models.ImageField(upload_to='post_image', blank=True)

    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    views = models.ManyToManyField(IpAddress, related_name='post_views')
    likes = models.ManyToManyField(User, related_name='like_post')
    is_blocked = models.BooleanField(default=False)

    def __init__(self):
        return self.user








