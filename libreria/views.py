from http.client import HTTPResponse
from django.views.generic import *
from django.shortcuts import render
from .models import *
from django.http import HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
    template_name = 'home.html'
#-----------------------------------------------------------------------------------------------
#Autor
class AutorPageView(LoginRequiredMixin, ListView):
    template_name = 'autor.html'
    model = Autor
    context_object_name = 'Todos_Los_Autores'
    login_url = 'login'

class AutorPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'autor_detalle.html'
    model = Autor
    context_object_name = 'Detalle_Autor'
    login_url = 'login'


class AutorPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'autor_nuevo.html'
    model = Autor
    fields = "__all__"
    login_url = 'login'

class AutorPageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'autor_editar.html'
    model = Autor
    fields = "__all__"
    login_url = 'login'

class AutorPageDelete(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = '/autores/'
    template_name = 'autor_delete.html'
    login_url = 'login'
#-----------------------------------------------------------------------------------------------
#Biblioteca
class BibliotecaPageView(LoginRequiredMixin, ListView):
    template_name = 'biblioteca.html'
    model = Biblioteca
    context_object_name = 'Todas_Las_Bibliotecas'
    login_url = 'login'

class BibliotecaPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'biblioteca_detalle.html'
    model = Biblioteca
    context_object_name = 'Detalle_Biblioteca'
    login_url = 'login'


class BibliotecaPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'biblioteca_nuevo.html'
    model = Biblioteca
    fields = "__all__"
    login_url = 'login'

class BibliotecaPageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'biblioteca_editar.html'
    model = Biblioteca
    fields = "__all__"
    login_url = 'login'

class BibliotecaPageDelete(LoginRequiredMixin, DeleteView):
    model = Biblioteca
    success_url = '/bibliotecas/'
    template_name = 'biblioteca_delete.html'
    login_url = 'login'
#-----------------------------------------------------------------------------------------------
#Editorial
class EditorialPageView(LoginRequiredMixin, ListView):
    template_name = 'editorial.html'
    model = Editorial
    context_object_name = 'Todas_Las_Editoriales'
    login_url = 'login'

class EditorialPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'editorial_detalle.html'
    model = Editorial
    context_object_name = 'Detalle_Editorial'
    login_url = 'login'


class EditorialPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'editorial_nuevo.html'
    model = Editorial
    fields = "__all__"
    login_url = 'login'

class EditorialPageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'editorial_editar.html'
    model = Editorial
    fields = "__all__"
    login_url = 'login'

class EditorialPageDelete(LoginRequiredMixin, DeleteView):
    model = Editorial
    success_url = '/editoriales/'
    template_name = 'editorial_delete.html'
    login_url = 'login'
#-----------------------------------------------------------------------------------------------
#Libro
class LibroPageView(LoginRequiredMixin, ListView):
    template_name = 'libro.html'
    model = Libro
    context_object_name = 'Todos_Los_Libros'
    login_url = 'login'

class LibroPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'libro_detalle.html'
    model = Libro
    context_object_name = 'Detalle_Libro'
    login_url = 'login'


class LibroPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'libro_nuevo.html'
    model = Libro
    fields = "__all__"
    login_url = 'login'

class LibroPageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'libro_editar.html'
    model = Libro
    fields = "__all__"
    login_url = 'login'

class LibroPageDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = '/libros/'
    template_name = 'libro_delete.html'
    login_url = 'login'

#Comentarios
class ComentariosPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'comentarios_libro_nuevo.html'
    model = Comentarios
    fields = ('comentario',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.creador = self.request.user
        form.instance.libro_id = self.kwargs['pk']
        return super().form_valid(form)

class ComentariosPageDelete(LoginRequiredMixin, DeleteView):
    model = Comentarios
    success_url = '/libros/'
    template_name = 'comentarios_libro_delete.html'
    context_object_name = 'Comentario'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseNotFound('<h1>Pagina no encontrada</h1>')