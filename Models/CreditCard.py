from datetime import date
from dataclasses import dataclass

import Exceptions

MAX_ANNUAL_INTEREST = 100

@dataclass
class CreditCard:
    """
    Representa la entidad de una tarjeta de crédito.
    """
    card_number: str
    owner_id: str
    owner_name: str
    bank_name: str
    due_date: date
    franchise: str
    payment_day: int
    monthly_fee: float
    interest_rate: float

    def __init__(self, card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate):
        """
        Inicializa una instancia de Tarjeta de Crédito.
        """
        self.card_number: str = card_number
        self.owner_id: str = owner_id
        self.owner_name: str = owner_name
        self.bank_name: str = bank_name
        self.due_date: date = due_date
        self.franchise: str = franchise
        self.payment_day: int = payment_day
        self.monthly_fee: float = monthly_fee
        self.interest_rate: float = interest_rate
        self.ANNUAL_INTEREST = self.interest_rate * 12  # Tasa de interés anual
        self.interest_percentage = self.interest_rate / 100  # Tasa de interés como porcentaje

    def calc_monthly_payment(self, amount: float, installments: int) -> float:
        """
        Calcula el pago mensual para una cantidad dada y un número de cuotas.
        """
        if amount == 0:
            raise Exceptions.ZeroAmountError
        elif installments <= 0:
            raise Exceptions.NegativeNumberOfPaymentsError
        if self.interest_rate == 0:
            return amount / installments
        if installments == 1:
            return amount
        else:
            # Fórmula para calcular el pago mensual con interés compuesto
            return round((amount * self.interest_percentage)/(1 - (1 + self.interest_percentage)**(-installments)), 4)

    def calc_total_interest(self, amount: float, installments: int) -> float:
        """
        Calcula el interés total para una cantidad dada y un número de cuotas.
        """
        payment_value: float = self.calc_monthly_payment(amount, installments)
        total_interest: float = round((payment_value * installments) - amount, 2)
        return total_interest

    def calc_planned_saving(self, monthly_amount: float, total_amount: float) -> int:
        """
        Calcula el número de pagos necesarios para alcanzar una meta de ahorro.
        """
        total_interest: float = 0
        subtotal: float = 0
        payment_number: int = 0
        while subtotal < total_amount:
            payment_number += 1
            subtotal += round(monthly_amount + total_interest, 4)
            total_interest = round(self.interest_percentage * subtotal, 4)
            if subtotal >= total_amount:
                return payment_number
