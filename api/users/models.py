from django.db import models
import uuid
import bcrypt
import time 
from datetime import datetime

# Create your models here.

class User(models.Model):
    unique_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email_id = models.TextField(blank=False)
    password_id = models.TextField(blank=False)
    timezone_id = models.TextField(blank=False)
    time_id = models.TextField(blank=False)
    entry_time = models.DateTimeField(default= datetime.now)


    def encrypt_password(self,password):
        password = str(password).encode('utf-8')
        hash_password = bcrypt.hashpw(password,bcrypt.gensalt())
        return hash_password

    def getTime(self):
        return time.time()

    def set_user(self,email_id,password_id,timezone_id):
        self.email_id = email_id
        self.password_id = self.encrypt_password(password_id)
        self.timezone_id = timezone_id
        self.time_id = self.getTime()


