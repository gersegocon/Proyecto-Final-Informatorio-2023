import smtplib
import os
from email.message import EmailMessage
import ssl
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm  # Asegúrate de importar tu formulario correctamente

def envio_correo(nombre, email):
    email_remitente = "contacto.viajazos@gmail.com"
    password = "jbqa qhtd swly acdd"
    email_receptor = email
    subject = '¡Gracias por tu mensaje!'
    mensaje = f'Hola {nombre},\n\nGracias por ponerte en contacto con nosotros. Hemos recibido tu mensaje y te responderemos tan pronto como sea posible.\n\nSaludos,\n¡Viajazos!' 
    
    em = EmailMessage()
    em["From"] = '¡Viajazos!'
    em["To"] = email_receptor
    em["Subject"] = subject
    em.set_content(mensaje)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context) as smtp:
        smtp.login(email_remitente, password)
        smtp.sendmail(email_remitente, email_receptor,em.as_string())


class vista_contacto(View):
    template_name = 'contacto.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Obtener los datos del formulario
            email = form.cleaned_data['email']
            nombre = form.cleaned_data['nombre']
            envio_correo(nombre, email)            
            messages.success(request, '¡Tu mensaje se ha enviado correctamente!')
            return redirect('contacto')

        return render(request, self.template_name, {'form': form})

