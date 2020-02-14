# from django.shortcuts import render
# from django.http import HttpResponseRedirect,HttpResponse
# from django.utils.deprecation import MiddlewareMixin
# class Custom500Middleware(MiddlewareMixin):
#     def process_exception(self, request, exception):
#         if isinstance(exception, Http404):
#             # implement your custom logic. You can send
#             # http response with any template or message
#             # here. unicode(exception) will give the custom
#             # error message that was passed.
#             msg = unicode(exception)
#             return render(request,'home/custom500.html')
#         else:
#             return HttpResponse("YO")

# from .models import launch,popular,description,genres,logo
from django.shortcuts import render
# from django.http import HttpResponseRedirect
# class Custom500Middleware:
# 	def _init_(self,get_response):
# 		self.get_response=get_response
# 	def _call_(self, request):
# 		a=self.get_response(request)
# 		if (a.status_code!=404):
# 			return a
# 		else:


# class Custom500Middleware(object):
#     def process_exception(self, request, exception):
#         print (exception.__class__.__name__)
#         print (exception.message)
# #         return None
from django.utils.deprecation import MiddlewareMixin
class Custom500Middleware(MiddlewareMixin):

    def process_exception(self,request,exception):
        # if isinstance(exception, http.Http404):
        return render(request,'home/custom500.html')
        # pass


# from .models import launch,popular,description,genres,logo
from django.shortcuts import render
from django.http import HttpResponseRedirect
# class Custom500Middleware():
# 	def _init_(self,get_response):
# 		self.get_response=get_response
# 	def _call_(self,request):
# 		a=self.get_response(request)
# 		if (a.status_code!=404):
# 			return a
# 		else:
# 			return render(request,'games/myown404.html',{})