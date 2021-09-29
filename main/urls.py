from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('api', api, name='api'),

    path('bitcoin',bitcoin,name='bitcoin'),
    path('bitcoin/<int:id>/',bitcoin_blog,name='bitcoin_blog'),

    path('dogecoin',dogecoin,name='dogecoin'),
    path('dogecoin/<int:id>/',dogecoin_blog,name='dogecoin_blog'),

    path('ethereum',ethereum,name='ethereum'),
    path('ethereum/<int:id>/',ethereum_blog,name='ethereum_blog'),

    path('ripple',ripple,name='ripple'),
    path('ripple/<int:id>/',ripple_blog,name='ripple_blog'),

    path('buy_sell',buy_sell,name='buy_sell'),
    path('buysell/<int:id>/',buy_sell_blog,name='buyblog'),

    path('mining',mining,name='mining'),
    path('mining/<int:id>/',mining_blog,name='mining_blog'),

    path('pricing',pricing,name='pricing'),
    path('pricing/<int:id>/',pricing_blog,name='pricing_blog'),

    path('blockchain',blockchain,name='blockchain'),
    path('blockchain/<int:id>/',blockchain_blog,name='blockchain_blog'),

    path('guide',guide,name='guide'),
    path('guide/<int:id>/',guide_blog,name='guide_blog'),

    path('convertor',convertor,name='convertor'),

   
    
    

]