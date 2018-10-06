from dataclasses import dataclass
from plug.abstract import Transform

from free_money.model import BalanceModel

import free_money.error
import free_money.model

@dataclass
class BalanceTransfer(Transform):
    fqdn = "tutorial.BalanceTransfer"
    sender: str
    receiver: str
    amount: int

    def required_authorizations(self):
        print("place_holder!")

    @staticmethod
    def required_models():
        print("place_holder!")

    def required_keys(self):
        print("place_holder!")

    @staticmethod
    def pack(registry, obj):
        print("place_holder!")

    @classmethod
    def unpack(cls, registry, payload):
        print("place_holder!")

    def verify(self, state_slice):
        print("place_holder!")

    def apply(self, state_slice):
        print("place_holder!")

@dataclass
class FreeMoney(Transform):
    fqdn = "tutorial.FreeMoney"
    user: str
    amount: int

    def required_authorizations(self):
        return {self.user}

    @staticmethod
    def required_models():
        return {BalanceModel.fqdn}

    def required_keys(self):
        return {self.user}

    @staticmethod
    def pack(registry, obj):
        return {
            "user": obj.user,
            "amount": obj.amount,
        }

    @classmethod
    def unpack(cls, registry, payload):
        return cls(
            user=payload["user"],
            amount=payload["amount"],
        )

    def verify(self, state_slice):
        balances = state_slice[BalanceModel.fqdn]
      
        if self.amount <= 0:
            raise free_money.error.InvalidAmountError("amount should be greater than 0")
        
        userBalance = balances[self.user].balance
        if self.amount > userBalance:
            raise free_money.error.NotEnoughMoneyError("you will be broke if you send this amount")

    def apply(self, state_slice):
        balances = state_slice[BalanceModel.fqdn]
        balances[self.user].balance += self.amount
