from django.core.exceptions import ValidationError


def validate_trailer_size(value):
    fileSize = value.size

    if fileSize > 15728640:
        raise ValidationError("File size cannot be above 15MB")
    else:
        return value