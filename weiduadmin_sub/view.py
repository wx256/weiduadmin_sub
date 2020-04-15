from django.http import HttpResponse

from wduser.models import WduserAuthuser, WduserOrg
import os


#取随机账号
def get_rand_user(request):
    user = WduserAuthuser.objects.filter(nickname='d52645894d8c5d83').order_by('?')
    if user:
        account_name = user[0].account_name
        #     user.nickname+="_"
        #     user.save()
    else:
        account_name = None
    return HttpResponse(account_name)


#提交选取组织
def set_rand_user(request):
    username = request.GET.get('username', default='')
    org1 = request.GET.get('org1', default='')
    org2 = request.GET.get('org2', default='')
    org3 = request.GET.get('org3', default='')
    org4 = request.GET.get('org4', default='')
    org5 = request.GET.get('org5', default='')
    user = WduserOrg.objects.filter(account_name=username).last()
    if user:
        user.org_level1 = org1
        user.org_level2 = org2
        user.org_level3 = org3
        user.org_level4 = org4
        user.org_level5 = org5
        user.save()
        return HttpResponse('update')
    else:
        user = WduserOrg(account_name=username, org_level1=org1, org_level2=org2, org_level3=org3, org_level4=org4,
                         org_level5=org5)
        user.save()
        return HttpResponse('insert')


#图标
def favicon(request):
    imgDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    imgDir = os.path.join(imgDir, 'public/images')
    imgFilePath = os.path.join(imgDir, 'favicon.ico')
    # return HttpResponse('favicon...' + imgFilePath)
    image_data = open(imgFilePath, "rb").read()
    return HttpResponse(image_data, content_type="image/png")