from django.db import models

class Maincategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    maincategory = models.ForeignKey(Maincategory,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    stock = models.CharField(max_length=30,default="In Stock",null=True)
    description = models.CharField(max_length=50)
    baseprice = models.IntegerField()
    discount = models.IntegerField(default=0,null=True,blank=True)
    finalprice = models.IntegerField()
    pic1 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    pic2 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    pic3 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    pic4 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)

    def __str__(self):
        return self.name

class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    address3 = models.CharField(max_length=100)
    pin = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pic1 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    otp = models.IntegerField(default=-100005)

    def __str__(self):
        return str(self.id)+" "+self.name
    

class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)+" "+self.user.username+" "+self.product.name
    

status = ((0,"Order Placed"),(1,"Ready To Pack"),(2,"Order Packed"),(3,"Ready To Ship"),(4,"Shipped"),(5,"Out for Delivery"),(6,"Delivered"),(7,"Cancelled"))
payment = ((0,"Pending"),(1,"Done"))
mode = ((0,"COD"),(1,"Netbanking"))
class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    total = models.IntegerField()
    final = models.IntegerField()
    shipping = models.IntegerField()
    rppid = models.CharField(max_length=30,default="",null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    paymentmode = models.IntegerField(choices=mode,default=0)
    paymentstatus = models.IntegerField(choices=payment,default=0)
    orderstatus = models.IntegerField(choices=status,default=0)

    def __str__(self):
        return str(self.id)+" "+self.user.username
    
class CheckoutProducts(models.Model):
    id = models.AutoField(primary_key=True)
    checkout = models.ForeignKey(Checkout,on_delete=models.CASCADE)
    p = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    total= models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+str(self.checkout.id)
    

contactstatus = ((0,'Active'),(1,"Solved"))
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.subject
