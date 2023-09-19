
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def hello(request, context):
    print(f'hello====={context}')
    return HttpResponse(f'hello====={context}')

@csrf_exempt
def test_task(request):

    # 同步数据
    # bs.sync_apply_to_cms('', '')

    return HttpResponse('ok')


