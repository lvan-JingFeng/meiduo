from django_redis import get_redis_connection
from rest_framework import serializers


class CheckImageCodeSerializer(serializers):
    """图片验证码序列化器"""
    image_code = serializers.UUIDField()
    text = serializers.CharField(max_length=4, min_length=4)

    def validate(self, attrs):
        """校验图片验证码是否正确"""
        image_code_id = attrs['image_code_id']
        text = attrs['text']
        # 查询redis数据库，获取真实的验证码
        # 获取redis的连接对象
        redis_conn = get_redis_connection('verify_codes')
        real_image_code_text = redis_conn.get('img_%s' % image_code_id)
        if real_image_code_text is None:
            # 过期或者不存在
            raise serializers.ValidationError('图片验证码无效')