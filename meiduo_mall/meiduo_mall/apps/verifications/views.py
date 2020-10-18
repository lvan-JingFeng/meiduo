from django.http import HttpResponse
from django.shortcuts import render
from django_redis import get_redis_connection

from meiduo_mall.libs.captcha.captcha import captcha
from . import constants
# Create your views here.
"""
在用户注册中，需要实现一下接口：

图片验证码
短信验证码
用户名判断是否存在
手机号判断是否存在
注册保存用户数据
"""
from rest_framework.views import APIView


class ImageCodeView(APIView):
    """
    图片验证码
    """
    def get(self, request, image_code_id):
        """获取图片验证码"""

        # 生成验证码图片

        text, image = captcha.generate_captcha()
        redis_conn = get_redis_connection("verify_codes")
        redis_conn.setex("img_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)

        return HttpResponse(image, content_type="images/jpg")
