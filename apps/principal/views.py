from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from forms import ContactForm
from django.core.mail import EmailMultiAlternatives # Enviamos HTML
from django.template import RequestContext


# Create your views here.

class IndexView(TemplateView):
	template_name = 'index.html'




def contacto_view(request):
	info_enviado  =  False
	email=""
	titulo = ""
	texto=""
	if request.method =="POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

			# Configuracion enviando mensaje via GMAIL
			to_admin = 'adeconlaguna@gmail.com'
			html_content = "Informacion recibida de [%s] <br><br><br>***Mensaje****<br><br>%s"%(email,texto)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html') # Definimos el contenido como HTML
			msg.send() # Enviamos  en correo
	else:
		formulario = ContactForm()
	ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
	return render_to_response('contactanos.html',ctx,context_instance=RequestContext(request))