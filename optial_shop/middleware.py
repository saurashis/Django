from django.contrib.auth import logout

class DemoMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print( ((request.body.decode('utf-8'))))
        return self.get_response(request)
        
    

