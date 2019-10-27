import json


def lambda_handler(event, context):

    index=event['iterator']['index']
    step=event['iterator']['step']
    count=event['iterator']['count']

    index += step

    if index<count:
        continuance=True
    else:
        continuance=False

    response = {'index':index, 'step':step, 'count':count,
                'continuance':continuance}

    return response

