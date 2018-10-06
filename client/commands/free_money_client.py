from plug.key import ED25519SigningKey
from plug.hash import sha256
from plug.proof import SingleKeyProof
from free_money.transform import FreeMoney
from plug.transaction import Transaction
from plug.constant import TransactionEvent
from plug.message import Event
from plug.registry import Registry
from client.utils import register_transform_event
from client.user import User
import aiohttp
import json
import asyncio
from asyncio import get_event_loop

def init_free_money(client, user_input_key, amount):
    register_transform_event(FreeMoney)

    transform = FreeMoney(
        user=user_input_key,
        amount=int(amount),
    )

    loop = get_event_loop()

    response = loop.run_until_complete(client.broadcast_transform(transform))

    print(response)
    return response

    # challenge = transform.hash(sha256)
    # proof = SingleKeyProof(receiver.address, receiver.nonce, challenge, 'challenge.FreeMoney')
    # proof.sign(receiver.receiver_input_key)
    # transaction = Transaction(transform, {proof.address: proof})

    # event = Event(
    #     event=TransactionEvent.ADD,
    #     payload=transaction,
    # )

    # payload = registry.pack(event)

    # async with aiohttp.ClientSession() as session:
    #     async with session.post("http://localhost:8081/_api/v1/transaction", json=payload) as response:
    #         data = await response.json()
    #         print(data)

    
