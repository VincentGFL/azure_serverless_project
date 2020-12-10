import azure.functions as func
import random

def main(req: func.HttpRequest) -> func.HttpRequest:
    for i in range(4):
        num += randint(0,9)
        return num