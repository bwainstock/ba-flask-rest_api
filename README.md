BeerAdvocate Flask REST API
===========================

A basic REST API for bar information scraped from BeerAdvocate.

__/bars/__
GET - Retrieve a sample set of 10 bars

__/bars/{STATE ABBREVIATION}/__
GET - Retrieve all bars from STATE

__/bars/{STATE ABBREVIATION}/{CITY}/__
GET - Retrieve all bars from CITY, STATE

__/bar/{ID}__
GET - Retrieve information for single bar ID

Sample Output
-------------

```
{
  "items": {
    "address": "701 W Lake St", 
    "categories": "Bar,Eatery", 
    "city": "Addison", 
    "lat": 41.94008, 
    "lon": -88.007191, 
    "name": "American Tap", 
    "rating": 3.5, 
    "state": "IL"
  }
}
```
