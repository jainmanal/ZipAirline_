from rest_framework import serializers
import math
from pydoc import plain
class UserSerializer(serializers.Serializer):
    plain_id = serializers.IntegerField()
    pass_no = serializers.IntegerField()
    
        
    
        