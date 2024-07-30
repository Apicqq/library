from django.core.exceptions import ValidationError
from django.utils.timezone import now

from core.constants import Errors


def validate_book_year(year: int) -> int:
    if year > now().year:
        raise ValidationError(Errors.INVALID_BOOK_YEAR)
    return year
