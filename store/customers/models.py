from django.db import models

class Categories(models.Model):
    categoryid = models.SmallIntegerField(primary_key=True)
    categoryname = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    picture = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Customercustomerdemo(models.Model):
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customerid', primary_key=True)
    customertypeid = models.ForeignKey('Customerdemographics', models.DO_NOTHING, db_column='customertypeid')

    class Meta:
        managed = False
        db_table = 'customercustomerdemo'
        unique_together = (('customerid', 'customertypeid'),)


class Customerdemographics(models.Model):
    customertypeid = models.CharField(primary_key=True, max_length=5)
    customerdesc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customerdemographics'


class Customers(models.Model):
    customerid = models.CharField(primary_key=True, max_length=5)
    companyname = models.CharField(max_length=40)
    contactname = models.CharField(max_length=30, blank=True, null=True)
    contacttitle = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Employees(models.Model):
    employeeid = models.SmallIntegerField(primary_key=True)
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=10)
    title = models.CharField(max_length=30, blank=True, null=True)
    titleofcourtesy = models.CharField(max_length=25, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    hiredate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    homephone = models.CharField(max_length=24, blank=True, null=True)
    extension = models.CharField(max_length=4, blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    reportsto = models.ForeignKey('self', models.DO_NOTHING, db_column='reportsto', blank=True, null=True)
    photopath = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Employeeterritories(models.Model):
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='employeeid', primary_key=True)
    territoryid = models.ForeignKey('Territories', models.DO_NOTHING, db_column='territoryid')

    class Meta:
        managed = False
        db_table = 'employeeterritories'
        unique_together = (('employeeid', 'territoryid'),)


class OrderDetails(models.Model):
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='orderid', primary_key=True)
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='productid')
    unitprice = models.FloatField()
    quantity = models.SmallIntegerField()
    discount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'order_details'
        unique_together = (('orderid', 'productid'),)


class Orders(models.Model):
    orderid = models.SmallIntegerField(primary_key=True)
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    orderdate = models.DateField(blank=True, null=True)
    requireddate = models.DateField(blank=True, null=True)
    shippeddate = models.DateField(blank=True, null=True)
    shipvia = models.ForeignKey('Shippers', models.DO_NOTHING, db_column='shipvia', blank=True, null=True)
    freight = models.FloatField(blank=True, null=True)
    shipname = models.CharField(max_length=40, blank=True, null=True)
    shipaddress = models.CharField(max_length=60, blank=True, null=True)
    shipcity = models.CharField(max_length=15, blank=True, null=True)
    shipregion = models.CharField(max_length=15, blank=True, null=True)
    shippostalcode = models.CharField(max_length=10, blank=True, null=True)
    shipcountry = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Products(models.Model):
    productid = models.SmallIntegerField(primary_key=True)
    productname = models.CharField(max_length=40)
    supplierid = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='supplierid', blank=True, null=True)
    categoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='categoryid', blank=True, null=True)
    quantityperunit = models.CharField(max_length=20, blank=True, null=True)
    unitprice = models.FloatField(blank=True, null=True)
    unitsinstock = models.SmallIntegerField(blank=True, null=True)
    unitsonorder = models.SmallIntegerField(blank=True, null=True)
    reorderlevel = models.SmallIntegerField(blank=True, null=True)
    discontinued = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products'


class Region(models.Model):
    regionid = models.SmallIntegerField(primary_key=True)
    regiondescription = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'region'


class Shippers(models.Model):
    shipperid = models.SmallIntegerField(primary_key=True)
    companyname = models.CharField(max_length=40)
    phone = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shippers'


class Suppliers(models.Model):
    supplierid = models.SmallIntegerField(primary_key=True)
    companyname = models.CharField(max_length=40)
    contactname = models.CharField(max_length=30, blank=True, null=True)
    contacttitle = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppliers'


class Territories(models.Model):
    territoryid = models.CharField(primary_key=True, max_length=20)
    territorydescription = models.CharField(max_length=255)
    regionid = models.ForeignKey(Region, models.DO_NOTHING, db_column='regionid')

    class Meta:
        managed = False
        db_table = 'territories'


class Usstates(models.Model):
    stateid = models.SmallIntegerField()
    statename = models.CharField(max_length=100, blank=True, null=True)
    stateabbr = models.CharField(max_length=2, blank=True, null=True)
    stateregion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usstates'