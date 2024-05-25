---
title: 'Capstone Project The Battle Of Neighborhoods'
date: 2021-01-03
permalink: /posts/2021-01/Capstone-Project/
tags:
  - cool posts
  - category1
  - category2
---

Capstone Project — The Battle of Neighborhoods
 \* {
 font-family: Georgia, Cambria, "Times New Roman", Times, serif;
 }
 html, body {
 margin: 0;
 padding: 0;
 }
 h1 {
 font-size: 50px;
 margin-bottom: 17px;
 color: #333;
 }
 h2 {
 font-size: 24px;
 line-height: 1.6;
 margin: 30px 0 0 0;
 margin-bottom: 18px;
 margin-top: 33px;
 color: #333;
 }
 h3 {
 font-size: 30px;
 margin: 10px 0 20px 0;
 color: #333;
 }
 header {
 width: 640px;
 margin: auto;
 }
 section {
 width: 640px;
 margin: auto;
 }
 section p {
 margin-bottom: 27px;
 font-size: 20px;
 line-height: 1.6;
 color: #333;
 }
 section img {
 max-width: 640px;
 }
 footer {
 padding: 0 20px;
 margin: 50px 0;
 text-align: center;
 font-size: 12px;
 }
 .aspectRatioPlaceholder {
 max-width: auto !important;
 max-height: auto !important;
 }
 .aspectRatioPlaceholder-fill {
 padding-bottom: 0 !important;
 }
 header,
 section[data-field=subtitle],
 section[data-field=description] {
 display: none;
 }
 

Capstone Project — The Battle of Neighborhoods
==============================================




Applied Data Science Capstone




---

![](https://cdn-images-1.medium.com/max/800/1*3zbPopZdR6-WR8yvw5RmEQ.jpeg)### Capstone Project — The Battle of Neighborhoods

### Applied Data Science Capstone

### Peer-graded Assignment: Capstone Project — The Battle of Neighborhoods

*IBM Data Science Professional*

**Introduction/Business Problem**

This study aims to help people who are planning to open a new restaurant in Toronto to choose the right location by providing data about each neighborhood’s income and population and the competitors already present in the same regions.

**Data**

To provide the stakeholders with the necessary information, I’ll be combining Toronto’s 2016 Census with population, the average income per Neighborhood with Toronto’s Neighborhoods shapefile, and Foursquare API to collect competitors in the same neighborhoods

Toronto’s Census data is publicly available at this [**website**](https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-catalogue/#8c732154-5012-9afe-d0cd-ba3ffc813d5a)

Toronto Neighborhoods’ shapefile is publicly available at this [**website**](https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-catalogue/#a45bd45a-ede8-730e-1abc-93105b2c439f)

Based on the definition of our problem, the factors that will influence our decision are:

* number of existing restaurants in the neighborhood (any restaurant)
* number of and distance to Italian restaurants in the district, if any
* distance of neighborhood from city center

We decided to use the regularly spaced grid of locations, centered around the city center, to define our neighborhoods.

Following data sources will be needed to extract/generate the required information:

* centers of candidate areas will be developed algorithmically, and approximate addresses of centers of those areas will be obtained using *Google Maps API reverse geocoding*
* number of restaurants and their type and location in every neighborhood will be obtained using *Foursquare API*
* coordinate of Toronto center will be obtained using *Google Maps API geocoding* of well known Toronto location.

**Methodology**

For this report, I used a few different maps that could help a new investor to decide the best neighborhood to open a restaurant in Toronto, based on its income, population, and available competitors. To do that, I’ve used the 2016 Census information combined with *choropleth* maps to visually display the wealthier and more populational neighborhoods and *Foursquare* data to display the current restaurants in each region.

**Results**

Comparing the maps, we can notice most of the restaurants grouped on main streets and the south of the city, although some of the wealthiest neighborhoods are up to the north. Also, the areas with a dense population don’t reflect the number of restaurants.

**Discussion**

When I first decided to create this study, I was expecting to find clusters of restaurants in certain regions, and the final result didn’t meet that expectation.

**Conclusion**

This report may help someone plan to open a Toronto restaurant by comparing the current offers and neighborhood profiles. However, it may not cover all variables such as access to public transportation or even the restaurant profiles, so it shall not be used as a single decision-making tool.



By [Dr. Farruh](https://medium.com/@k-farruh) on [January 3, 2021](https://medium.com/p/9d462abb8aec).

[Canonical link](https://medium.com/@k-farruh/capstone-project-the-battle-of-neighborhoods-9d462abb8aec)

Exported from [Medium](https://medium.com) on May 25, 2024.

