from django.shortcuts import render
from . import models
from django.http import JsonResponse
from http import HTTPStatus

# get all languages
def get_languages(request):
    if request.method == 'GET':
        languages = models.languageList.objects.all()
    
    data = [
        {
            'id': language.id,
            'languageCode': language.languageCode,
            'languages': language.languages,
            'is_active': language.is_active,
            'created_at': language.created_at,
            'updated_at': language.updated_at
        }
         
        for language in languages
    ]
    
    if not data:
        return JsonResponse({
            'status': HTTPStatus.NOT_FOUND.value,
            'code': 0,
            'message': 'No languages found..',
            'data': []
        }, status = HTTPStatus.NOT_FOUND.value)
        
    response = {
        'status': HTTPStatus.OK.value,
        'code': 1,
        'message': 'Languages retrieved successfully.',
        'data': data
    }
    
    return JsonResponse(response, status = HTTPStatus.OK.value, safe = False)