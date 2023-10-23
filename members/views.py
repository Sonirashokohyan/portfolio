from django.shortcuts import render,redirect
from .models import projects
# from .models import projects
from django.conf import settings
from django.http import FileResponse
import os
import smtplib
from email.message import EmailMessage
from django.contrib import messages

def home(request):
  if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message1 = request.POST.get('message')
        email = request.POST.get('email')
        message=f"""
Dear Sonira Shokohyan,

I hope this email finds you well. Kindly find the details of the submission below:

Message: {message1}
Name: {name}
Phone: {phone}
Email:{email}"""
        recipient = 'sonira.shokoyan123@gmail.com'

        # Create the email message
        email = EmailMessage()
        email['Subject'] = name
        email['From'] = settings.EMAIL_HOST_USER
        email['To'] = recipient
        email.set_content(message)

        # Send the email using SMTP
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as smtp:
            smtp.starttls()
            smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            smtp.send_message(email)

        return redirect('/success/')
  project=projects.objects.all()
  data2={
     'projects':project
  }
  return render(request,'index.html',data2)


def success(request):
    return render(request,'success.html')
def download_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'sonira.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True)


# def download_pdf(request):
#     file_path = os.path.join(settings.MEDIA_ROOT, 'sonira.pdf')
#     with open(file_path, 'rb') as file:
#         response = FileResponse(file, as_attachment=True)
#         return response