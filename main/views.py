from django.shortcuts import redirect, render
import requests
import json

from requests.api import request
from .models import Blog, Buy_Sell,Coin,Mining,Pricing,Blochchain,Guide,Messages

# Create your views here.
def home(request):
    coin=Coin.objects.get(name='Bitcoin')
    blog=Blog.objects.filter(category=coin)
    if request.method=='POST':

        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        print(name)
        msg=Messages(name=name,email=email,phone=phone,subject=subject,message=message)
        msg.save()
        return redirect('home')

    url = "https://cryptocurrency-news-and-social-media-indices.p.rapidapi.com/signals/tickerInfo"

    headers = {

        'x-rapidapi-key': "0784f6e946msh25a4daf6fbe2119p124f0djsnb699cbc53e81",
        'x-rapidapi-host': "cryptocurrency-news-and-social-media-indices.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    return render(request,'index.html',{'blog':blog})


# def api(request):
#     url = 'https://www.bitstamp.net/api/ticker/'
#     try:
#         r = requests.get(url, timeout=60)
#         priceFloat = float(json.loads(r.text)['last'])
        
#         print(priceFloat)
#     except:
#         print("Error")
#     return render(request,'api.html',{'price':priceFloat})

def api(request):
    url = 'http://api.coinlayer.com/api/live?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
    try:
        r = requests.get(url, timeout=60)
        priceFloat = float(json.loads(r.text)['rates'])
        
        print(priceFloat)
    except:
        print("Error")
    return render(request,'api.html',{'price':priceFloat})

def bitcoin(request):
    blog=Blog.objects.all()
    coin=Coin.objects.get(name='Bitcoin')
    

    url = 'http://api.coinlayer.com/api/list?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
    url1='http://api.coinlayer.com/api/live?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
        #r = requests.get(url, timeout=60)
        #r=json.load(r)
    response = requests.get(url).json()
    supply=response['crypto']['BCD']['max_supply']
    dogecoin=response['crypto']['DOGE']['max_supply']
    dogeicon=response['crypto']['BCD']['icon_url']


    response1=requests.get(url1).json()
    rates=response1['rates']['BTC']
    doge=response1['rates']['DOGE']

    etc=response['crypto']['ETH']['max_supply']
    etc1=response1['rates']['ETH']

    xrp=response['crypto']['XRP']['max_supply']
    xrp1=response1['rates']['XRP']

    xlm=response['crypto']['XLM']['max_supply']
    xlm1=response1['rates']['XLM']

    data={'supply':supply,
    'rates':rates,
    'dogecoin':dogecoin,
    'doge':doge,
    'dogeicon':dogeicon,
    'etc':etc,
    'etc1':etc1,
    'xrp':xrp,
    'xrp1':xrp1,
    'xlm':xlm,
    'xlm1':xlm1,
    'blog':blog,
    'coin':coin}

    return render(request,'bitcoin.html',data)

def bitcoin_blog(request,id):
    coin=Coin.objects.get(name='Bitcoin')
    print(coin)
    blog=Blog.objects.get(pk=id)
    print(blog.title)
    recent=Blog.objects.all().order_by('-id')
    print(recent)
    category=Coin.objects.all()
    

    url = 'http://api.coinlayer.com/api/list?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
    url1='http://api.coinlayer.com/api/live?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
        #r = requests.get(url, timeout=60)
        #r=json.load(r)
    response = requests.get(url).json()
    supply=response['crypto']['BCD']['max_supply']
    dogecoin=response['crypto']['DOGE']['max_supply']
    dogeicon=response['crypto']['BCD']['icon_url']


    response1=requests.get(url1).json()
    rates=response1['rates']['BTC']
    doge=response1['rates']['DOGE']

    etc=response['crypto']['ETH']['max_supply']
    etc1=response1['rates']['ETH']

    xrp=response['crypto']['XRP']['max_supply']
    xrp1=response1['rates']['XRP']

    xlm=response['crypto']['XLM']['max_supply']
    xlm1=response1['rates']['XLM']

    data={'supply':supply,
    'rates':rates,
    'dogecoin':dogecoin,
    'doge':doge,
    'dogeicon':dogeicon,
    'etc':etc,
    'etc1':etc1,
    'xrp':xrp,
    'xrp1':xrp1,
    'xlm':xlm,
    'xlm1':xlm1,
    'blog':blog,
    'coin':coin,
    'recent':recent,
    'cat':category}
    return render(request,'bitcoin_blog.html',data)

def dogecoin(request):
    coin=Coin.objects.get(name='Dogecoin')
    print(coin)
    blog=Blog.objects.filter(category=coin)
    

    url = 'http://api.coinlayer.com/api/list?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
    url1='http://api.coinlayer.com/api/live?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
        #r = requests.get(url, timeout=60)
        #r=json.load(r)
    response = requests.get(url).json()
    supply=response['crypto']['BCD']['max_supply']
    dogecoin=response['crypto']['DOGE']['max_supply']
    dogeicon=response['crypto']['BCD']['icon_url']


    response1=requests.get(url1).json()
    rates=response1['rates']['BTC']
    doge=response1['rates']['DOGE']

    etc=response['crypto']['ETH']['max_supply']
    etc1=response1['rates']['ETH']

    xrp=response['crypto']['XRP']['max_supply']
    xrp1=response1['rates']['XRP']

    xlm=response['crypto']['XLM']['max_supply']
    xlm1=response1['rates']['XLM']

    data={'supply':supply,
    'rates':rates,
    'dogecoin':dogecoin,
    'doge':doge,
    'dogeicon':dogeicon,
    'etc':etc,
    'etc1':etc1,
    'xrp':xrp,
    'xrp1':xrp1,
    'xlm':xlm,
    'xlm1':xlm1,
    'blog':blog,
    'coin':coin}
    return render(request,'dogecoin.html',data)

def dogecoin_blog(request,id):
    coin=Coin.objects.get(name='Dogecoin')
    print(coin)
    blog=Blog.objects.get(pk=id)
    print(blog.title)
    recent=Blog.objects.all().order_by('-id')
    print(recent)
    category=Coin.objects.all()
    

    url = 'http://api.coinlayer.com/api/list?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
    url1='http://api.coinlayer.com/api/live?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
        #r = requests.get(url, timeout=60)
        #r=json.load(r)
    response = requests.get(url).json()
    supply=response['crypto']['BCD']['max_supply']
    dogecoin=response['crypto']['DOGE']['max_supply']
    dogeicon=response['crypto']['BCD']['icon_url']


    response1=requests.get(url1).json()
    rates=response1['rates']['BTC']
    doge=response1['rates']['DOGE']

    etc=response['crypto']['ETH']['max_supply']
    etc1=response1['rates']['ETH']

    xrp=response['crypto']['XRP']['max_supply']
    xrp1=response1['rates']['XRP']

    xlm=response['crypto']['XLM']['max_supply']
    xlm1=response1['rates']['XLM']

    data={'supply':supply,
    'rates':rates,
    'dogecoin':dogecoin,
    'doge':doge,
    'dogeicon':dogeicon,
    'etc':etc,
    'etc1':etc1,
    'xrp':xrp,
    'xrp1':xrp1,
    'xlm':xlm,
    'xlm1':xlm1,
    'blog':blog,
    'coin':coin,
    'recent':recent,
    'cat':category}
    return render(request,'dogecoin_blog.html',data)


def ethereum(request):
    coin=Coin.objects.get(name='Ethereum')
    print(coin)
    blog=Blog.objects.filter(category=coin)
    

    url = 'http://api.coinlayer.com/api/list?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
    url1='http://api.coinlayer.com/api/live?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
        #r = requests.get(url, timeout=60)
        #r=json.load(r)
    response = requests.get(url).json()
    supply=response['crypto']['BCD']['max_supply']
    dogecoin=response['crypto']['DOGE']['max_supply']
    dogeicon=response['crypto']['BCD']['icon_url']


    response1=requests.get(url1).json()
    rates=response1['rates']['BTC']
    doge=response1['rates']['DOGE']

    etc=response['crypto']['ETH']['max_supply']
    etc1=response1['rates']['ETH']

    xrp=response['crypto']['XRP']['max_supply']
    xrp1=response1['rates']['XRP']

    xlm=response['crypto']['XLM']['max_supply']
    xlm1=response1['rates']['XLM']

    data={'supply':supply,
    'rates':rates,
    'dogecoin':dogecoin,
    'doge':doge,
    'dogeicon':dogeicon,
    'etc':etc,
    'etc1':etc1,
    'xrp':xrp,
    'xrp1':xrp1,
    'xlm':xlm,
    'xlm1':xlm1,
    'blog':blog,
    'coin':coin}
    return render(request,'ethereum.html',data)

def ethereum_blog(request,id):
    coin=Coin.objects.get(name='Ethereum')
    print(coin)
    blog=Blog.objects.get(pk=id)
    print(blog.title)
    recent=Blog.objects.all().order_by('-id')
    print(recent)
    category=Coin.objects.all()
    

    url = 'http://api.coinlayer.com/api/list?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
    url1='http://api.coinlayer.com/api/live?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
        #r = requests.get(url, timeout=60)
        #r=json.load(r)
    response = requests.get(url).json()
    supply=response['crypto']['BCD']['max_supply']
    dogecoin=response['crypto']['DOGE']['max_supply']
    dogeicon=response['crypto']['BCD']['icon_url']


    response1=requests.get(url1).json()
    rates=response1['rates']['BTC']
    doge=response1['rates']['DOGE']

    etc=response['crypto']['ETH']['max_supply']
    etc1=response1['rates']['ETH']

    xrp=response['crypto']['XRP']['max_supply']
    xrp1=response1['rates']['XRP']

    xlm=response['crypto']['XLM']['max_supply']
    xlm1=response1['rates']['XLM']

    data={'supply':supply,
    'rates':rates,
    'dogecoin':dogecoin,
    'doge':doge,
    'dogeicon':dogeicon,
    'etc':etc,
    'etc1':etc1,
    'xrp':xrp,
    'xrp1':xrp1,
    'xlm':xlm,
    'xlm1':xlm1,
    'blog':blog,
    'coin':coin,
    'recent':recent,
    'cat':category}
    return render(request,'ethereum_blog.html',data)




def ripple(request):
    coin=Coin.objects.get(name='Ripple')
    print(coin)
    blog=Blog.objects.filter(category=coin)
    recent=Blog.objects.all().order_by('-id')
    print(recent)
    category=Coin.objects.all()
    

    url = 'http://api.coinlayer.com/api/list?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
    url1='http://api.coinlayer.com/api/live?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
        #r = requests.get(url, timeout=60)
        #r=json.load(r)
    response = requests.get(url).json()
    supply=response['crypto']['BCD']['max_supply']
    dogecoin=response['crypto']['DOGE']['max_supply']
    dogeicon=response['crypto']['BCD']['icon_url']


    response1=requests.get(url1).json()
    rates=response1['rates']['BTC']
    doge=response1['rates']['DOGE']

    etc=response['crypto']['ETH']['max_supply']
    etc1=response1['rates']['ETH']

    xrp=response['crypto']['XRP']['max_supply']
    xrp1=response1['rates']['XRP']

    xlm=response['crypto']['XLM']['max_supply']
    xlm1=response1['rates']['XLM']

    data={'supply':supply,
    'rates':rates,
    'dogecoin':dogecoin,
    'doge':doge,
    'dogeicon':dogeicon,
    'etc':etc,
    'etc1':etc1,
    'xrp':xrp,
    'xrp1':xrp1,
    'xlm':xlm,
    'xlm1':xlm1,
    'blog':blog,
    'coin':coin,
    'recent':recent,
    'cat':category}
    return render(request,'blog.html',data)

def ripple_blog(request,id):
    coin=Coin.objects.get(name='Ripple')
    print(coin)
    blog=Blog.objects.get(pk=id)
    print(blog.title)
    recent=Blog.objects.all().order_by('-id')
    print(recent)
    category=Coin.objects.all()
    

    url = 'http://api.coinlayer.com/api/list?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
    url1='http://api.coinlayer.com/api/live?access_key=30c86d627399476fe4c4c60aa8f8e3bb'
        #r = requests.get(url, timeout=60)
        #r=json.load(r)
    response = requests.get(url).json()
    supply=response['crypto']['BCD']['max_supply']
    dogecoin=response['crypto']['DOGE']['max_supply']
    dogeicon=response['crypto']['BCD']['icon_url']


    response1=requests.get(url1).json()
    rates=response1['rates']['BTC']
    doge=response1['rates']['DOGE']

    etc=response['crypto']['ETH']['max_supply']
    etc1=response1['rates']['ETH']

    xrp=response['crypto']['XRP']['max_supply']
    xrp1=response1['rates']['XRP']

    xlm=response['crypto']['XLM']['max_supply']
    xlm1=response1['rates']['XLM']

    data={'supply':supply,
    'rates':rates,
    'dogecoin':dogecoin,
    'doge':doge,
    'dogeicon':dogeicon,
    'etc':etc,
    'etc1':etc1,
    'xrp':xrp,
    'xrp1':xrp1,
    'xlm':xlm,
    'xlm1':xlm1,
    'blog':blog,
    'coin':coin,
    'recent':recent,
    'cat':category}
    return render(request,'single-blog.html',data)

def buy_sell(request):
    blog=Buy_Sell.objects.all()
    data={'blog':blog}
    return render(request,'buy.html',data)
def buy_sell_blog(request,id):
    blog=Buy_Sell.objects.get(id=id)
    recent=Blog.objects.all().order_by('-id')
    print(recent)
    category=Coin.objects.all()
    data={
        'blog':blog,
        'cat':category,
        'recent':recent,
    }
    return render(request,'buy_blog.html',data)

def mining(request):
    blog=Mining.objects.all()
    data={'blog':blog}
    return render(request,'mining.html',data)

def mining_blog(request,id):
    blog=Mining.objects.get(id=id)
    recent=Blog.objects.all().order_by('-id')
    print(recent)
    category=Coin.objects.all()
    data={
        'blog':blog,
        'cat':category,
        'recent':recent,
    }
    return render(request,'mining_blog.html',data)

def pricing(request):
    blog=Pricing.objects.all()
    data={'blog':blog}
    return render(request,'price.html',data)

def pricing_blog(request,id):
    blog=Pricing.objects.get(id=id)
    recent=Blog.objects.all().order_by('-id')
    print(recent)
    category=Coin.objects.all()
    data={
        'blog':blog,
        'cat':category,
        'recent':recent,
    }
    return render(request,'pricing_blog.html',data)

def blockchain(request):
    blog=Blochchain.objects.all()
    data={'blog':blog}
    return render(request,'blockchain.html',data)

def blockchain_blog(request,id):
    blog=Blochchain.objects.get(id=id)
    recent=Blog.objects.all().order_by('-id')
    print(recent)
    category=Coin.objects.all()
    data={
        'blog':blog,
        'cat':category,
        'recent':recent,
    }
    return render(request,'blockchain_blog.html',data)

def guide(request):
    blog=Guide.objects.all()
    data={'blog':blog}
    return render(request,'guide.html',data)

def guide_blog(request,id):
    blog=Guide.objects.get(id=id)
    recent=Blog.objects.all().order_by('-id')
    print(recent)
    category=Coin.objects.all()
    data={
        'blog':blog,
        'cat':category,
        'recent':recent,
    }
    return render(request,'guide_blog.html',data)


def convertor(request):
    return render(request,'convertor.html')




        
    
        
