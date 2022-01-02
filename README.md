# How to run the app

To run the app locally:
- pip3 install -r requirements.txt
- python3 main.py

To run the app with docker:
- docker build -t power-generation-statistics-app
- docker run -p 5000:5000 power-generation-statistics-app



-------------------------------


# Services

The app is deployed on Heroku under the domain name: power-generation-statistics.herokuapp.com

- Return the top N plants in terms of annual net generation
```
    method: GET
    endpoint: https://power-generation-statistics.herokuapp.com/top_annual_generation_plants?limit=<N value>
    body: {}
    headers: {}
```
- Get absolute value and percentage of the annual net generation by federal state
```
    method: GET
    endpoint: https://power-generation-statistics.herokuapp.com/get_annual_net_generation_by_state
    body: {}
    headers: {}
```
- Get absolute value and percentage of the annual net generation of a certain state
```
    method: GET
    endpoint: https://power-generation-statistics.herokuapp.com/get_annual_net_generation_by_state?state=<state>
    body: {}
    headers: {}
```
