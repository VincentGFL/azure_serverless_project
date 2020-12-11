import azure.functions as func
import random
import logging

def main(req: func.HttpRequest) -> func.HttpRequest:
    logging.info('Python HTTP trigger function processed a request.')
    for i in range(4):
        num += randint(0,9)
        
    logging.info(num)
    return func.HttpResponse(
        num,
        status_code=200
    )