from string import ascii_letters, digits

ALL_SYMBOLS = ascii_letters + digits
REGEX_VALIDATE = r'^[a-zA-Z0-9]+'
MAX_LENGHT_URL = 6
MAX_LENGHT_SHORT_LINK = 16
SHORT_LINK_IN_DB = "Предложенный вариант короткой ссылки уже существует."
LINK_IN_DB = "Предложенный вариант короткой ссылки уже существует."
NO_VALID_SHORT_LINK = "Указано недопустимое имя для короткой ссылки"
REQUIRED_URL = "\"url\" является обязательным полем!"
NO_BODY_IN_REQUEST = "Отсутствует тело запроса"
NO_FOUND = "Указанный id не найден"
