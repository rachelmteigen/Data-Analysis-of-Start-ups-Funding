#!/usr/bin/env python
from os import getcwd
from os.path import join


def columns_of_interest():
  return ['ascii_name', 'latitude', 'longitude', 'population', 'Total Funding Amount']

def extract(filename='US.tsv', delimiter='\t', encoding='ISO-8859-1'):
  from pandas import read_csv

  data = read_csv(join(getcwd(), '..', 'data', filename), 
                      delimiter=delimiter,
                      encoding=encoding)

  return data[columns_of_interest()]


def filter_data(df):
  return df[df['population'] != 0]


def cities_of_interest(df, cities):
  return df[df['ascii_name'].isin(cities)]


def extract_cities_of_interest(cities):
  return cities_of_interest(filter_data(extract()), cities)


if __name__ == '__main__':
  df = extract_cities_of_interest(['San Francisco', 'Chicago'])
  df.head()
  print(len(df))
