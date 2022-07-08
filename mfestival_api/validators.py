from django.core.exceptions import ValidationError


def validate_trailer_size(value):
    fileSize = value.size

    if fileSize > 31457280:
        raise ValidationError("File size cannot be above 30MB")
    else:
        return value