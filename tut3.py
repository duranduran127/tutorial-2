%matplotlib inline

import pandas as pd
import geopandas

pd.options.display.max_rows = 10

countries = geopandas.read_file("zip://.//ne_110m_admin_0_countries.zip")
cities = geopandas.read_file("zip://.//ne_110m_populated_places.zip")
rivers = geopandas.read_file("zip://.//ne_50m_rivers_lake_centerlines.zip")

cities2 = cities[cities['NAME'].isin(['Bern', 'Brussels', 'London', 'Paris'])].copy()
cities2['iso_a3'] = ['CHE', 'BEL', 'GBR', 'FRA']

cities2

countries2 = countries[['ISO_A3', 'NAME', 'CONTINENT']]
countries2.head()

cities2.merge(countries2, on='ISO_A3')

france = countries.loc[countries['NAME'] == 'France', 'geometry'].squeeze()
cities.within(france)

cities[cities.within(france)]

joined = geopandas.sjoin(cities, countries, op='within', how='left')
joined
joined['continent'].value_counts()

africa = countries[countries['continent'] == 'Africa']
africa.plot()
cities['geometry'] = cities.buffer(2)
geopandas.overlay(africa, cities, how='difference').plot()
