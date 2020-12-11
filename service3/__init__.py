import azure.functions as func
import random
import string

def main(req: func.HttpRequest) -> func.HttpRequest:
    logging.info('Python HTTP trigger function processed a request.')
    for i in range(4):
        letter = ''.join(random.choice(string.ascii_lowercase))
        
    logging.info(letter)
    return func.HttpResponse(
        letter,
        status_code=200
    )