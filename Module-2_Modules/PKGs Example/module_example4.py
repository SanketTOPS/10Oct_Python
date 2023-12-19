import pyqrcode

url="https://studygyaan.com/django/host-django-website-application-for-free-in-5-minutes"


qr=pyqrcode.create(url)

qr.png('myqr.png')

