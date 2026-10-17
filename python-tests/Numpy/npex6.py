import numpy as np
countries = np.array(['luxembourg','Norway','Japan','Switzerland','USA'])
gdp_per_capita = np.array([52056.1234,40345.4565,45456.78564,33245.56782,34544.45888])

#max gdp per capita
max_gdp_per_capita = gdp_per_capita.argmax()
print(max_gdp_per_capita)

country_with_max_gdp_per_capita = countries[max_gdp_per_capita]
print(country_with_max_gdp_per_capita)

min_gdp_per_capital = gdp_per_capita.argmin()
print(min_gdp_per_capital)

country_with_min_gdp_per_capita = countries[min_gdp_per_capital]
print(country_with_min_gdp_per_capita)

#printing values iteratively
for country in countries:
    print('ecalculating country {}'.format(country))

for i in range(0,len(countries)-1):
    country = countries[i]
    country_gdp_per_capita = gdp_per_capita[i]
    print('country {} per capita gdp is {}'.format(country,country_gdp_per_capita))

print(gdp_per_capita.max())
print(gdp_per_capita.min())
print(gdp_per_capita.mean())
print(gdp_per_capita.std())





