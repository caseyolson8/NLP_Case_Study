from bs4 import BeautifulSoup

def parser(row):
    '''
    Basic HTML parser hard coded to find "td" tags and process them in a
    pandas DataFrame
    Need to uncomment out text or table to pull appropriate data
    '''
    soup = BeautifulSoup(row, 'html.parser')
    try:
        td = soup.find_all('td')
        table = str(td[0]).replace('<td bordercolor="#d0d7e5"><font color="#000000" face="Calibri" style="FONT-SIZE:11pt">', '')\
                .replace('</font></td>', '').split('<br/>')
        #text = td[1].get_text()
        return table
        #return text
    except IndexError:
        return row


def table_parser(row, n):
    if len(row) == 6:
        return row[n]
    else:
        return row

def removal(row, name):
    return row.replace(f'{name}:','').replace(f'{name} :','').replace('<td bordercolor="#c0c0c0"><font color="#000000" face="Arial" style="FONT-SIZE:10pt">', '').strip()


def duration_cleaner(row, words):
    if len(row) == 0:
        return 'Unknown'
    else:
        row = row.replace('+','').replace('~', '').replace('&gt;', '').replace('&lt;','')
        row = row.replace('one', '1').replace('One', '1').replace('two', '1').replace('five', '5').replace('ten', '10').replace('three', '3')
        for word in words:
            row = row.replace(word, ' ')
        return row

def bagofwords(df, col_name):
    corpus = df[col_name].values.tolist()
    words = []
    for phrase in corpus:
        text = phrase.split()
        for word in text:
            if word in ['minute', 'minutes', 'mimutes', 'mimute', 'minutess', 'minutes?', 'mintues', 'minuts',
                        'minuets', 'mints', 'min', 'mins', 'min.',
                        'Min.', 'Mins', 'Mins.', 'mins.', 'Min', 'Minutes', 'Minute', 'mins.', 'Min', 'Minutes',
                        'Minute', 'minutes,', 'minutes.', 'minuites', 'minites', 'min?',
                        'MINUTES', 'SECONDS', 'MIN', 'MIN.', 'MINS', 'MINUTE', 'HOURS', 'HOUR', 'HRS.', 'SEC', 'SEC.',
                        'SECS', 'HRS',
                        'second', 'seconds', 'sec', 'sec.', 'secs', 'secs.', 'Sec.', 'Sec', 'seconds?', 'Seconds',
                        'Second', 'secounds', 'seconds.',
                        'hour', 'hours', 'Hour', 'Hours', 'hr', 'hr.', 'hrs.', 'hrs', 'hours?',
                        'ongoing', 'Ongoing', 'day', 'days', 'unknown', 'Unknown', 'UNKNOWN', 'to']:
                pass
            elif word.isdigit():
                pass
            elif word[0].isdigit():
                pass
            else:
                words.append(word)
    return words