from django.db import models
from django.core.mail import send_mail
from django.db import models
import telepot


class Dht(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.temp)

    def save(self, *args, **kwargs):
        if self.temp < 2:
            token = '5830022921:AAFz-iLfWpvRat4yp1Ph8YtZxvpXABYuYAY'
            rece_id = 676259354
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id, ' Temperature du frigo' + str(self.temp))
            print(bot.sendMessage(rece_id, ' La temperature a depasse : ' + str(self.temp)))
            send_mail(
                'temperature depasse la normale ,' + str(self.temp),
                'anomalie dans la machine',
                'chaimaa.zahri@ump.ac.ma',
                ['chourakfarah@gmail.com'],
                fail_silently=False,
            )
        elif self.temp > 8:
            token = '5830022921:AAFz-iLfWpvRat4yp1Ph8YtZxvpXABYuYAY'
            rece_id = 676259354
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id, ' Temperature du frigo' + str(self.temp))
            print(bot.sendMessage(rece_id, ' La temperature a depasse : ' + str(self.temp)))
            send_mail(
                'temperature depasse la normale ,' + str(self.temp),
                'anomalie dans la machine',
                'chaimaa.zahri@ump.ac.ma',
                ['chourakfarah@gmail.com'],
                fail_silently=False,
                )
        return super().save(*args, **kwargs)

# Create your models here.
