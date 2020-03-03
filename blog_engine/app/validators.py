import pathlib


def check_img(field):
    if field.startswith('http'):
        return True
    file_path = 'app/static/img/' + field
    path = pathlib.Path(file_path)
    return path.is_file() is False


def is_empty(field):
    return field.strip() == ''


def validate_form(check_func, fields):
    for field in fields:
        check_function, field_name, error_text = field
        error = check_func(check_function, field_name, error_text)
        if error:
            return error




