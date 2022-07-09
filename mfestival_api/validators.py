from django.core.exceptions import ValidationError


def validate_trailer_size(value):
    fileSize = value.size

    if fileSize > 157286400:
        raise ValidationError("File size cannot be above 150MB")
    else:
        return value