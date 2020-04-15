from django.http import HttpResponse

from wduser.models import WduserAuthuser, WduserOrg
import os

def get_rand_user(request):
    try:
        user = WduserAuthuser.objects.filter(nickname='d52645894d8c5d83').order_by('?')[0]
        account_name = user.account_name
        # if account_name:
        #     user.nickname+="_"
        #     user.save()
        return HttpResponse(account_name)
    except:
        return HttpResponse(None)


def set_rand_user(request):
    username = request.GET.get('username', default='')
    org1 = request.GET.get('org1', default='')
    org2 = request.GET.get('org2', default='')
    org3 = request.GET.get('org3', default='')
    org4 = request.GET.get('org4', default='')
    org5 = request.GET.get('org5', default='')
    try:
        user = WduserOrg.objects.get(account_name=username)
        user.org_level1 = org1
        user.org_level2 = org2
        user.org_level3 = org3
        user.org_level4 = org4
        user.org_level5 = org5
        user.save()
        return HttpResponse('update')
    except:
        user = WduserOrg(account_name=username, org_level1=org1, org_level2=org2, org_level3=org3, org_level4=org4,
                         org_level5=org5)
        user.save()
        return HttpResponse('insert')


def favicon(request):
    imgDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    imgDir = os.path.join(imgDir, 'public/images')
    imgFilePath = os.path.join(imgDir, 'favicon.ico')
    # return HttpResponse('favicon...' + imgFilePath)
    image_data = open(imgFilePath, "rb").read()
    return HttpResponse(image_data, content_type="image/png")