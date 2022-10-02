# U.S. Congress Age Analysis

## Summary

This project was inspired by an [article]( https://www.businessinsider.com/gerontocracy-united-states-congress-red-white-and-gray-data-charts-2022-9) published in Business Insider titled "The oldest government in history," by Annie Fu, Walt Hickey, and Shayanne Gal.  This article highlighted the increasing median age of the U.S. Congress over time, and after reading it I was interested in doing my own analysis on the data referenced within the article.  Specifically I was interested in looking at the changes in age range distribution of U.S. Congress over the years, which was not included in their original article.

I utilized Python to prep the obtained data files (discussed below), and Tableau Public to create the data visualizations.  [Please click here to view the Tableau data visualation of this data.](https://public.tableau.com/app/profile/johnny.kile/viz/U_S_CongressAgeVisualization/DashboardFinal)

## Analysis

### Data Preparation

This analysis utilized data from the following sources:

* The *.json files located in the data/ folder were obtained from the [@unitedstates/congress-legislators repository](https://github.com/unitedstates/congress-legislators). The files contain information about the legislators in congress including name, birthdate, party, type of representative (senate vs house), and other miscellaneous information that was not utilized in this analysis.  
* The *.csv files located in the data/ folder were obtained from the [United States Census Bureau data website](https://data.census.gov/cedsci/). The files contain information regarding the median age of the U.S. population within a given year, as identified by the filenames.  The files ranged in date from 2010-2021, however 2020 was missing.

The `dataprep_legislators.py` script was used to load the *.json files into a pandas DataFrame, manipulate the data (i.e. calculate age of each legislator during a given year), combine the data from the two files, and export as an Excel sheet for use in Tableau.  The data in the exported file ranged from the years 1789-2022. 

The `dataprep_census.py` script was used to extract the median age of the U.S. population from the multiple *.csv files into a single DataFrame, and export as an Excel sheet for use in Tableau.  The data in the exported file range from the years 2010-2021, with 2020 omitted (as noted above). 

### Data Visualization

Note, all images shown below can be viewed on the dashboard published on Tableau Public.  [Click here to view the dashboard](https://public.tableau.com/app/profile/johnny.kile/viz/U_S_CongressAgeVisualization/DashboardFinal).

The median age of the U.S. Congress was plotted over time, as shown in the chart below.  For reference, the median age of the U.S. Congress in 2021 was 60 compared to the median age of the U.S. population being 39.

![](https://github.com/JohnnyKile/US-Legislator-Age-Analysis/blob/main/images/1-AgeOverTime-LineChart.png?raw=true)

The chart showed that in recent years, since 1980 through 2022, the median age of the U.S. Congress has steadily increased from 51 years old to 61. This chart also showed that 90% of the 2022 U.S. Congress was above the age of 44.  For comparison, 75% of the 1980 U.S. Congress was older than 43.  The percentiles pushed me to explore the age range distribution a bit more to further understand the data.  I utilized Tableau to put the ages into bins utilizing ranges of 10 years with the exception of the upper range.  The bins were as follows: 25-34, 35-44, 45-54, 55-64, 65-74, 75+.  The age distribution data was visualized using an area chart with a continuous year axis, as well as using a heat map, with year intervals of 20, per below.

![](https://github.com/JohnnyKile/US-Legislator-Age-Analysis/blob/main/images/2-AgeRangeDistribution-AreaChart.png?raw=true)

![](https://github.com/JohnnyKile/US-Legislator-Age-Analysis/blob/main/images/3-AgeRangeDistribution-HeatMap.png?raw=true)

These two visualizations showed that the proportion of congress made up of people in the 25-34 and 35-44 age ranges were generally shrinking over time, while the proportion of congress made up of legislators in the 55-64, 65-74, and 75+ age ranges were growing. For example, from 1980 to 2020 the percentage of the U.S. Congress that was aged 35-44 dropped more than half, from 25.14% to 11.23%.  Meanwhile the percentage of the U.S. Congress aged 65-74 almost tripled, from 10.28% in 1980, to 29.10% in 2020. (Note: values for the other groups and years can be viewed on the [Tableau dashboard](https://public.tableau.com/app/profile/johnny.kile/viz/U_S_CongressAgeVisualization/DashboardFinal)).

### Other Analysis

I also plotted the median age after grouping by party (republican VS democrat) and charted the median age of legislators that were serving their first year, in an attempt to find patterns with respect to whether the parties differ or whether first-time candidates are generally getting older. Generally, the parties were closely aligned and did not differ enough to warrant discussion.  The chart of the first year legislator ages was choppy and was also left out of this section.  In addition, when broken out by the senate and house, the senate median age was generally 5 years older than the house median age which made sense given their differing age limits (25 in the house vs 30 in congress), and thus was not worth including as well.

## Conclusion

Overall, the data showed that in general U.S. Congress has been steadily getting older.  The data within this analysis only looked at the trend of the age range distrbution changes, and did not shed any light onto the cause.  The next steps in my analysis would be to do additional research and bring in additional data in order to help determine factors that contributed to the rise in median age of U.S. Congress, especially in recent years from 1980-2022.  An idea of the outside research I would look into would be the following:

- According to [OpenSecrets.org](https://www.opensecrets.org/elections-overview/cost-of-election?cycle=2020&display=T&infl=N), the money spent in congressional elections has increased from $1.6 billion in 1998, to $5.7 billion in 2018, and up to $8.7 billion in 2020.  As the money spent on elections has steadily risen, has it created a barrier to entry for younger people that would generally have less access to funds than older people?  
- With respect to the costs noted above, how has the internet and social media changed how races are run, and how funds can be raised?  How will the ease of access to people granted by social media in the very recent years (Facebook was launched in 2004) change how the age range distribution looks in the coming decades?  
- Generally it's said that younger people are less inclined to vote in elections, especially in midterms, which would affect the legislators that make up U.S. Congress.  Has the age range distribution of people voting in elections over time changed to match the charts above of U.S. Congress, or has it remained fairly consistent (young people vote less, older people vote more)?
- It's worth noting that in 2020, the ages of the millennial generation (1981-1996) ranged from 24-39, and the ages of generation X (1965-1980) ranged from 40-55.  Both generations make up the group with decreased proportional representation in U.S. Congress in 2020.  In 2020, Baby Boomers were 55-73 (1946-1964), and made up a much larger portion of U.S. Congress.  Is this a factor of overall population numbers within the generations, or another phenomena (some noted above)?  
- It may seem insignificant but has the general negative connotation of the term 'millennial' hindered candidates within that group from breaking into U.S. Congress, or are they just not running in elections?

Note that the list above is just the tip of the iceberg, there are certainly more avenues to explore that may help explain the shift seen in the above visualizations.  This project was only initially limited to an analysis of the data files outlined above, however I will bring in new data as applicable in the future and continue building out this analysis.