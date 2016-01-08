from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from perfis.models import Perfil
from usuarios.forms import RegistrarUsuarioForm

class RegistrarUsuarioView(View):
     template_nome = 'registrar.html'

     def get(self, request):
         return render(request, self.template_nome)

     def post(self, request):
         form = RegistrarUsuarioForm(request.POST)

         if form.is_valid():
             dados_form = form.data
            #Cria o usuario e o perfil
             usuario = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])
             perfil = Perfil(nome=dados_form['nome'],
                             email=dados_form['email'],
                             telefone=dados_form['telefone'],
                             nome_empresa=dados_form['nome_empresa'],
                             usuario=usuario)
             #salva no banco e envia para a pagina principal
             perfil.save()
             return redirect('index')

         return render(request, self.template_nome, {'form': form})