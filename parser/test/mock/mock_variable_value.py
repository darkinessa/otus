# -*- coding: utf-8 -*-
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

expected_google_results = [('Введение в PyTest - Alexander Demura - Medium',
             'https://medium.com/@dmrlx/%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-pytest-cc6175c7d0dc'),
            ('PyTest / Хабр - Habr', 'https://habr.com/ru/post/269759/'),
            ('Погружаемся в основы и нюансы тестирования Python-кода', 'https://proglib.io/p/python-testing/'),
             (
                'Все точки над И - разбираем фикстуры pytest - python ...',
                'https://automated-testing.info/t/vse-tochki-nad-i-razbiraem-fikstury-pytest/8051'),
            ("Блог gigimon'а ← Немного про py.test", 'https://it4it.ru/2016/02/11/pytest-1/'), (
                'Тестирование в Python [unittest]. Часть 1. Введение',
                'https://devpractice.ru/unit-testing-in-python-part-1/'),
            ('Нескучное тестирование с pytest - SlideShare', 'https://www.slideshare.net/imankulov/pytest-testing'),
            ('Test-Driven Development в Python для начинающих, часть ...',
             'https://shepetko.com/ru/blog/beginning-test-driven-development-in-python-2')]


mock_expected_extra_links_with_yandex_html = [[], [], [], [('Хвойные деревья — лучшие хвойные деревья и особенности их применения в ландшафтном дизайне (140 фото)', 'http://landshaftadvice.ru/xvojnye-derevya/'), ('Хавортия уход и посадка в домашних условиях: посадка, размножение и особенности выращивания (110 фото и видео)', 'http://landshaftadvice.ru/xavortiya-uxod/'), ('Хлебное дерево: 105 фото как выглядит, описание, выращивание и особенности употребления в пищу', 'http://landshaftadvice.ru/xlebnoe-derevo/'), ('Инженерные системы', 'http://landshaftadvice.ru/inzhenernye-sistemy/')], [], [], [('Комнатные растения', 'https://kvetok.ru/komnatnye-rasteniya'), ('Лиственные деревья', 'https://kvetok.ru/listvennye-derevya'), ('Лиственные кустарники', 'https://kvetok.ru/listvennye-kustarniki'), ('Эхинодорусы', 'https://kvetok.ru/rasteniya-dlya-akvariuma-i-vodoemov/e-hinodorusy'), ('Иксиолирион горный', 'https://kvetok.ru/rastenie/iksiolirion-gornyi'), ('Ирис безлистный', 'https://kvetok.ru/rastenie/iris-bezlistnyi'), ('Ирис кожистый', 'https://kvetok.ru/rastenie/iris-kozhistyi'), ('Ирис черепитчатый', 'https://kvetok.ru/rastenie/iris-cherepitchatyi'), ('Дидискус: виды и сорта, условия выращивания', 'https://kvetok.ru/travy/didiskus-vidy-i-sorta-uslovija-vyrashhivanija'), ('Гомфрена: виды и сорта, условия выращивания', 'https://kvetok.ru/travy/gomfrena-vidy-i-sorta-uslovija-vyrashhivanija'), ('Эндимион: виды и сорта, советы по разведению', 'https://kvetok.ru/travy/jendimion-vidy-i-sorta-sovety-po-razvedeniju'), ('Комнатные растения(505)', 'https://kvetok.ru/komnatnye-rasteniya'), ('Лиственные деревья(303)', 'https://kvetok.ru/listvennye-derevya'), ('Лиственные кустарники(280)', 'https://kvetok.ru/listvennye-kustarniki'), ('Эхинодорусы(16)', 'https://kvetok.ru/rasteniya-dlya-akvariuma-i-vodoemov/e-hinodorusy'), ('Импатиенс ампельный: лучшие сорта, как вырастить', 'https://kvetok.ru/komnatnye-rasteniya/impatiens-ampelnyj-luchshie-sorta-kak-vyrastit'), ('Пизония: особенности выращивания в квартире', 'https://kvetok.ru/komnatnye-rasteniya/pizonija-osobennosti-vyrashhivanija-v-kvartire'), ('Погонатерум: популярные виды, уход в домашних условиях', 'https://kvetok.ru/komnatnye-rasteniya/pogonaterum-populjarnye-vidy-uhod-v-domashnih-uslovijah'), ('Орбея: виды, советы по выращиванию', 'https://kvetok.ru/komnatnye-rasteniya/orbeja-vidy-sovety-po-vyrashhivaniju'), ('Пеллея: виды папоротника, особенности выращивания', 'https://kvetok.ru/komnatnye-rasteniya/pelleja-vidy-paporotnika-osobennosti-vyrashhivanija'), ('Аяния: виды, как разводить в домашних условиях', 'https://kvetok.ru/komnatnye-rasteniya/ajanija-vidy-kak-razvodit-v-domashnih-uslovijah'), ('Сидерасис: советы по выращиванию', 'https://kvetok.ru/komnatnye-rasteniya/siderasis-sovety-po-vyrashhivaniju'), ('Колокольчик персиколистый', 'https://kvetok.ru/rastenie/kolokolchik-persikolistyi')], [], [('Фестиваль в Аптекарском огороде "Репетиция весны"', 'http://www.blogs.plantopedia.ru/post/olgapetina/Festival-v-Aptekarskom-ogorode-Repetitciya-vesny/'), ('Выставка "Цветущая Азия", Москва, 12 февраля 2015-март 2015', 'http://www.blogs.plantopedia.ru/post/olgapetina/Vystavka-TCvetushaya-Aziya-Moskva-12-fevralya-2015/')], [('Доставка фруктовых корзин', 'https://www.cyber-florist.ru/zakazat-frukty.html'), ('благородные ирисы', 'https://cyber-florist.ru/flowers/irises'), ('ирисы', 'https://cyber-florist.ru/flowers/irises'), ('сиреневые ирисы роскошно смотрятся в тандеме с красными тюльпанами', 'https://cyber-florist.ru/order/violetta'), ('композиции, собранные из роз, лилий, ирисов', 'https://cyber-florist.ru/order/my-special-lady'), ('скомпоновать ирисы с герберами', 'https://cyber-florist.ru/order/celebration'), ('Строгие каллы сделают композицию ирисов богаче, эффектней', 'https://cyber-florist.ru/order/paradise'), ('Радуйте своих близких королевскими цветами ирисами - роскошными и символичными.', 'https://cyber-florist.ru/flowers/irises'), ('Яркая красочная корзина с цветами "Музыка красок"', 'https://cyber-florist.ru/news/music-of-colors/'), ('Яркий и нежный букет с брассикой "Утренняя звезда"', 'https://cyber-florist.ru/news/iarkii-i-niezhnyi-bukiet-s-brasikoi/')]]

expected_combined_results_with_yandex_results = [(('1 000+ Бесплатные Ирисы & Цветок изображения - Pixabay', 'https://pixabay.com/ru/images/search/%D0%B8%D1%80%D0%B8%D1%81%D1%8B/'), []), (('«Ирис» — сеть цветочных салонов', 'https://iris-flowers.ru/'), []), (('Ирисы | Natural Museum', 'https://natural-museum.ru/flora/%D0%B8%D1%80%D0%B8%D1%81%D1%8B'), []), (('Ирисы: 130 фото цветка и идей по украшению сада...', 'http://landshaftadvice.ru/irisy/'), [('Хвойные деревья — лучшие хвойные деревья и особенности их применения в ландшафтном дизайне (140 фото)', 'http://landshaftadvice.ru/xvojnye-derevya/'), ('Хавортия уход и посадка в домашних условиях: посадка, размножение и особенности выращивания (110 фото и видео)', 'http://landshaftadvice.ru/xavortiya-uxod/'), ('Хлебное дерево: 105 фото как выглядит, описание, выращивание и особенности употребления в пищу', 'http://landshaftadvice.ru/xlebnoe-derevo/'), ('Инженерные системы', 'http://landshaftadvice.ru/inzhenernye-sistemy/')]), (('Карликовые ирисы: сорта, описание, фото, посадка и уход', 'https://www.syl.ru/article/333595/karlikovyie-irisyi-sorta-opisanie-foto-posadka-i-uhod'), []), (('Садовая классификация ирисов', 'https://www.greeninfo.ru/grassy/iris_hybrida.html/Article/_/aID/4985'), []), (('Цветы бородатые ирисы: лучшие сорта, фото и названия...', 'https://kvetok.ru/tsvety-dlya-sada/iris-borodaty-j'), [('Комнатные растения', 'https://kvetok.ru/komnatnye-rasteniya'), ('Лиственные деревья', 'https://kvetok.ru/listvennye-derevya'), ('Лиственные кустарники', 'https://kvetok.ru/listvennye-kustarniki'), ('Эхинодорусы', 'https://kvetok.ru/rasteniya-dlya-akvariuma-i-vodoemov/e-hinodorusy'), ('Иксиолирион горный', 'https://kvetok.ru/rastenie/iksiolirion-gornyi'), ('Ирис безлистный', 'https://kvetok.ru/rastenie/iris-bezlistnyi'), ('Ирис кожистый', 'https://kvetok.ru/rastenie/iris-kozhistyi'), ('Ирис черепитчатый', 'https://kvetok.ru/rastenie/iris-cherepitchatyi'), ('Дидискус: виды и сорта, условия выращивания', 'https://kvetok.ru/travy/didiskus-vidy-i-sorta-uslovija-vyrashhivanija'), ('Гомфрена: виды и сорта, условия выращивания', 'https://kvetok.ru/travy/gomfrena-vidy-i-sorta-uslovija-vyrashhivanija'), ('Эндимион: виды и сорта, советы по разведению', 'https://kvetok.ru/travy/jendimion-vidy-i-sorta-sovety-po-razvedeniju'), ('Комнатные растения(505)', 'https://kvetok.ru/komnatnye-rasteniya'), ('Лиственные деревья(303)', 'https://kvetok.ru/listvennye-derevya'), ('Лиственные кустарники(280)', 'https://kvetok.ru/listvennye-kustarniki'), ('Эхинодорусы(16)', 'https://kvetok.ru/rasteniya-dlya-akvariuma-i-vodoemov/e-hinodorusy'), ('Импатиенс ампельный: лучшие сорта, как вырастить', 'https://kvetok.ru/komnatnye-rasteniya/impatiens-ampelnyj-luchshie-sorta-kak-vyrastit'), ('Пизония: особенности выращивания в квартире', 'https://kvetok.ru/komnatnye-rasteniya/pizonija-osobennosti-vyrashhivanija-v-kvartire'), ('Погонатерум: популярные виды, уход в домашних условиях', 'https://kvetok.ru/komnatnye-rasteniya/pogonaterum-populjarnye-vidy-uhod-v-domashnih-uslovijah'), ('Орбея: виды, советы по выращиванию', 'https://kvetok.ru/komnatnye-rasteniya/orbeja-vidy-sovety-po-vyrashhivaniju'), ('Пеллея: виды папоротника, особенности выращивания', 'https://kvetok.ru/komnatnye-rasteniya/pelleja-vidy-paporotnika-osobennosti-vyrashhivanija'), ('Аяния: виды, как разводить в домашних условиях', 'https://kvetok.ru/komnatnye-rasteniya/ajanija-vidy-kak-razvodit-v-domashnih-uslovijah'), ('Сидерасис: советы по выращиванию', 'https://kvetok.ru/komnatnye-rasteniya/siderasis-sovety-po-vyrashhivaniju'), ('Колокольчик персиколистый', 'https://kvetok.ru/rastenie/kolokolchik-persikolistyi')]), (('Ирис - мифы, легенды, история происхождения', 'https://mifflow.ru/iris.html'), []), (('Ирис', 'http://www.plantopedia.ru/encyclopaedia/garden-plants/details/i/iris/'), [('Фестиваль в Аптекарском огороде "Репетиция весны"', 'http://www.blogs.plantopedia.ru/post/olgapetina/Festival-v-Aptekarskom-ogorode-Repetitciya-vesny/'), ('Выставка "Цветущая Азия", Москва, 12 февраля 2015-март 2015', 'http://www.blogs.plantopedia.ru/post/olgapetina/Vystavka-TCvetushaya-Aziya-Moskva-12-fevralya-2015/')]), (('Ирисы - история, значение, советы', 'https://cyber-florist.ru/news/irisy-istoriia-znachieniie-soviety/'), [('Доставка фруктовых корзин', 'https://www.cyber-florist.ru/zakazat-frukty.html'), ('благородные ирисы', 'https://cyber-florist.ru/flowers/irises'), ('ирисы', 'https://cyber-florist.ru/flowers/irises'), ('сиреневые ирисы роскошно смотрятся в тандеме с красными тюльпанами', 'https://cyber-florist.ru/order/violetta'), ('композиции, собранные из роз, лилий, ирисов', 'https://cyber-florist.ru/order/my-special-lady'), ('скомпоновать ирисы с герберами', 'https://cyber-florist.ru/order/celebration'), ('Строгие каллы сделают композицию ирисов богаче, эффектней', 'https://cyber-florist.ru/order/paradise'), ('Радуйте своих близких королевскими цветами ирисами - роскошными и символичными.', 'https://cyber-florist.ru/flowers/irises'), ('Яркая красочная корзина с цветами "Музыка красок"', 'https://cyber-florist.ru/news/music-of-colors/'), ('Яркий и нежный букет с брассикой "Утренняя звезда"', 'https://cyber-florist.ru/news/iarkii-i-niezhnyi-bukiet-s-brasikoi/')])]


expected_combined_results_with_google_results = [(('Введение в PyTest - Alexander Demura - Medium', 'https://medium.com/@dmrlx/%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-pytest-cc6175c7d0dc'), []), (('PyTest / Хабр - Habr', 'https://habr.com/ru/post/269759/'), [('Python', 'https://habr.com/ru/hub/python/'), ('python', 'https://habr.com/ru/search/?q=%5Bpython%5D&target_type=posts'), ('                    Python Testing с pytest. Начало работы с pytest, Глава 1                  ', 'https://habr.com/ru/post/448782/'), ('                    Python Testing with pytest. Просто, Быстро, Эффективно и Масштабируемо. Предисловие и Ведение                  ', 'https://habr.com/ru/post/426699/'), ('Преподаватель PythonМосковская школа программистовМосквадо 100\xa0000', 'https://career.habr.com/vacancies/1000055443'), ('Программист PythonFirstVDSИркутскот 50\xa0000до 90\xa0000', 'https://career.habr.com/vacancies/1000055649'), ('Программист PythonСтроительный ДворМоскваот 150\xa0000до 200\xa0000', 'https://career.habr.com/vacancies/1000054566'), ('Программист PythonСтроительный ДворТюменьот 70\xa0000до 130\xa0000', 'https://career.habr.com/vacancies/1000053958'), ('Team Lead Python DeveloperYLabТольяттиМожно удаленноот 180\xa0000', 'https://career.habr.com/vacancies/1000055915'), ('www.slideshare.net/imankulov/pytest-testing', 'http://www.slideshare.net/imankulov/pytest-testing')]), (('Погружаемся в основы и нюансы тестирования Python-кода', 'https://proglib.io/p/python-testing/'), [('книги по Python', 'https://proglib.io/p/python-best-books/'), ('Инструменты для анализа кода Python. Часть 1', 'https://proglib.io/p/python-code-analysis/'), ('Инструменты для анализа кода Python. Часть 2', 'https://proglib.io/p/python-code-analysis-tools/'), ('13 лучших книг по Python для начинающих и продолжающих', 'https://proglib.io/p/python-best-books/'), ('ТОП-10 книг по Python: эффективно, емко, доходчиво', 'https://proglib.io/p/python-books/'), ('Realpython', 'https://realpython.com/python-testing/')]), (('PyTest - Python Дайджест', 'https://pythondigest.ru/view/7436/'), []), (('Все точки над И - разбираем фикстуры pytest - python ...', 'https://automated-testing.info/t/vse-tochki-nad-i-razbiraem-fikstury-pytest/8051'), [('python', 'https://automated-testing.info/tags/python'), ('http://habrahabr.ru/company/yandex/blog/242795/', 'http://habrahabr.ru/company/yandex/blog/242795/'), (' Python', 'http://lessons2.ru/python-for-testers?utm_source=atinfo&utm_medium=top_menu&utm_term=link&utm_campaign=reference'), (' Python', 'http://lessons2.ru/python-for-testers?utm_source=atinfo&utm_medium=top_menu&utm_term=link&utm_campaign=reference')]), (("Блог gigimon'а ← Немного про py.test", 'https://it4it.ru/2016/02/11/pytest-1/'), []), (('Тестирование в Python [unittest]. Часть 1. Введение', 'https://devpractice.ru/unit-testing-in-python-part-1/'), [('Книга “Линейная алгебра на Python”', 'https://devpractice.ru/book-linalg-python/'), ('Книга “Python. Уроки”', 'https://devpractice.ru/book-python-lessons/'), ('Книга “Python. unittest”', 'https://devpractice.ru/book-python-unittest/'), ('Python', 'https://devpractice.ru/python/'), ('Python. Уроки', 'https://devpractice.ru/python-lessons/'), ('Python [unittest]. Уроки', 'https://devpractice.ru/python-unittest-lessons/'), ('Python-разработчику', 'https://devpractice.ru/category/python/py-dev/'), ('Python', 'https://devpractice.ru/category/python/'), ('Тестирование в Python', 'https://devpractice.ru/category/python/testing-in-python/'), ('Python', 'https://devpractice.ru/tag/python/'), ('Тестирование в Python', 'https://devpractice.ru/tag/%d1%82%d0%b5%d1%81%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5-%d0%b2-python/'), ('← Python. Урок 15. Итераторы и генераторы', 'https://devpractice.ru/python-lesson-15-iterators-and-generators/'), ('Тестирование в Python [unittest]. Часть 2. TestCase →', 'https://devpractice.ru/unit-testing-in-python-part-2/'), ('Python', 'https://devpractice.ru/category/python/'), ('Python-разработчику', 'https://devpractice.ru/category/python/py-dev/'), ('Тестирование в Python', 'https://devpractice.ru/category/python/testing-in-python/'), ('Уроки по Python', 'https://devpractice.ru/category/python/python-lessons/'), ('Линейная алгебра на Python', 'https://devpractice.ru/category/machine-learning-and-data-analysis/linalg-on-py/'), ('Python. Урок 21. Работа с контекстным менеджером', 'https://devpractice.ru/python-lesson-21-context-manager/'), ('Python', 'https://devpractice.ru/category/python/')]), (('Нескучное тестирование с pytest - SlideShare', 'https://www.slideshare.net/imankulov/pytest-testing'), []), (('Test-Driven Development в Python для начинающих, часть ...', 'https://shepetko.com/ru/blog/beginning-test-driven-development-in-python-2'), [('http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137', 'http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137'), ('#Python', 'https://shepetko.com/ru/tag/python'), ('Декораторы в Python, часть 2', 'https://shepetko.com/ru/blog/python-decorators-2'), ('Декораторы в Python, часть 1', 'https://shepetko.com/ru/blog/python-decorators-1'), ('Абстрактные базовые классы в Python', 'https://shepetko.com/ru/blog/abstraktnye-bazovye-klassy-v-python'), ('Асинхронное программирование в Python, часть вторая', 'https://shepetko.com/ru/blog/asinkhronnoe-programmirovanie-v-python-2'), ('Асинхронное программирование в Python, часть первая', 'https://shepetko.com/ru/blog/asinkhronnoe-programmirovanie-v-python-1'), ('#Python', 'https://shepetko.com/ru/tag/python')])]

expected_extra_results_with_google_results = [[], [('Python', 'https://habr.com/ru/hub/python/'), ('python', 'https://habr.com/ru/search/?q=%5Bpython%5D&target_type=posts'), ('                    Python Testing с pytest. Builtin Fixtures, Глава 4                  ', 'https://habr.com/ru/post/448792/'), ('                    Python Testing с pytest. ГЛАВА 3 pytest Fixtures                  ', 'https://habr.com/ru/post/448786/'), ('                    Python Testing с pytest. Глава 2, Написание тестовых функций                  ', 'https://habr.com/ru/post/448788/'), ('                    Python Testing с pytest. Начало работы с pytest, Глава 1                  ', 'https://habr.com/ru/post/448782/'), ('                    Python Testing with pytest. Просто, Быстро, Эффективно и Масштабируемо. Предисловие и Ведение                  ', 'https://habr.com/ru/post/426699/'), ('Преподаватель PythonМосковская школа программистовМосквадо 100\xa0000', 'https://career.habr.com/vacancies/1000055443'), ('Программист PythonFirstVDSИркутскот 50\xa0000до 90\xa0000', 'https://career.habr.com/vacancies/1000055649'), ('Программист PythonСтроительный ДворМоскваот 150\xa0000до 200\xa0000', 'https://career.habr.com/vacancies/1000054566'), ('Team Lead Python DeveloperYLabТольяттиМожно удаленноот 180\xa0000', 'https://career.habr.com/vacancies/1000055915'), ('Python-разработчикОнлайн-кинотеатр iviМоскваот 140\xa0000до 190\xa0000', 'https://career.habr.com/vacancies/11035166'), ('www.slideshare.net/imankulov/pytest-testing', 'http://www.slideshare.net/imankulov/pytest-testing'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')], [('книги по Python', 'https://proglib.io/p/python-best-books/'), ('Инструменты для анализа кода Python. Часть 1', 'https://proglib.io/p/python-code-analysis/'), ('Инструменты для анализа кода Python. Часть 2', 'https://proglib.io/p/python-code-analysis-tools/'), ('13 лучших книг по Python для начинающих и продолжающих', 'https://proglib.io/p/python-best-books/'), ('ТОП-10 книг по Python: эффективно, емко, доходчиво', 'https://proglib.io/p/python-books/'), ('Realpython', 'https://realpython.com/python-testing/')], [('ffmpeg-python - FFmpeg binding с поддержкой фильтрации', 'http://github.com/kkroening/ffmpeg-python'), ('Функции-таймеры в Python', 'https://realpython.com/python-timer/')], [('python', 'https://automated-testing.info/tags/python'), ('http://habrahabr.ru/company/yandex/blog/242795/', 'http://habrahabr.ru/company/yandex/blog/242795/'), (' Python', 'http://lessons2.ru/python-for-testers?utm_source=atinfo&utm_medium=top_menu&utm_term=link&utm_campaign=reference'), (' Python', 'http://lessons2.ru/python-for-testers?utm_source=atinfo&utm_medium=top_menu&utm_term=link&utm_campaign=reference')], [], [('Книга “Линейная алгебра на Python”', 'https://devpractice.ru/book-linalg-python/'), ('Книга “Python. Уроки”', 'https://devpractice.ru/book-python-lessons/'), ('Книга “Python. unittest”', 'https://devpractice.ru/book-python-unittest/'), ('Python', 'https://devpractice.ru/python/'), ('Python. Уроки', 'https://devpractice.ru/python-lessons/'), ('Python [unittest]. Уроки', 'https://devpractice.ru/python-unittest-lessons/'), ('Python-разработчику', 'https://devpractice.ru/category/python/py-dev/'), ('Python', 'https://devpractice.ru/category/python/'), ('Тестирование в Python', 'https://devpractice.ru/category/python/testing-in-python/'), ('Python', 'https://devpractice.ru/tag/python/'), ('Тестирование в Python', 'https://devpractice.ru/tag/%d1%82%d0%b5%d1%81%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5-%d0%b2-python/'), ('← Python. Урок 15. Итераторы и генераторы', 'https://devpractice.ru/python-lesson-15-iterators-and-generators/'), ('Тестирование в Python [unittest]. Часть 2. TestCase →', 'https://devpractice.ru/unit-testing-in-python-part-2/'), ('Python', 'https://devpractice.ru/category/python/'), ('Python-разработчику', 'https://devpractice.ru/category/python/py-dev/'), ('Тестирование в Python', 'https://devpractice.ru/category/python/testing-in-python/'), ('Уроки по Python', 'https://devpractice.ru/category/python/python-lessons/'), ('Линейная алгебра на Python', 'https://devpractice.ru/category/machine-learning-and-data-analysis/linalg-on-py/'), ('Python. Урок 21. Работа с контекстным менеджером', 'https://devpractice.ru/python-lesson-21-context-manager/'), ('Python', 'https://devpractice.ru/category/python/')], [('http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137', 'http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137'), ('#Python', 'https://shepetko.com/ru/tag/python'), ('Декораторы в Python, часть 2', 'https://shepetko.com/ru/blog/python-decorators-2'), ('Декораторы в Python, часть 1', 'https://shepetko.com/ru/blog/python-decorators-1'), ('Абстрактные базовые классы в Python', 'https://shepetko.com/ru/blog/abstraktnye-bazovye-klassy-v-python'), ('Асинхронное программирование в Python, часть вторая', 'https://shepetko.com/ru/blog/asinkhronnoe-programmirovanie-v-python-2'), ('Асинхронное программирование в Python, часть первая', 'https://shepetko.com/ru/blog/asinkhronnoe-programmirovanie-v-python-1'), ('#Python', 'https://shepetko.com/ru/tag/python')]]