from django.utils.deprecation import MiddlewareMixin
import datetime

class RequestLogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print(f"📌 Requested URL: {request.path} at {datetime.datetime.now()}")

    def process_response(self, request, response):
        print("✅ Response sent successfully!")
        return response
