# ZipAirline_

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Requirements.

```bash
pip install -r requirement.txt
```

## Command to Run Server
```bash
python manage.py runserver
```
Go to this address http://127.0.0.1:8000/fuel-details

Sample json data (Payload) for the POST API 
```JSON
{
    "plane_id":[1,2,3,4,5,6,7,8,9],
    "passenger_no":[10,12,15,15,50,12,15,15,50]
}
```
Sample json Response of the POST API
```JSON
{
    
    "Total Fuel Consumption per min": 1.5754075753824441,
    "Total Fly Time": 5022.153170487487
}
```
## Command to Run Test
```bash
python manage.py test
```
