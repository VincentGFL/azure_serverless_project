import logging
import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numbers = requests.get('http://localhost:7071/api/service2')
    letters = requests.get('http://localhost:7071/api/service3')

    numletter = numbers.text + letters.text
    logging.info(numbers.text)
    logging.info(letters.text)

    return func.HttpResponse(
        numletter,
        status_code=200
    )
