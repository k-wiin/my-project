
import json
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        chrome=False
        browser=request.META['HTTP_USER_AGENT']
        if browser in ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36']:
            chrome=True
            my_request  = request.GET.copy()
            my_request['chrome']=chrome
            request.GET = my_request
        print("-----------request-------")


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.


        response['succcccccess']="its correct"
        # print("----------------response-in middleware-------",json.loads(response.text))

        return response