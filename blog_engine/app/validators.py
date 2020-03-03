import pathlib
import re


def check_img(field):
    file_path = 'app/static/img/' + field
    path = pathlib.Path(file_path)
    return path.is_file() is False


def is_empty(field):
    return field.strip() == ''


def check_slug(field):
    if (len(field.split()) != 1):
        return field
    match_field = re.match(r"^[a-z0-9][ a-z0-9_-]*$", field.strip().lower())
    return match_field is None


def validate_form(check_func, fields):
    for field in fields:
        check_function, field_name, error_text = field
        error = check_func(check_function, field_name, error_text)
        if error:
            return error
