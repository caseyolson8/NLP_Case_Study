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