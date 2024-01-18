# 아래에 코드를 작성하시오.
# import conf.settings

from conf import settings
from utils import create_url

# print(settings.NAME)
# print(settings.MAIN_URL)

# print(create_url.create_url(settings.NAME, settings.MAIN_URL))
result = create_url.create_url(settings.NAME, settings.MAIN_URL)
print(result)