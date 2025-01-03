from django.http import HttpResponse
from django.template import loader


def show_korea_map(request):
    def get():
        templates = loader.get_template('map/main.html')
        return HttpResponse(templates.render())

    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)