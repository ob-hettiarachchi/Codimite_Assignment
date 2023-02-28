from rest_framework.views import APIView
from rest_framework.response import Response

class GCDtest(APIView):
    def get(self,request):

        A = 270
        B = 192

        while (B != 0):
            mod = A % B

            A = B
            B = mod

        return Response(A)
    
class GCD(APIView):
    def get(self,request, a,b):

        A = a
        B = b

        while (B != 0):
            mod = A % B

            A = B
            B = mod

        return Response(A)

class fibonacci(APIView):
    def get(self, request, n):

        index = n
        index = index - 2

        x = 0
        y = 1

        while (index != 0):

            value = x + y
            x = y
            y = value

            index = index - 1

        return Response(value)

class test(APIView):
    def get(self, request):
        return Response ("test")

