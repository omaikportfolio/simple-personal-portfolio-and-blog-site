from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'

class AboutContact(TemplateView):
    template_name = 'About_contact.html'
