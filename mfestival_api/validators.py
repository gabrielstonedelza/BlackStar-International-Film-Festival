from django.core.exceptions import ValidationError


def validate_trailer_size(value):
    fileSize = value.size

    if fileSize > 52428800:
        raise ValidationError("File size cannot be above 50MB")
    else:
        return value