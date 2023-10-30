import unittest
from datetime import date

import Exceptions
from Models.CreditCard import CreditCard
from Controllers import ControllerCreditCard
from Tests import testControllerCreditCards


class TestPayment(unittest.TestCase):
    """
    Conjunto de pruebas para el sistema de pagos con tarjetas de crédito.
    """

    @classmethod
    def setUpClass(cls):
        """
        Configuración inicial de las pruebas.
        """
        print("Invoking setUpClass")
        ControllerCreditCard.create_table()
        tests_credit_cards = testControllerCreditCards.TestControllerCreditCard()
        tests_credit_cards.test_1()
        tests_credit_cards.test_2()
        tests_credit_cards.test_3()
        tests_credit_cards.test_4()
        tests_credit_cards.test_5()

    @classmethod
    def tearDownClass(cls):
        """
        Limpieza después de las pruebas.
        """
        print("Invoking tearDownClass")
        ControllerCreditCard.delete_all_rows()


    def test_normal_case_entrances(self):
        """
        Prueba de compra con tarjeta de crédito: Monto de $200,000 en 36 cuotas.
        """
        amount: float = 200000
        card_number: str = "556677"
        installments: int = 36

        searched_card = ControllerCreditCard.search_by_card_id(card_number)

        credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
                                 searched_card.bank_name, searched_card.due_date, searched_card.franchise,
                                 searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)
        result_monthly_payment = credit_card.calc_monthly_payment(amount, installments)
        result_total_interest = credit_card.calc_total_interest(amount, installments)
        expected_monthly_payment_output: float = 9297.9591
        expected_total_interest: float = 134726.53
        self.assertEqual(result_total_interest, expected_total_interest)
        self.assertEqual(result_monthly_payment, expected_monthly_payment_output)


    def test_normal_case_entrances_2(self):
        """
        Prueba de compra con tarjeta de crédito: Monto de $850,000 en 24 cuotas.
        """
        amount: float = 850000
        card_number: str = "223344"
        installments: int = 24

        searched_card = ControllerCreditCard.search_by_card_id(card_number)

        credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
                                 searched_card.bank_name, searched_card.due_date, searched_card.franchise,
                                 searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)
        result_monthly_payment = credit_card.calc_monthly_payment(amount, installments)
        result_total_interest = credit_card.calc_total_interest(amount, installments)
        expected_monthly_payment_output: float = 52377.4986
        expected_total_interest: float = 407059.97
        self.assertEqual(result_total_interest, expected_total_interest)
        self.assertEqual(result_monthly_payment, expected_monthly_payment_output)


    def test_interest_zero(self):
        """
        Prueba de compra con tarjeta de crédito: Monto de $480,000 en 48 cuotas.
        """
        amount: float = 480000
        card_number: str = "445566"
        installments: int = 48

        searched_card = ControllerCreditCard.search_by_card_id(card_number)

        credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
                                 searched_card.bank_name, searched_card.due_date, searched_card.franchise,
                                 searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)
        result_monthly_payment = credit_card.calc_monthly_payment(amount, installments)
        result_total_interest = credit_card.calc_total_interest(amount, installments)
        expected_monthly_payment_output: float = 10000
        expected_total_interest: float = 0
        self.assertEqual(result_total_interest, expected_total_interest)
        self.assertEqual(result_monthly_payment, expected_monthly_payment_output)


    def test_single_fee_entrances(self):
        """
        Prueba de compra con tarjeta de crédito: Monto de $90,000 en 1 cuota.
        """
        amount: float = 90000
        card_number: str = "445566"
        installments: int = 1

        searched_card = ControllerCreditCard.search_by_card_id(card_number)

        credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
                                 searched_card.bank_name, searched_card.due_date, searched_card.franchise,
                                 searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)
        result_monthly_payment = credit_card.calc_monthly_payment(amount, installments)
        result_total_interest = credit_card.calc_total_interest(amount, installments)
        expected_monthly_payment_output: float = 90000
        expected_total_interest: float = 0
        self.assertEqual(result_total_interest, expected_total_interest)
        self.assertEqual(result_monthly_payment, expected_monthly_payment_output)


    def test_buy_error_entrances(self):
        """
        Prueba de compra con tarjeta de crédito: Monto de $0 en 60 cuotas.
        """
        amount: float = 0
        card_number: str = "223344"
        installments: int = 60

        searched_card = ControllerCreditCard.search_by_card_id(card_number)

        credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
                                 searched_card.bank_name, searched_card.due_date, searched_card.franchise,
                                 searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)

        self.assertRaises(Exceptions.ZeroAmountError, credit_card.calc_monthly_payment, amount, installments)

    def test_negative_error_entrances(self):
        """
        Prueba de compra con tarjeta de crédito: Monto de $50,000 en -10 cuotas.
        """
        amount: float = 50000
        card_number: str = "556677"
        installments: int = -10

        searched_card = ControllerCreditCard.search_by_card_id(card_number)

        credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
                                 searched_card.bank_name, searched_card.due_date, searched_card.franchise,
                                 searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)

        self.assertRaises(Exceptions.NegativeNumberOfPaymentsError, credit_card.calc_monthly_payment, amount, installments)

    def test_credit_card_dont_exist(self):
        """
        Prueba de compra con tarjeta de crédito: Tarjeta no encontrada.
        """
        amount: float = 50000
        card_number: str = "885522"
        installments: int = 10

        self.assertRaises(Exceptions.CardNotFoundError, ControllerCreditCard.search_by_card_id, card_number)


if __name__ == '__main__':
    unittest.main()
