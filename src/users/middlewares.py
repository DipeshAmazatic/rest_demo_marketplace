import logging
import json
from django.utils.deprecation import MiddlewareMixin

class LogUserDetailsMiddleware(MiddlewareMixin):
    log = logging.getLogger('requestlogger')
    request_data = None
    
    def process_response(self, request, response):
        
        try:
            user = request._cached_user if hasattr(request, '_cached_user') else request.user
            if  hasattr(request, 'auth') and request.auth:
                if hasattr(request.auth, 'customer'):
                    user = request.auth.user or user
            headers = request.headers
            headers = {key: value for key,value in headers.items() if key not in {'Authorization'}}
            response_data = None
            try:
                assert headers.get('Content-Type').split(';')[0] == 'application/json'
                response_data = json.loads(response.content)
                print("asfsdjfdsf")
            except AssertionError as e:
                print(e)
                self.log.error(e)
                raise Exception('Content-Type is not a JSON format data...')
            log_data = {
                'HEADERS': headers,
                'METHOD': request.method,
                'USER': {
                    'id': user.pk if hasattr(user, 'pk') else None,
                    'phone_number': user.phone_no if hasattr(user, 'phone_no') else response_data.get('user').get('phone_no'),
                    'email': user.email if hasattr(user, 'email') else response_data.get('user').get('email'),
                    'model': 'User' if hasattr(user, 'is_superuser') else 'User',
                    'ip_address': self.get_ip(request)
                },
                'URL': request.build_absolute_uri(),
                'REQUEST_DATA': self.request_data,
                'RESPONSE_DATA': response_data,
                'STATUS_CODE': response.status_code
            }
        except Exception as e:
            print("before log")
            self.log.error(e)
            print("after log")
        else:
            print(log_data)
            self.log.debug(log_data)
        return response
    
    def get_ip(self, request):
        """
        get client ip address
        """
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', None)
        if ip_address:
            ip_address = ip_address.split(', ')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR', '')
        return ip_address
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        
        try:
            self.request_data = json.loads(request.body)
        except Exception as e:
            self.log.error(e)
