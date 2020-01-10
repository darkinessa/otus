
expected_yandex_results = [('1 000+ Бесплатные Ирисы & Цветок изображения - Pixabay',
             'https://pixabay.com/ru/images/search/%D0%B8%D1%80%D0%B8%D1%81%D1%8B/'),
            ('«Ирис» — сеть цветочных салонов', 'https://iris-flowers.ru/'),
            ('Ирисы | Natural Museum',
             'https://natural-museum.ru/flora/%D0%B8%D1%80%D0%B8%D1%81%D1%8B'),
            ('Ирисы: 130 фото цветка и идей по украшению сада...',
             'http://landshaftadvice.ru/irisy/'),
            ('Карликовые ирисы: сорта, описание, фото, посадка и уход',
             'https://www.syl.ru/article/333595/karlikovyie-irisyi-sorta-opisanie-foto-posadka-i-uhod'),
            ('Садовая классификация ирисов',
             'https://www.greeninfo.ru/grassy/iris_hybrida.html/Article/_/aID/4985'),
            ('Цветы бородатые ирисы: лучшие сорта, фото и названия...',
             'https://kvetok.ru/tsvety-dlya-sada/iris-borodaty-j'),
            ('Ирис - мифы, легенды, история происхождения',
             'https://mifflow.ru/iris.html'),
            ('Ирис',
             'http://www.plantopedia.ru/encyclopaedia/garden-plants/details/i/iris/'),
            ('Ирисы - история, значение, советы',
             'https://cyber-florist.ru/news/irisy-istoriia-znachieniie-soviety/')]

expected_extra_link_with_google_results = [[], [('Python', 'https://habr.com/ru/hub/python/'), ('python', 'https://habr.com/ru/search/?q=%5Bpython%5D&target_type=posts'), ('                    Python Testing с pytest. Builtin Fixtures, Глава 4                  ', 'https://habr.com/ru/post/448792/'), ('                    Python Testing с pytest. ГЛАВА 3 pytest Fixtures                  ', 'https://habr.com/ru/post/448786/'), ('                    Python Testing с pytest. Глава 2, Написание тестовых функций                  ', 'https://habr.com/ru/post/448788/'), ('                    Python Testing с pytest. Начало работы с pytest, Глава 1                  ', 'https://habr.com/ru/post/448782/'), ('                    Python Testing with pytest. Просто, Быстро, Эффективно и Масштабируемо. Предисловие и Ведение                  ', 'https://habr.com/ru/post/426699/'), ('Преподаватель PythonМосковская школа программистовМосквадо 100\xa0000', 'https://career.habr.com/vacancies/1000055443'), ('Программист PythonFirstVDSИркутскот 50\xa0000до 90\xa0000', 'https://career.habr.com/vacancies/1000055649'), ('Программист PythonСтроительный ДворМоскваот 150\xa0000до 200\xa0000', 'https://career.habr.com/vacancies/1000054566'), ('Team Lead Python DeveloperYLabТольяттиМожно удаленноот 180\xa0000', 'https://career.habr.com/vacancies/1000055915'), ('Python-разработчикОнлайн-кинотеатр iviМоскваот 140\xa0000до 190\xa0000', 'https://career.habr.com/vacancies/11035166'), ('www.slideshare.net/imankulov/pytest-testing', 'http://www.slideshare.net/imankulov/pytest-testing'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')], [('книги по Python', 'https://proglib.io/p/python-best-books/'), ('Инструменты для анализа кода Python. Часть 1', 'https://proglib.io/p/python-code-analysis/'), ('Инструменты для анализа кода Python. Часть 2', 'https://proglib.io/p/python-code-analysis-tools/'), ('13 лучших книг по Python для начинающих и продолжающих', 'https://proglib.io/p/python-best-books/'), ('ТОП-10 книг по Python: эффективно, емко, доходчиво', 'https://proglib.io/p/python-books/'), ('Realpython', 'https://realpython.com/python-testing/')], [('ffmpeg-python - FFmpeg binding с поддержкой фильтрации', 'http://github.com/kkroening/ffmpeg-python'), ('Функции-таймеры в Python', 'https://realpython.com/python-timer/')], [('python', 'https://automated-testing.info/tags/python'), ('http://habrahabr.ru/company/yandex/blog/242795/', 'http://habrahabr.ru/company/yandex/blog/242795/'), (' Python', 'http://lessons2.ru/python-for-testers?utm_source=atinfo&utm_medium=top_menu&utm_term=link&utm_campaign=reference'), (' Python', 'http://lessons2.ru/python-for-testers?utm_source=atinfo&utm_medium=top_menu&utm_term=link&utm_campaign=reference')], [], [('Книга “Линейная алгебра на Python”', 'https://devpractice.ru/book-linalg-python/'), ('Книга “Python. Уроки”', 'https://devpractice.ru/book-python-lessons/'), ('Книга “Python. unittest”', 'https://devpractice.ru/book-python-unittest/'), ('Python', 'https://devpractice.ru/python/'), ('Python. Уроки', 'https://devpractice.ru/python-lessons/'), ('Python [unittest]. Уроки', 'https://devpractice.ru/python-unittest-lessons/'), ('Python-разработчику', 'https://devpractice.ru/category/python/py-dev/'), ('Python', 'https://devpractice.ru/category/python/'), ('Тестирование в Python', 'https://devpractice.ru/category/python/testing-in-python/'), ('Python', 'https://devpractice.ru/tag/python/'), ('Тестирование в Python', 'https://devpractice.ru/tag/%d1%82%d0%b5%d1%81%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5-%d0%b2-python/'), ('← Python. Урок 15. Итераторы и генераторы', 'https://devpractice.ru/python-lesson-15-iterators-and-generators/'), ('Тестирование в Python [unittest]. Часть 2. TestCase →', 'https://devpractice.ru/unit-testing-in-python-part-2/'), ('Python', 'https://devpractice.ru/category/python/'), ('Python-разработчику', 'https://devpractice.ru/category/python/py-dev/'), ('Тестирование в Python', 'https://devpractice.ru/category/python/testing-in-python/'), ('Уроки по Python', 'https://devpractice.ru/category/python/python-lessons/'), ('Линейная алгебра на Python', 'https://devpractice.ru/category/machine-learning-and-data-analysis/linalg-on-py/'), ('Python. Урок 21. Работа с контекстным менеджером', 'https://devpractice.ru/python-lesson-21-context-manager/'), ('Python', 'https://devpractice.ru/category/python/')], [('http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137', 'http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137'), ('#Python', 'https://shepetko.com/ru/tag/python'), ('Декораторы в Python, часть 2', 'https://shepetko.com/ru/blog/python-decorators-2'), ('Декораторы в Python, часть 1', 'https://shepetko.com/ru/blog/python-decorators-1'), ('Абстрактные базовые классы в Python', 'https://shepetko.com/ru/blog/abstraktnye-bazovye-klassy-v-python'), ('Асинхронное программирование в Python, часть вторая', 'https://shepetko.com/ru/blog/asinkhronnoe-programmirovanie-v-python-2'), ('Асинхронное программирование в Python, часть первая', 'https://shepetko.com/ru/blog/asinkhronnoe-programmirovanie-v-python-1'), ('#Python', 'https://shepetko.com/ru/tag/python')]]

mock_expected_extra_links_with_yandex_html = [[], [], [], [('Хвойные деревья — лучшие хвойные деревья и особенности их применения в ландшафтном дизайне (140 фото)', 'http://landshaftadvice.ru/xvojnye-derevya/'), ('Хавортия уход и посадка в домашних условиях: посадка, размножение и особенности выращивания (110 фото и видео)', 'http://landshaftadvice.ru/xavortiya-uxod/'), ('Хлебное дерево: 105 фото как выглядит, описание, выращивание и особенности употребления в пищу', 'http://landshaftadvice.ru/xlebnoe-derevo/'), ('Инженерные системы', 'http://landshaftadvice.ru/inzhenernye-sistemy/')], [], [], [('Комнатные растения', 'https://kvetok.ru/komnatnye-rasteniya'), ('Лиственные деревья', 'https://kvetok.ru/listvennye-derevya'), ('Лиственные кустарники', 'https://kvetok.ru/listvennye-kustarniki'), ('Эхинодорусы', 'https://kvetok.ru/rasteniya-dlya-akvariuma-i-vodoemov/e-hinodorusy'), ('Иксиолирион горный', 'https://kvetok.ru/rastenie/iksiolirion-gornyi'), ('Ирис безлистный', 'https://kvetok.ru/rastenie/iris-bezlistnyi'), ('Ирис кожистый', 'https://kvetok.ru/rastenie/iris-kozhistyi'), ('Ирис черепитчатый', 'https://kvetok.ru/rastenie/iris-cherepitchatyi'), ('Дидискус: виды и сорта, условия выращивания', 'https://kvetok.ru/travy/didiskus-vidy-i-sorta-uslovija-vyrashhivanija'), ('Гомфрена: виды и сорта, условия выращивания', 'https://kvetok.ru/travy/gomfrena-vidy-i-sorta-uslovija-vyrashhivanija'), ('Эндимион: виды и сорта, советы по разведению', 'https://kvetok.ru/travy/jendimion-vidy-i-sorta-sovety-po-razvedeniju'), ('Комнатные растения(505)', 'https://kvetok.ru/komnatnye-rasteniya'), ('Лиственные деревья(303)', 'https://kvetok.ru/listvennye-derevya'), ('Лиственные кустарники(280)', 'https://kvetok.ru/listvennye-kustarniki'), ('Эхинодорусы(16)', 'https://kvetok.ru/rasteniya-dlya-akvariuma-i-vodoemov/e-hinodorusy'), ('Импатиенс ампельный: лучшие сорта, как вырастить', 'https://kvetok.ru/komnatnye-rasteniya/impatiens-ampelnyj-luchshie-sorta-kak-vyrastit'), ('Пизония: особенности выращивания в квартире', 'https://kvetok.ru/komnatnye-rasteniya/pizonija-osobennosti-vyrashhivanija-v-kvartire'), ('Погонатерум: популярные виды, уход в домашних условиях', 'https://kvetok.ru/komnatnye-rasteniya/pogonaterum-populjarnye-vidy-uhod-v-domashnih-uslovijah'), ('Орбея: виды, советы по выращиванию', 'https://kvetok.ru/komnatnye-rasteniya/orbeja-vidy-sovety-po-vyrashhivaniju'), ('Пеллея: виды папоротника, особенности выращивания', 'https://kvetok.ru/komnatnye-rasteniya/pelleja-vidy-paporotnika-osobennosti-vyrashhivanija'), ('Аяния: виды, как разводить в домашних условиях', 'https://kvetok.ru/komnatnye-rasteniya/ajanija-vidy-kak-razvodit-v-domashnih-uslovijah'), ('Сидерасис: советы по выращиванию', 'https://kvetok.ru/komnatnye-rasteniya/siderasis-sovety-po-vyrashhivaniju'), ('Колокольчик персиколистый', 'https://kvetok.ru/rastenie/kolokolchik-persikolistyi')], [], [('Фестиваль в Аптекарском огороде "Репетиция весны"', 'http://www.blogs.plantopedia.ru/post/olgapetina/Festival-v-Aptekarskom-ogorode-Repetitciya-vesny/'), ('Выставка "Цветущая Азия", Москва, 12 февраля 2015-март 2015', 'http://www.blogs.plantopedia.ru/post/olgapetina/Vystavka-TCvetushaya-Aziya-Moskva-12-fevralya-2015/')], [('Доставка фруктовых корзин', 'https://www.cyber-florist.ru/zakazat-frukty.html'), ('благородные ирисы', 'https://cyber-florist.ru/flowers/irises'), ('ирисы', 'https://cyber-florist.ru/flowers/irises'), ('сиреневые ирисы роскошно смотрятся в тандеме с красными тюльпанами', 'https://cyber-florist.ru/order/violetta'), ('композиции, собранные из роз, лилий, ирисов', 'https://cyber-florist.ru/order/my-special-lady'), ('скомпоновать ирисы с герберами', 'https://cyber-florist.ru/order/celebration'), ('Строгие каллы сделают композицию ирисов богаче, эффектней', 'https://cyber-florist.ru/order/paradise'), ('Радуйте своих близких королевскими цветами ирисами - роскошными и символичными.', 'https://cyber-florist.ru/flowers/irises'), ('Яркая красочная корзина с цветами "Музыка красок"', 'https://cyber-florist.ru/news/music-of-colors/'), ('Яркий и нежный букет с брассикой "Утренняя звезда"', 'https://cyber-florist.ru/news/iarkii-i-niezhnyi-bukiet-s-brasikoi/')]]

expected_combined_results_with_yandex_results = [(('1 000+ Бесплатные Ирисы & Цветок изображения - Pixabay', 'https://pixabay.com/ru/images/search/%D0%B8%D1%80%D0%B8%D1%81%D1%8B/'), []), (('«Ирис» — сеть цветочных салонов', 'https://iris-flowers.ru/'), []), (('Ирисы | Natural Museum', 'https://natural-museum.ru/flora/%D0%B8%D1%80%D0%B8%D1%81%D1%8B'), []), (('Ирисы: 130 фото цветка и идей по украшению сада...', 'http://landshaftadvice.ru/irisy/'), [('Хвойные деревья — лучшие хвойные деревья и особенности их применения в ландшафтном дизайне (140 фото)', 'http://landshaftadvice.ru/xvojnye-derevya/'), ('Хавортия уход и посадка в домашних условиях: посадка, размножение и особенности выращивания (110 фото и видео)', 'http://landshaftadvice.ru/xavortiya-uxod/'), ('Хлебное дерево: 105 фото как выглядит, описание, выращивание и особенности употребления в пищу', 'http://landshaftadvice.ru/xlebnoe-derevo/'), ('Инженерные системы', 'http://landshaftadvice.ru/inzhenernye-sistemy/')]), (('Карликовые ирисы: сорта, описание, фото, посадка и уход', 'https://www.syl.ru/article/333595/karlikovyie-irisyi-sorta-opisanie-foto-posadka-i-uhod'), []), (('Садовая классификация ирисов', 'https://www.greeninfo.ru/grassy/iris_hybrida.html/Article/_/aID/4985'), []), (('Цветы бородатые ирисы: лучшие сорта, фото и названия...', 'https://kvetok.ru/tsvety-dlya-sada/iris-borodaty-j'), [('Комнатные растения', 'https://kvetok.ru/komnatnye-rasteniya'), ('Лиственные деревья', 'https://kvetok.ru/listvennye-derevya'), ('Лиственные кустарники', 'https://kvetok.ru/listvennye-kustarniki'), ('Эхинодорусы', 'https://kvetok.ru/rasteniya-dlya-akvariuma-i-vodoemov/e-hinodorusy'), ('Иксиолирион горный', 'https://kvetok.ru/rastenie/iksiolirion-gornyi'), ('Ирис безлистный', 'https://kvetok.ru/rastenie/iris-bezlistnyi'), ('Ирис кожистый', 'https://kvetok.ru/rastenie/iris-kozhistyi'), ('Ирис черепитчатый', 'https://kvetok.ru/rastenie/iris-cherepitchatyi'), ('Дидискус: виды и сорта, условия выращивания', 'https://kvetok.ru/travy/didiskus-vidy-i-sorta-uslovija-vyrashhivanija'), ('Гомфрена: виды и сорта, условия выращивания', 'https://kvetok.ru/travy/gomfrena-vidy-i-sorta-uslovija-vyrashhivanija'), ('Эндимион: виды и сорта, советы по разведению', 'https://kvetok.ru/travy/jendimion-vidy-i-sorta-sovety-po-razvedeniju'), ('Комнатные растения(505)', 'https://kvetok.ru/komnatnye-rasteniya'), ('Лиственные деревья(303)', 'https://kvetok.ru/listvennye-derevya'), ('Лиственные кустарники(280)', 'https://kvetok.ru/listvennye-kustarniki'), ('Эхинодорусы(16)', 'https://kvetok.ru/rasteniya-dlya-akvariuma-i-vodoemov/e-hinodorusy'), ('Импатиенс ампельный: лучшие сорта, как вырастить', 'https://kvetok.ru/komnatnye-rasteniya/impatiens-ampelnyj-luchshie-sorta-kak-vyrastit'), ('Пизония: особенности выращивания в квартире', 'https://kvetok.ru/komnatnye-rasteniya/pizonija-osobennosti-vyrashhivanija-v-kvartire'), ('Погонатерум: популярные виды, уход в домашних условиях', 'https://kvetok.ru/komnatnye-rasteniya/pogonaterum-populjarnye-vidy-uhod-v-domashnih-uslovijah'), ('Орбея: виды, советы по выращиванию', 'https://kvetok.ru/komnatnye-rasteniya/orbeja-vidy-sovety-po-vyrashhivaniju'), ('Пеллея: виды папоротника, особенности выращивания', 'https://kvetok.ru/komnatnye-rasteniya/pelleja-vidy-paporotnika-osobennosti-vyrashhivanija'), ('Аяния: виды, как разводить в домашних условиях', 'https://kvetok.ru/komnatnye-rasteniya/ajanija-vidy-kak-razvodit-v-domashnih-uslovijah'), ('Сидерасис: советы по выращиванию', 'https://kvetok.ru/komnatnye-rasteniya/siderasis-sovety-po-vyrashhivaniju'), ('Колокольчик персиколистый', 'https://kvetok.ru/rastenie/kolokolchik-persikolistyi')]), (('Ирис - мифы, легенды, история происхождения', 'https://mifflow.ru/iris.html'), []), (('Ирис', 'http://www.plantopedia.ru/encyclopaedia/garden-plants/details/i/iris/'), [('Фестиваль в Аптекарском огороде "Репетиция весны"', 'http://www.blogs.plantopedia.ru/post/olgapetina/Festival-v-Aptekarskom-ogorode-Repetitciya-vesny/'), ('Выставка "Цветущая Азия", Москва, 12 февраля 2015-март 2015', 'http://www.blogs.plantopedia.ru/post/olgapetina/Vystavka-TCvetushaya-Aziya-Moskva-12-fevralya-2015/')]), (('Ирисы - история, значение, советы', 'https://cyber-florist.ru/news/irisy-istoriia-znachieniie-soviety/'), [('Доставка фруктовых корзин', 'https://www.cyber-florist.ru/zakazat-frukty.html'), ('благородные ирисы', 'https://cyber-florist.ru/flowers/irises'), ('ирисы', 'https://cyber-florist.ru/flowers/irises'), ('сиреневые ирисы роскошно смотрятся в тандеме с красными тюльпанами', 'https://cyber-florist.ru/order/violetta'), ('композиции, собранные из роз, лилий, ирисов', 'https://cyber-florist.ru/order/my-special-lady'), ('скомпоновать ирисы с герберами', 'https://cyber-florist.ru/order/celebration'), ('Строгие каллы сделают композицию ирисов богаче, эффектней', 'https://cyber-florist.ru/order/paradise'), ('Радуйте своих близких королевскими цветами ирисами - роскошными и символичными.', 'https://cyber-florist.ru/flowers/irises'), ('Яркая красочная корзина с цветами "Музыка красок"', 'https://cyber-florist.ru/news/music-of-colors/'), ('Яркий и нежный букет с брассикой "Утренняя звезда"', 'https://cyber-florist.ru/news/iarkii-i-niezhnyi-bukiet-s-brasikoi/')])]

google_extra_soup = [[('Разработка идеального pypi пакета с поддержкой разных версий python', 'https://habr.com/ru/post/483512/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Создатель Python Гвидо ван Россум ушел из Dropbox на пенсию', 'https://habr.com/ru/news/t/473926/'), ('Что такое *args и **kwargs в Python?', 'https://habr.com/ru/company/ruvds/blog/482464/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Отслеживаем прогресс выполнения в Python', 'https://habr.com/ru/post/483400/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Начинаем работу с Google Sheets на Python. От регистрации до чтения данных', 'https://habr.com/ru/post/483302/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Работаем с API Google Drive с помощью Python', 'http://datalytics.ru/all/rabotaem-s-api-google-drive-s-pomoschyu-python/'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('                    Python                                      Простой                  Установка PyQt5?0 ответов', 'https://qna.habr.com/q/699463'), ('                    Python                                      Простой                  Что выбрать новичку: Python, C++ или все же GOlang?5 ответов', 'https://qna.habr.com/q/699456'), ('                    Python                                      Простой                  Как установить pyaudio?2 ответа', 'https://qna.habr.com/q/699439'), ('                    Python                                      Простой                  Можно ли pug использовать в python?1 ответ', 'https://qna.habr.com/q/699418'), ('                    Python                                      Простой                  Как сделать кнопки (клавиатуру) в боте ВКонтакте с помощью vk_api на Python?2 ответа', 'https://qna.habr.com/q/699375'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Введение в ASGI: становление асинхронной веб-экосистемы Python', 'https://habr.com/ru/post/482936/'), ('Python', 'https://habr.com/ru/hub/python/'), ('"Introduction to ASGI: Emergence of an Async Python Web Ecosystem"', 'https://florimond.dev/blog/articles/2019/08/introduction-to-asgi-async-python-web/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Кодировки, шифр сдвига, брут хешей и создание картинки с помощью PIL python.', 'https://habr.com/ru/post/472628/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')], [('Что такое *args и **kwargs в Python?', 'https://habr.com/ru/company/ruvds/blog/482464/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Разработка идеального pypi пакета с поддержкой разных версий python', 'https://habr.com/ru/post/483512/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Создатель Python Гвидо ван Россум ушел из Dropbox на пенсию', 'https://habr.com/ru/news/t/473926/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Выбор python-фреймворка', 'https://habr.com/ru/post/9372/'), ('Python за 10 минут', 'https://habr.com/ru/post/9621/'), ('Поддержка Ruby и Python на клиенте в Firefox 4', 'https://habr.com/ru/post/12647/'), ('Python 3000 alpha1', 'https://habr.com/ru/post/13722/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Python', 'https://habr.com/ru/hub/python/'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')], [('Python', 'https://habr.com/ru/hub/python/'), ('ch4/authors/conftest.py', 'https://media.pragprog.com/titles/bopytest/code/ch4/authors/conftest.py'), ('ch4/pytestconfig/conftest.py', 'https://media.pragprog.com/titles/bopytest/code/ch4/pytestconfig/conftest.py'), ('ch4/pytestconfig/test_config.py', 'https://media.pragprog.com/titles/bopytest/code/ch4/pytestconfig/test_config.py'), ('ch4/pytestconfig/test_config.py', 'https://media.pragprog.com/titles/bopytest/code/ch4/pytestconfig/test_config.py'), ('ch4/monkey/test_cheese.py', 'https://media.pragprog.com/titles/bopytest/code/ch4/monkey/test_cheese.py'), ('ch4/monkey/test_cheese.py', 'https://media.pragprog.com/titles/bopytest/code/ch4/monkey/test_cheese.py'), ('ch4/monkey/test_cheese.py', 'https://media.pragprog.com/titles/bopytest/code/ch4/monkey/test_cheese.py'), ('ch4/monkey/test_cheese.py', 'https://media.pragprog.com/titles/bopytest/code/ch4/monkey/test_cheese.py'), ('ch4/dt/3/conftest.py', 'https://media.pragprog.com/titles/bopytest/code/ch4/dt/3/conftest.py'), ('                    Python Testing с pytest. ГЛАВА 3 pytest Fixtures                  ', 'https://habr.com/ru/post/448786/'), ('                    Python Testing с pytest. Глава 2, Написание тестовых функций                  ', 'https://habr.com/ru/post/448788/'), ('                    Python Testing с pytest. Начало работы с pytest, Глава 1                  ', 'https://habr.com/ru/post/448782/'), ('                    Python Testing with pytest. Просто, Быстро, Эффективно и Масштабируемо. Предисловие и Ведение                  ', 'https://habr.com/ru/post/426699/'), ('Преподаватель PythonМосковская школа программистовМосквадо 100\xa0000', 'https://career.habr.com/vacancies/1000055443'), ('Программист PythonСтроительный ДворМоскваот 150\xa0000до 200\xa0000', 'https://career.habr.com/vacancies/1000054566'), ('Программист PythonFirstVDSИркутскот 50\xa0000до 90\xa0000', 'https://career.habr.com/vacancies/1000055649'), ('Программист PythonСтроительный ДворТюменьот 70\xa0000до 130\xa0000', 'https://career.habr.com/vacancies/1000053958'), ('Team Lead Python DeveloperYLabТольяттиМожно удаленноот 180\xa0000', 'https://career.habr.com/vacancies/1000055915'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')], [('Python', 'https://habr.com/ru/hub/python/'), ('ch3/b/tasks_proj/tests/conftest.py', 'https://media.pragprog.com/titles/bopytest/code/ch3/b/tasks_proj/tests/conftest.py'), ('ch3/c/tasks_proj/tests/conftest.py', 'https://media.pragprog.com/titles/bopytest/code/ch3/c/tasks_proj/tests/conftest.py'), ('                    Python Testing with pytest. Просто, Быстро, Эффективно и Масштабируемо. Предисловие и Ведение                  ', 'https://habr.com/ru/post/426699/'), ('Преподаватель PythonМосковская школа программистовМосквадо 100\xa0000', 'https://career.habr.com/vacancies/1000055443'), ('Программист PythonСтроительный ДворМоскваот 150\xa0000до 200\xa0000', 'https://career.habr.com/vacancies/1000054566'), ('Программист PythonFirstVDSИркутскот 50\xa0000до 90\xa0000', 'https://career.habr.com/vacancies/1000055649'), ('Программист PythonСтроительный ДворТюменьот 70\xa0000до 130\xa0000', 'https://career.habr.com/vacancies/1000053958'), ('Team Lead Python DeveloperYLabТольяттиМожно удаленноот 180\xa0000', 'https://career.habr.com/vacancies/1000055915'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')], [('Python', 'https://habr.com/ru/hub/python/'), ('                    Python Testing with pytest. Просто, Быстро, Эффективно и Масштабируемо. Предисловие и Ведение                  ', 'https://habr.com/ru/post/426699/'), ('Преподаватель PythonМосковская школа программистовМосквадо 100\xa0000', 'https://career.habr.com/vacancies/1000055443'), ('Программист PythonСтроительный ДворМоскваот 150\xa0000до 200\xa0000', 'https://career.habr.com/vacancies/1000054566'), ('Программист PythonFirstVDSИркутскот 50\xa0000до 90\xa0000', 'https://career.habr.com/vacancies/1000055649'), ('Программист PythonСтроительный ДворТюменьот 70\xa0000до 130\xa0000', 'https://career.habr.com/vacancies/1000053958'), ('Team Lead Python DeveloperYLabТольяттиМожно удаленноот 180\xa0000', 'https://career.habr.com/vacancies/1000055915'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')], [('Python', 'https://habr.com/ru/hub/python/'), ('https://pypi.python.org/pypi/pytest', 'https://pypi.python.org/pypi/pytest'), ('                    Python Testing with pytest. Просто, Быстро, Эффективно и Масштабируемо. Предисловие и Ведение                  ', 'https://habr.com/ru/post/426699/'), ('Преподаватель PythonМосковская школа программистовМосквадо 100\xa0000', 'https://career.habr.com/vacancies/1000055443'), ('Программист PythonСтроительный ДворМоскваот 150\xa0000до 200\xa0000', 'https://career.habr.com/vacancies/1000054566'), ('Программист PythonFirstVDSИркутскот 50\xa0000до 90\xa0000', 'https://career.habr.com/vacancies/1000055649'), ('Программист PythonСтроительный ДворТюменьот 70\xa0000до 130\xa0000', 'https://career.habr.com/vacancies/1000053958'), ('Team Lead Python DeveloperYLabТольяттиМожно удаленноот 180\xa0000', 'https://career.habr.com/vacancies/1000055915'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')], [('Python', 'https://habr.com/ru/hub/python/'), ('python', 'https://habr.com/ru/search/?q=%5Bpython%5D&target_type=posts'), ('                    Реализация паттерна Page Object на Python + pytest                  ', 'https://habr.com/ru/post/472156/'), ('                    Python и FPGA. Тестирование                  ', 'https://habr.com/ru/post/442010/'), ('Python приложение для отображения данных6 откликов50 просмотров5000за проект', 'http://freelance.habr.com/tasks/282786'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')], [], [], [], [], [], [], [('Python', 'https://habr.com/ru/hub/python/'), ('Python 3.8', 'https://habr.com/ru/search/?q=%5BPython%203.8%5D&target_type=posts'), ('                    Онлайн-репетитор по Python                  ', 'https://habr.com/ru/post/138513/'), ('                    Осваиваем Python. Унция 1. Типы данных.                  ', 'https://habr.com/ru/post/49671/'), ('                    Подробности о Python 2.6 и Python 3.0                  ', 'https://habr.com/ru/post/16555/'), ('Python приложение для отображения данных6 откликов50 просмотров5000за проект', 'http://freelance.habr.com/tasks/282786'), ('www.python.org/dev/peps/pep-0570', 'https://www.python.org/dev/peps/pep-0570/'), ('stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6', 'https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6'), ('multiprocessing.shared_memory', 'https://docs.python.org/3/library/multiprocessing.shared_memory.html'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')]]

