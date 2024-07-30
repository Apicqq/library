from http import HTTPStatus

from django.shortcuts import render


def page_not_found(request, *args, **kwargs):
    return render(request, 'error_pages/404.html', status=HTTPStatus.NOT_FOUND)


def csrf_failure(request, *args, **kwargs):
    return render(request, 'error_pages/403csrf.html',
                  status=HTTPStatus.FORBIDDEN)


def internal_error(request, *args, **kwargs):
    return render(request, 'error_pages/500.html',
                  status=HTTPStatus.INTERNAL_SERVER_ERROR)
