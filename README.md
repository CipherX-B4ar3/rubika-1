# rubika
rubika client for python 3


# نصب 

```pip install https://github.com/IRMilad/rubika/archive/refs/heads/main.zip```

# مثال 

```python 
import asyncio
from rubika import Client, events, methods


async def main():
    app = Client('rubika')

    @app.on(events.MessageUpdates(func=lambda x: x.message.text == 'hi'))
    async def updates(event):
        await app(
            methods.messages.SendMessage(
                event.object_guid,
                text='hi rubika'
            )
        )

    await app.start(phone_number='98912*******')
    await app.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

# وقت زیادی روی این پروژه نزاشتم و احتمالا مشکلاتی داره هر مشکلی بود داخل [گروه تلگرامم](https://t.me/irtelepy) بگید تا برطرف کنم

سعی کردم تمام متد هارو بنویسم ولی توی بخش ```gadgets.methods.channels``` کمی ضعف هست چون اجازه ساخت کانال بهم نداد

تنها کمبود مهمی که فکر میکنم داشته باشه ویس چت هست که اگر استقبال بشه اضافه میکنم


وقت نوشتن مستندات کامل ندارم از این نظر از شما معدزت میخوام اگر با vs code کد بزنید راحت متوجه میشین چی به چی هست



دوست دار شما میلاد 💚
