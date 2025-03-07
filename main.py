import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard
from datacenter.models import Visit
import datetime  # noqa: E402

if __name__ == '__main__':
    all_visit = Visit.objects.all()
# Программируем здесь
    def get_duration(visit):
        if visit.leaved_at
            return = visit.leaved_at - visit.entered_at
        else:
            return datetime.now() - visit.entered_at

    def is_visit_long(visit, minutes=10):
        return get_duration(visit).total.seconds() > minutes * 60

    
    all_passcards = Passcard.objects.all()
    active_passcards = []
    active_passcards = Passcard.objects.filter(is_active=True)
    some_passcards = active_passcards[0]
    one_person_visit = Visit.objects.filter(passcard=some_passcards)

    



     

    print("все визиты одного", one_person_visit) 
    print("Визиты дольше 10 минут", )
    print("Визиты дольше 1000 минут",)   
    #print("Какой то пропуск", some_passcards)
    #print("Всего пропусков", (all_passcards))
    #print("Активные пропуска", (active_passcards))
      
