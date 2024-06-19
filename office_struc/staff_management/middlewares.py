def my_middleware(get_response):
    print('one time initialisation')
    def my_function(request):
        print('this is before view')
        response = get_response(request)
        print('this is after view')
        return response
    return my_function

'''When Custom Middleware is Required
Request and Response Processing:

You need to modify the request or response objects globally before or after the view function is executed.
Example: Adding custom headers to responses or logging request details.
Authentication and Authorization:

Implementing custom authentication schemes or enhancing existing ones.
Example: Verifying API tokens in request headers.
Session Management:

Customizing session handling beyond what is provided by Django's session middleware.
Example: Implementing custom session expiry logic.
Request Throttling and Rate Limiting:

Implementing custom rate limiting logic based on specific criteria.
Example: Limiting the number of requests from a specific IP address.
Performance Monitoring and Logging:

Adding custom logging or performance monitoring.
Example: Logging request processing time or profiling slow requests.
Custom Error Handling:

Implementing global error handling logic.
Example: Capturing and logging exceptions globally, and returning custom error pages.
Modifying Request and Response Content:

Modifying the request or response body.
Example: Compressing response content or decrypting/encrypting request/response data.'''