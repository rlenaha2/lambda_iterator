import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    index=event['iterator']['index']
    step=event['iterator']['step']
    count=event['iterator']['count']

    logger.info(f'Entering step {step}')

    index += step

    if index<count:
        continuance=True
    else:
        continuance=False

    response = {'index':index, 'step':step, 'count':count,
                'continuance':continuance}

    return response

