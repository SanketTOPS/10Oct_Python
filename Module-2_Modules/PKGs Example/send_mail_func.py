from django.core.mail import send_mail


sub="Welcome to Python"
msg=f"Hello Students\n\nThis is Email Sending function using Python!\n\nThanks and Regards\n+919724799469"
from_id="sanket.tops@gmail.com"
to_email=["manjusanjli@gmail.com","maulikmeldpara2242@gmail.com"]

send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_email)