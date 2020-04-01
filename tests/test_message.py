import uuid

from smtp4dev import Message


def test_message_deserializes_summary():
    msg_id = uuid.uuid4()
    payload = {
        "id": msg_id,
        "from": "romeo@montague.it",
        "to": "mercutio@montague.it, benvoilio@montague.it",
        "subject": "Saturday night drinks",
        "receivedDate": "1604-02-14T14:32:02.123456",
        "attachmentCount": 2,
        "isUnread": True,
    }
    msg = Message.deserialize(payload)

    assert msg.pk == msg_id
    assert msg.sender == payload["from"]
    assert msg.recipients == ("mercutio@montague.it", "benvoilio@montague.it")
    assert msg.subject == payload["subject"]
    assert msg.received_date.isoformat() == "1604-02-14T14:32:02+00:00"
    assert msg.attachment_count == payload["attachmentCount"]
    assert msg.is_unread


def test_message_deserializes_full():
    msg_id = uuid.uuid4()
    payload = {
        "id": msg_id,
        "from": "romeo@montague.it",
        "to": "mercutio@montague.it, benvoilio@montague.it",
        "subject": "Saturday night drinks",
        "receivedDate": "1604-02-14T14:32:02.123456",
        "parts": [{"isAttachment": True}, {"isAttachment": True}],
    }
    html = "<pre>Hey guys, meet Saturday for drinks!</pre>"
    msg = Message.deserialize(payload, html)

    assert msg.pk == msg_id
    assert msg.sender == payload["from"]
    assert msg.recipients == ("mercutio@montague.it", "benvoilio@montague.it")
    assert msg.subject == payload["subject"]
    assert msg.received_date.isoformat() == "1604-02-14T14:32:02+00:00"
    assert msg.attachment_count == 2
    assert msg.is_unread == False
    assert msg.body == html
