import requests
from bs4 import BeautifulSoup
from tmp_test import get_test_page

# https://www.google.com/
# search?q=%BE%D0%B9+%D0%BA%D0%BE%D1%88%D0%BA%D0%B8&oq=%D0%BA%D1%83
# &aqs=chrome.0.69i59l3j35i39j69i57j69i61l3.4708j1j7  &aqs=chrome..69i57j0.1380j0j9
# &sourceid=chrome&ie=UTF-8

g_local_link = ''
g_page = get_test_page(g_local_link)


def get_google_links(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('div', id="search").find_all('a')
    new_links = []
    results = []

    for h in range(len(links)):
        if links[h].find('h3', class_='LC20lb') is not None:
            new_links.append(links[h])

    for r in new_links:
        link = r.get('href')
        head = r.find('h3').string
        rs = head, link
        results.append(rs)

    return results

# https://www.google.com/search?q=%D0%BF%D0%B0%D1%80%D1%81%D0%B5%D1%80&oq=%D0%BF%D0%B0%D1%80%D1%81%D0%B5%D1%80&aqs=chrome..69i57j0l5j69i61j69i60.3921j1j7&sourceid=chrome&ie=UTF-8
#
# <div class="rc">
# <div class="r">
# <a href="https://www.wordreference.com/enru/Christmas" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://www.wordreference.com/enru/Christmas&amp;ved=2ahUKEwjkh4yhiKbmAhWM1aYKHT6qAasQFjAPegQIAxAB" target="_blank" rel="noopener">
# <h3 class="LC20lb"><span class="S3Uucc">Christmas - Англо-русский словарь на WordReference.com</span></h3><br>
# <div class="TbwUpd"><cite class="iUh30 bc">https://www.wordreference.com › enru › Christmas</cite></div></a><span>
# <div class="action-menu ab_ctl"><a class="GHDvEf ab_button" href="https://www.google.ru/search?ie=UTF-8&amp;hl=ru&amp;q=christmas#" id="am-b15" aria-label="Параметры" aria-expanded="false" aria-haspopup="true" role="button" jsaction="m.tdd;keydown:m.hbke;keypress:m.mskpe" data-ved="2ahUKEwjkh4yhiKbmAhWM1aYKHT6qAasQ7B0wD3oECAMQBA">
# <span class="mn-dwn-arw"></span></a><div class="action-menu-panel ab_dropdown" role="menu" tabindex="-1" jsaction="keydown:m.hdke;mouseover:m.hdhne;mouseout:m.hdhue" data-ved="2ahUKEwjkh4yhiKbmAhWM1aYKHT6qAasQqR8wD3oECAMQBQ"><ol><li class="action-menu-item ab_dropdownitem" role="menuitem"><a class="fl" href="https://webcache.googleusercontent.com/search?q=cache:ELjxyhWWIZsJ:https://www.wordreference.com/enru/Christmas+&amp;cd=16&amp;hl=ru&amp;ct=clnk&amp;gl=ru" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://webcache.googleusercontent.com/search%3Fq%3Dcache:ELjxyhWWIZsJ:https://www.wordreference.com/enru/Christmas%2B%26cd%3D16%26hl%3Dru%26ct%3Dclnk%26gl%3Dru&amp;ved=2ahUKEwjkh4yhiKbmAhWM1aYKHT6qAasQIDAPegQIAxAG" target="_blank" rel="noopener">Сохраненная&nbsp;копия</a></li></ol></div></div></span></div>
# <div class="s"><div><span class="st"><em>Christmas</em> - Бесплатный онлайн словарь. 210 000 слов, выражений и переводов, плюс форумы для обсуждения.</span></div></div></div>
