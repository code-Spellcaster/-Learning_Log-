from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Registrar un nuevo usuario."""
    if request.method != 'POST':
        # Muestra un formulario de registro en blanco.
        form = UserCreationForm()
    else:
        # Procesar un formulario completado.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Logear al usuario nuevo y redireccionarlo a la home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Mostrar un formulario en blanco o invalido.
    context = {'form': form}
    return render(request, 'registration/register.html', context)