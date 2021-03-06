import json
import logging
from random import randint

request_logger = logging.getLogger('django.request')
error_logger = logging.getLogger('django.request')


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = randint(0, 100000000000)

        log_data = {
            "request_id": request_id,
            "remote_address": request.META["REMOTE_ADDR"],
            "request_method": request.method,
            "request_path": request.get_full_path(),
        }
        response = self.get_response(request)
        if "/api" in request.get_full_path():
            req_body = json.loads(request.body) if request.body else {}
            log_data["request_body"] = req_body
            if not str(response.status_code).startswith("4") or str(response.status_code).startswith("5"):
                response_obj = {
                    "request_id": request_id,
                    "request_body": req_body,
                    "status_code": response.status_code,
                    "response_data": response.data,
                }
                request_logger.info(msg=log_data)
                request_logger.info(msg=response_obj)
        return response

    def process_exception(self, request, exception):
        try:
            raise exception
        except Exception as e:
            request_logger.exception("Unhandled Exception: " + str(e))
        return exception


class ErrorLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if "/api" in request.get_full_path():
            if str(response.status_code).startswith("4") or str(response.status_code).startswith("5"):
                error_response_obj = {
                    "request_path": request.get_full_path(),
                    "status_code": response.status_code,
                    "response_data": response.data,
                }
                error_logger.info(msg=error_response_obj)
        return response
