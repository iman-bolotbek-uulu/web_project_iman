from shop.models import Item,Purchase
from django.utils import timezone

phone = Item.objects.create(name='Телефон',price=10000)
earphone = Item.objects.create(name='Наушники',price=100)
headphone = Item.objects.create(name='Головные наушники',price=1000)
laptop = Item.objects.create(name='Ноутбук',price=100000)
tablet = Item.objects.create(name='Планшет',price=10000)
charger = Item.objects.create(name='Зарядка',price=5000)
watch = Item.objects.create(name='Часы',price=15000)
glasses = Item.objects.create(name='Очки',price=6000)
column = Item.objects.create(name='Колонка',price=50000)
case = Item.objects.create(name='Чехол',price=200)


phone.purchases.create(name='Some some1',age=20,date_purchase=timezone.now())
earphone.purchases.create(name='Some some2',age=21,date_purchase=timezone.now())
headphone.purchases.create(name='Some some3',age=22,date_purchase=timezone.now())
laptop.purchases.create(name='Some some4',age=23,date_purchase=timezone.now())
tablet.purchases.create(name='Some some5',age=24,date_purchase=timezone.now())
charger.purchases.create(name='Some some6',age=25,date_purchase=timezone.now())
watch.purchases.create(name='Some some7',age=26,date_purchase=timezone.now())
glasses.purchases.create(name='Some some8',age=27,date_purchase=timezone.now())
column.purchases.create(name='Some some9',age=28,date_purchase=timezone.now())
case.purchases.create(name='Some some10',age=29,date_purchase=timezone.now())
case.purchases.create(name='Some some11',age=30,date_purchase=timezone.now())
column.purchases.create(name='Some some12',age=31,date_purchase=timezone.now())
glasses.purchases.create(name='Some some13',age=32,date_purchase=timezone.now())
watch.purchases.create(name='Some some14',age=33,date_purchase=timezone.now())
charger.purchases.create(name='Some some15',age=34,date_purchase=timezone.now())
tablet.purchases.create(name='Some some16',age=35,date_purchase=timezone.now())
laptop.purchases.create(name='Some some17',age=36,date_purchase=timezone.now())
headphone.purchases.create(name='Some some18',age=37,date_purchase=timezone.now())
earphone.purchases.create(name='Some some19',age=38,date_purchase=timezone.now())
phone.purchases.create(name='Some some20',age=39,date_purchase=timezone.now())

phone.purchases.all()
earphone.purchases.all()
headphone.purchases.all()
laptop.purchases.all()
tablet.purchases.all()
case.purchases.all()
charger.purchases.all()
column.purchases.all()
glasses.purchases.all()
watch.purchases.all()






