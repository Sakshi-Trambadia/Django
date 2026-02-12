from django.db import models



class User(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    userName = models.CharField
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=20)   # Admin / Seller / Bidder
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=100)
    address = models.TextField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.seller_name


class Bidder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    auction_start = models.DateTimeField()
    auction_end = models.DateTimeField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.product_name


class Auction(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    min_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    auction_status = models.CharField(max_length=20)

    def __str__(self):
        return self.product.product_name


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)#id
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.bid_amount)


class Payment(models.Model):
    auction = models.OneToOneField(Auction, on_delete=models.CASCADE)
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=30)
    payment_status = models.CharField(max_length=20)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_status

