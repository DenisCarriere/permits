Data Processing
===============

OpenData is nice to have, however many of the times it needs a lot of work before it can be
"Useful" data. This GitHub page shows you all the data transformations that was used when processing
data collected from the City of Ottawa's Data Cataloge.

![Overview]

**Download [Shapefile]**

City of Ottawa Permits
----------------------

Construction, Demolition, Pool Enclosure Permits

- [2011]
- [2012]
- [2013]
- [2014] 

Download
--------

- [Shapefile]
- [Excel]
- [KML]
- [CSV]
- [GeoJSON]

Transformations
---------------

- Geo-reference Data [#2]
- Add confidence score [#18]
- Convert to Integer [#17]
- Standard Fieldnames [#4], [#5], [#12], [#14]
- Clean Values [#9], [#10], [#11], [#13]
- Standard Filename [#6], [#7], [#8]

Extra Help
----------

- City of Ottawa - [Open Data Catalog]
- City of Ottawa - [LICENSE]
- [OpenRefine]

[Overview]: https://raw.githubusercontent.com/DenisCarriere/permits/master/Images/Overview.png
[Shapefile]: https://github.com/DenisCarriere/permits/raw/master/Download/permits.shp.zip
[GeoJSON]: https://github.com/DenisCarriere/permits/raw/master/Download/permits.geojson.zip
[Excel]: https://github.com/DenisCarriere/permits/raw/master/Download/permits.xls.zip
[KML]: https://github.com/DenisCarriere/permits/raw/master/Download/permits.kml.zip
[CSV]: https://github.com/DenisCarriere/permits/raw/master/Download/permits.csv.zip
[#1]: https://github.com/DenisCarriere/permits/issues/1
[#2]: https://github.com/DenisCarriere/permits/issues/2
[#3]: https://github.com/DenisCarriere/permits/issues/3
[#4]: https://github.com/DenisCarriere/permits/issues/4
[#5]: https://github.com/DenisCarriere/permits/issues/5
[#6]: https://github.com/DenisCarriere/permits/issues/6
[#7]: https://github.com/DenisCarriere/permits/issues/7
[#8]: https://github.com/DenisCarriere/permits/issues/8
[#9]: https://github.com/DenisCarriere/permits/issues/9
[#10]: https://github.com/DenisCarriere/permits/issues/10
[#11]: https://github.com/DenisCarriere/permits/issues/11
[#12]: https://github.com/DenisCarriere/permits/issues/12
[#13]: https://github.com/DenisCarriere/permits/issues/13
[#14]: https://github.com/DenisCarriere/permits/issues/14
[#15]: https://github.com/DenisCarriere/permits/issues/15
[#16]: https://github.com/DenisCarriere/permits/issues/16
[#17]: https://github.com/DenisCarriere/permits/issues/17
[#18]: https://github.com/DenisCarriere/permits/issues/18

[2011]: https://github.com/DenisCarriere/permits/tree/master/CSV/2011
[2012]: https://github.com/DenisCarriere/permits/tree/master/CSV/2012
[2013]: https://github.com/DenisCarriere/permits/tree/master/CSV/2013
[2014]: https://github.com/DenisCarriere/permits/tree/master/CSV/2014

[MongoDB]: https://github.com/DenisCarriere/permits/blob/master/MongoDB.md
[OpenRefine]: https://github.com/OpenRefine/OpenRefine/wiki
[LICENSE]: http://ottawa.ca/en/mobile-apps-and-open-data/terms-use#license
[Open Data Catalog]: http://data.ottawa.ca/en/dataset/construction-demolition-pool-enclosure-permits-monthly
