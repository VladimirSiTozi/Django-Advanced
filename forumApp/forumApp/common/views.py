from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import now
from django.views import View


def view_counter(request):
    print(dict(request.session))
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0

    return HttpResponse(f'The count is: {request.session.get("counter")}')


# Create custom cookie
class SetTimeCookie(View):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        current_time = now()

        last_visit = request.COOKIES.get('last_visit')

        if last_visit:
            response.content = f'Your last visit was on {last_visit}'.encode()
        else:
            response.content = f'This is your first visit'.encode()

        response.set_cookie(
            'last_visit',
            current_time.strftime('%Y-%m-%d %H:%M:%S'),
            # expires=1,
        )

        return response
