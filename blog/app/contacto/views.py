from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm  # Asegúrate de importar tu formulario correctamente

class vista_contacto(View):
    template_name = 'contacto.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('contacto')

        return render(request, self.template_name, {'form': form})

