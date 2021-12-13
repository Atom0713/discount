import json
import os

from discount import sqs
from discount.common.constants import SQSTopicsConst


def get_webhook_queue_url_by_topic(topic: SQSTopicsConst):
    queue_topic_mapping: dict = {
        SQSTopicsConst.SHARE_USER_INFO: os.environ.get("")
    }

    return queue_topic_mapping.get(topic)


def send_message_to_sqs(topic: SQSTopicsConst, message_body: dict):
    sqs.send_message(
        QueueUrl=get_webhook_queue_url_by_topic(topic),
        DelaySeconds=10,
        MessageBody=json.dumps(message_body)
    )