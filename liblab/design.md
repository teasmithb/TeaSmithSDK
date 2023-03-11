I created main.py with flask framework to provide api specification for 
movie GET
movie/{id} GET
movie/{quote} GET


using localhost:5000/the-one-api.dev/v2, developer can view specification for each API call

openapi.json file is also located under static folder



movies_api.py is written in python that takes arguments in order to call api for all movies, specific movie or calculate quote for a specific movie


If quote argument is present but not id, error is returned

if id is not present all movies are returned, using requests library and movie GET API call
if id is present specific movie is returned, using requests library and movie/{id} GET API call


unittest script is in tests folder that runs tests for movies_api.py using subprocess and unittest library
