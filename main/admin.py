from django.contrib import admin
from .models import Blog,Coin,Buy_Sell,Mining,Pricing,Blochchain,Guide,Messages
# Register your models here.

@admin.register(Blog)
class OccasionAdmin(admin.ModelAdmin):
    list_display=['title','image','desc','body']

@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','subject','message']

@admin.register(Blochchain)
class BlockAdmin(admin.ModelAdmin):
    list_display=['title','image','desc','body']

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display=['title','image','desc','body']

@admin.register(Buy_Sell)
class BuyAdmin(admin.ModelAdmin):
    list_display=['title','image','desc','body']

@admin.register(Mining)
class MiningAdmin(admin.ModelAdmin):
    list_display=['title','image','desc','body']

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display=['title','image','desc','body']

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display=['name']
