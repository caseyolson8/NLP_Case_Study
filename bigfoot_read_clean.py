import json # to work with json file format
from bs4 import BeautifulSoup # to parse html
import pandas as pd




def bf_pull_observation(soup_record):
    text = ''
    for elem in soup_record.find_all('span', {'class': 'field'}):
        if elem.getText() == 'OBSERVED:':
            text = elem.parent.getText()[10:]
    return text

def bf_pull_date(soup_record):
    month, year = '',0
    for elem in soup_record.find_all('span', {'class': 'field'}):
        if elem.getText()  == 'YEAR:':
            year = elem.parent.getText()[6:]
        if elem.getText()  == 'MONTH:':
            month = elem.parent.getText()[7:]
    return month, year

def bf_pull_county_state(soup_record):
    county, state = '',''
    for elem in soup_record.find_all('span', {'class': 'field'}):
        if elem.getText()  == 'STATE:':
            county = elem.parent.getText()[7:]
        if elem.getText()  == 'COUNTY:':
            state = elem.parent.getText()[8:]
    return county, state

def bf_pull_class(soup_record):
    level = ''
    for elem in soup_record.find_all('span', {'class': 'reportclassification'}):
        level = elem.getText()[-2]
        return level
    return ''


if __name__ == "__main__":
    bf_df = pd.read_json('data/bigfoot_data.json', lines =True)
    bf_htmls = bf_df['html'].values

    counties = []
    states = []
    months = []
    years = []
    observations = []
    levels = []

    for html in bf_htmls:
        soup = BeautifulSoup(html, 'html.parser')
        
        observations.append(bf_pull_observation(soup))
        
        mn, yr = bf_pull_date(soup)
        months.append(mn)
        years.append(yr)
        
        st, cty = bf_pull_county_state(soup)
        counties.append(cty)
        states.append(st)
    
        levels.append(bf_pull_class(soup))


    bf_parsed = pd.DataFrame([months, years, counties, states, levels, observations]).T
    bf_parsed.columns = ['Month', 'Year', 'County', 'State', 'Class', 'Observation']
    bf_parsed['Obs_word_count'] = bf_parsed['Observation'].apply(lambda x: len(x.split(' ')))


    bf_filt = bf_parsed[bf_parsed['Obs_word_count']>20]
    bf_filt.to_csv('parsed_bf_test.csv')


