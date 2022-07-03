# rubika (beta-22.7.3)
rubika client for python 3


# نصب 

```pip install https://github.com/IRMilad/rubika/archive/refs/heads/main.zip```

# مثال 

```python 
import asyncio
from rubika import Client, models, handlers


async def main():
    async with Client(session='rubika') as client:
        @client.on(handlers.MessageUpdates(models.author_guid() == client._guid))
        async def updates(update):
            await update.reply('`hello` __from__ **rubika**')
        await client.run_until_disconnected()

asyncio.run(main())
```

# وقت زیادی روی این پروژه نزاشتم و احتمالا مشکلاتی داره هر مشکلی بود داخل [گروه تلگرامم](https://t.me/irtelepy) بگید تا برطرف کنم

سعی کردم تمام متد هارو بنویسم ولی توی بخش ```gadgets.methods.channels``` کمی ضعف هست چون اجازه ساخت کانال بهم نداد

تنها کمبود مهمی که فکر میکنم داشته باشه ویس چت هست که اگر استقبال بشه اضافه میکنم


وقت نوشتن مستندات کامل ندارم از این نظر از شما معدزت میخوام اگر با vs code کد بزنید راحت متوجه میشین چی به چی هست تا مستندات اماده بشه


دوست دار شما میلاد 💚
