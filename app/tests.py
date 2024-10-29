from django.test import TestCase
from app.database import *
from datetime import datetime 

# Create your tests here.
class db_test(TestCase):
    def test_db(self):
        #init_db()
        #add_alarm(datetime.now(), [1,3,5], 2)
        add_user("swss", "dwedwd")
        print('a')
