import pathlib


def check_img(field):
    if field.startswith('http'):
        return True
    file_path = 'app/static/img/' + field
    path = pathlib.Path(file_path)
    return path.is_file() is False


