import json

from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .models import Paste


@require_POST
@csrf_exempt
def create_api(request):
    req = json.loads(request.body)

    title = req.get('title', 'Untitled Paste')
    content = req.get('content', '')
    language = req.get('language', 'plaintext')

    paste = Paste(title=title, content=content, language=language)
    paste.save()

    return JsonResponse({'id': paste.id})


@csrf_exempt
def view_api(request, paste_id):
    paste = Paste.objects.get(id=paste_id)

    return JsonResponse({
        'title': paste.title,
        'content': paste.content,
        'language': paste.language,
        'createdOn': paste.created_on,
    })


def create(request):
    return render(request, 'create.html')


def view(request, paste_id):
    try:
        paste = Paste.objects.get(id=paste_id)

        return render(request, 'view.html', {
            'title': paste.title,
            'content': paste.content,
            'language': paste.language,
            'created_on': paste.created_on,
        })
    except:
        raise Http404('Paste does not exist')
