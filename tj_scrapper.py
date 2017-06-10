import requests
from lxml import html


def trim(text):
    return text.replace('\n', '').strip()


def get_posts():
    page = requests.get('https://tjournal.ru/tweets')
    tree = html.fromstring(page.content)
    posts = []
    for i in range(1, 51):
        post = ''
        name = tree.xpath(
            './/*[@id=\'l-container\']/div[4]/div/main/div/div[1]/div/div[' + str(i) + ']/div[1]/a/text()')
        tw = tree.xpath('.//*[@id=\'l-container\']/div[4]/div/main/div/div[1]/div/div[' + str(i) + ']/div[2]/a/text()')
        text = tree.xpath('.//*[@id=\'l-container\']/div[4]/div/main/div/div[1]/div/div[' + str(i) +
                          ']/div[4]/descendant-or-self::*/text()')

        quote_name = tree.xpath('.//*[@id=\'l-container\']/div[4]/div/main/div/div[1]/div/div[' + str(i) +
                                ']/div[5]/div/div[1]/text()')
        quote_tw = tree.xpath('.//*[@id=\'l-container\']/div[4]/div/main/div/div[1]/div/div[' + str(i) +
                              ']/div[5]/div/div[2]/text()')
        quote_text = tree.xpath('.//*[@id=\'l-container\']/div[4]/div/main/div/div[1]/div/div[' + str(i) +
                                ']/div[5]/div/div[3]/text()')
        likes = []
        div = 0
        while not len(likes) > 0:
            likes = tree.xpath('.//*[@id=\'l-container\']/div[4]/div/main/div/div[1]/div/div[' + str(i) +
                               ']/div[' + str(div) + ']/a[3]/u/text()')
            div += 1

        post += str(name[0] + ' ' + tw[0] + '\n')

        out_text = ''
        if len(text) > 0:
            for part in text:
                out_text += part
            post += (str(out_text) + '\n')

        if len(quote_name) > 0:
            post += ('    "' + trim(quote_name[0]) + '   ' + trim(quote_tw[0]) + '\n')
            post += ('    ' + trim(quote_text[0]) + '"' + '\n')
        post += ('likes: ' + likes[0] + '\n')
        post += '\n'

        posts.append(post)

    return posts

if __name__ == '__main__':
    posts = get_posts()
    for post in posts:
        print(post)
