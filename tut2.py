import pandas as pd
import geopandas
pd.options.display.max_rows = 10

countries = geopandas.read_file("zip://.//ne_110m_admin_0_countries.zip")
cities = geopandas.read_file("zip://.//ne_110m_populated_places.zip")
rivers = geopandas.read_file("zip://.//ne_50m_rivers_lake_centerlines.zip")

belgium = countries.loc[countries['NAME'] == 'Belgium', 'geometry'].squeeze()

paris = cities.loc[cities['NAME'] == 'Paris', 'geometry'].squeeze()
brussels = cities.loc[cities['NAME'] == 'Brussels', 'geometry'].squeeze()

from shapely.geometry import LineString
line = LineString([paris, brussels])

geopandas.GeoSeries([belgium, paris, brussels, line]).plot(cmap='tab10')

brussels.within(belgium)
belgium.contains(brussels)
belgium.contains(paris)
paris.within(belgium)
line.intersects(belgium)

amazon = rivers[rivers['name'] == 'Amazonas'].geometry.squeeze()
countries[countries.crosses(amazon)]  # or .intersects

geopandas.GeoSeries([belgium, brussels.buffer(1)]).plot(alpha=0.5, cmap='tab10')

brussels.buffer(1).intersection(belgium)
brussels.buffer(1).union(belgium)
brussels.buffer(1).difference(belgium)

africa_countries = countries[countries['CONTINENT'] == 'Africa']
africa = africa_countries.unary_union
africa
print(str(africa)[:1000])
