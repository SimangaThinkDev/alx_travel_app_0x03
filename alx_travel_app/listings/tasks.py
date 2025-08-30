from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from email.mime.text import MIMEText
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


@shared_task
def send_confirmation_email( recipient_email:str ):
    """
    This function sends a confirmation email 
    to specified user when called
    """
    email_subject = "Welcome To The ALX Travel App"
    email_body = f"""
    Hello, {recipient_email.split("@")[0]}.
    Again Welcome to the ALX Travel App, We are happy to have you on board.

    Use this email to ask questions if you have any
    regards: our_amazing_team
    """
    host_email = settings.EMAIL_HOST_PASSWORD

    # Set-Up the email job
    try:
        send_mail(
            email_subject,
            email_body,
            host_email,
            [recipient_email],
            fail_silently=False, # We kinda wanna debug this so ya
        )
    except BadHeaderError:
        return HttpResponse("Invalid header found.")

