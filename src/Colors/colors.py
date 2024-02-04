BACKGROUND_COLOR = (83, 134, 228)
MAIN_COLOR = (144, 122, 214)
SECOND_COLOR = (218, 191, 255)

BACKGROUND_COLOR_DARK_THEME = (76, 75, 99)
MAIN_COLOR_DARK_THEME = (44, 42, 74)
SECOND_COLOR_DARK_THEME = (79, 81, 140)

SHADOW = (30, 30, 30)

IS_DARK_THEME_OFF = True


def get_background_color():
    if IS_DARK_THEME_OFF:
        return BACKGROUND_COLOR
    return BACKGROUND_COLOR_DARK_THEME


def get_main_color():
    if IS_DARK_THEME_OFF:
        return MAIN_COLOR
    return MAIN_COLOR_DARK_THEME


def get_second_color():
    if IS_DARK_THEME_OFF:
        return SECOND_COLOR
    return SECOND_COLOR_DARK_THEME


def toggle_theme():
    IS_DARK_THEME_OFF = not IS_DARK_THEME_OFF


def get_shadow():
    return SHADOW
