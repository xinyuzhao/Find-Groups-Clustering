import feedparser
import re

low_bound = 0.1
up_bound = 0.5
remove_tag_reg = re.compile(r'<[^>]+>')
split_word_reg = re.compile(r'[^A-Z^a-z-]+')

def getWords(html):
    """
    Parse string by nonalphabetical char.

    Paramters:
    html: str

    Returns:
    A list of strs
    """

    # Remove all the HTML tags
    txt = remove_tag_reg.sub('', html)

    # Split words by all non-alpha characters
    words = split_word_reg.split(txt)

    return [word.lower() for word in words if words != '']


def getWordCounts(url):
    """
    Extract all words from a RSS feed. 

    Parameters
    ----------
    url: str

    Returns
    -------
    title: str
    wc: dict
    """

    d = feedparser.parse(url)
    wc = {}

    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        try: 
            words = getWords(e.title + ' ' + summary)
            for word in words:
                wc.setdefault(word, 0)
                wc[word] += 1

        except Exception as e:
            print(e)

    if wc:
        return d.feed.title, wc  
    else:
        return '', wc


if __name__ == '__main__': 
    apcount = {}
    wordcounts = {}
    
    with open('url_list.txt') as f:
        url_list = f.readlines()

    for url in url_list:
        feedurl = url.rstrip()
        print(feedurl)
        title, wc = getWordCounts(feedurl)

        if not wc:
            continue

        wordcounts[title] = wc

        for word, count in wc.items():
            apcount.setdefault(word, 0)
            if count > 1 and len(word) > 2:
                apcount[word] += 1

    useful_word_list = []
    list_len = len(url_list)
    for word, count in apcount.items():
        freq = count / list_len
        if freq > low_bound and freq < up_bound:
            useful_word_list.append(word)

    print(useful_word_list)

    out = open('blog_data.txt', 'w')
    out.write('Blog')
    for word in useful_word_list:
        out.write('\t%s' % word)
    out.write('\n')
    for title, wc in wordcounts.items():
        out.write(title)
        for word in useful_word_list:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
        out.write('\n')






