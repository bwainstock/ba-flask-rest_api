BeerAdvocate Flask REST API
===========================

A basic REST API for bar information scraped from BeerAdvocate.

__/bars/__
GET - Retrieve a sample set of 10 bars

__/bars/{STATE}/__
GET - Retrieve all bars from STATE

__/bars/{STATE}/{CITY}/__
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
Requirements
------------
- Flask==0.10.1
- Flask-SQLAlchemy==2.0
- Jinja2==2.7.3
- MarkupSafe==0.23
- SQLAlchemy==0.9.8
- Werkzeug==0.9.6
- argparse==1.2.1
- gunicorn==19.1.1
- itsdangerous==0.24
- wsgiref==0.1.2
