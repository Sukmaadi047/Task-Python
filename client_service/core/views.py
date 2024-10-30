from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Required if CSRF is not configured properly
def secret_view(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Success! This is a secret.'})
    return JsonResponse({'error': 'Method not allowed'}, status=405)
