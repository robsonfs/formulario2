from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib import messages

# Create your views here.

def formulario(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.nome = request.POST['nome']
            post.email = request.POST['email']
            post.telefone = request.POST['telefone']
            post.save()
            messages.success(
            request, "Seus dados foram registrados. Em breve entraremos em contato.")
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'core/layout.html', {'form': form})
