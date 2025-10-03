from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views.generic import TemplateView

class LandingView(TemplateView):
    template_name = "landing.html"

    def post(self, request, *args, **kwargs):
        # Aquí podrías enviar email, guardar en BD, etc.
        # nombre = request.POST.get("nombre")
        # email = request.POST.get("email")
        # mensaje = request.POST.get("mensaje")
        return redirect("/?ok=1")

