from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from web.service import code
import json


class WeChatView(View):
    def get(self, request):
        code_url = code.get_url()
        return render(request, 'wx.html', {'code_url': code_url})


class WxLoginView(View):
    def get(self, request):
        # 建立长轮询, 实时监听
        response = code.scan_code()
        # 获取到监听数据, 解析返回值
        result = code.analysis_task(response)
        return HttpResponse(json.dumps(result))

    @method_decorator(csrf_exempt)
    def post(self, request):
        response = code.send_msg(request.POST)
        print(response)
        return HttpResponse('...')


class WxPushView(View):
    def get(self, request):
        response = code.push_msg()
        return HttpResponse(json.dumps(response))


class WxIndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        response = code.send_msg(request.POST)
        print(response)
        return HttpResponse('...')