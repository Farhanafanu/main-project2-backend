# security_headers_middleware.py

class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Set Cross-Origin-Opener-Policy header
        response['Cross-Origin-Opener-Policy'] = 'same-origin'
        # Set Cross-Origin-Embedder-Policy header
        response['Cross-Origin-Embedder-Policy'] = 'require-corp'
        # Add other headers here if needed

        return response
