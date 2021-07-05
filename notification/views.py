import json
from datetime import datetime
from django.utils import timezone

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time

from Notifications_Reciver.models import Service
from backend.Email_notifications import Email
from backend.Save_Entity_To_DB import Save_Notification_To_Db, Update_Entity_On_Db, Retrive_Notification_From_Db
from threading import *

last_notification_time = time.mktime(time.localtime())
tabl = Retrive_Notification_From_Db("services")


@csrf_exempt
def notifications_handler(request):
    if request.method == 'POST':
        print("\n new notification received\n")
        json_body = json.loads(request.body)
        print(json_body)
        data = json_body["data"][0]
        Save_Notification_To_Db(json_body, data["type"])
        service = Service(id= data["id"], type=data["type"],name=data["id"].split(":")[-1])
        service.save()
        #Save_Notification_To_Db({"_id":data["id"], "notifiedAt": datetime.strptime(json_body["notifiedAt"], '%Y-%m-%dT%H:%M:%SZ')}, "services")
        # parser
        #tabl.update({data["id"]: datetime.strptime(json_body["notifiedAt"], '%Y-%m-%dT%H:%M:%SZ')})
        #print(tabl)
        global last_notification_time
        last_notification_time = time.mktime(time.localtime())
    return HttpResponse('waiting for notifications..... ')


def controler():
    while True:
        now = timezone.now()
        time.sleep(15)
        #if t > (last_notification_time + 1800) and t < (last_notification_time + 2900):
        #    Email(message="The Context Broker is not sending notifications!!")

        Service.objects.filter(date__lt=now).update(status='inactive')

t1 = Thread(target=controler)
t1.start()