from django.shortcuts import render
from django.views.generic.base import View

class RegistrarUsuarioView(View):
     template_nome = 'registrar.html'

     def get(self, request):
         return render(request, self.template_nome)

     def post(self, request):
         return render(request, self.template_nome)

# Create your views here.


