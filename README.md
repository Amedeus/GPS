# GPS

A command line tool to find informations with gps coordinates

This tool work with nominatim.openstreetmap.org.

## Installation

you need python3 and some common libraries

To add gps.py in the path :
```bash
$ chmod +x install.sh
$ ./install.sh
```
To update :
```bash
$ ./update 
```
(Make sure this file is executable, else : chmod +x update.sh)

## Usage
```bash
$ gps -h
$ gps [latitude] [longitude]
```


## Exemple

You find coordinates with exif for exemple and need more informations.

```bash
$ gps "N50°05'16''" "E14°25'14''"
type DMS->DD conversion
N50°05'16''
|->50.08777777777777777
type DMS->DD conversion
E14°25'14''
|->14.42055555555555557
address29 : Old Town Square
pedestrian : Staroměstské náměstí
suburb : Old Town
city : Prague
county : okres Hlavní město Praha
state : Prague
postcode : 110000
country : Czechia
country_code : cz
```

Note : 
 - longitude and latitude are strings, you need escape quotes (N50°05\'16\'\') or double quote like above.
 - It is DMS (degrees-minutes-seconds) notation but you can pass DD values

```bash
$ gps 38.899101696937265 -77.03782367970734

artwork : Major General Rochambeau
pedestrian : Pennsylvania Avenue Northwest
neighbourhood : Golden Triangle
city : Washington
state : District of Columbia
postcode : 20006
country : USA
country_code : us
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

