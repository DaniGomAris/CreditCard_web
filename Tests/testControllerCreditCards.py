import unittest
from datetime import date

import Exceptions
from Models.CreditCard import CreditCard
from Controllers import ControllerCreditCard


class TestControllerCreditCard(unittest.TestCase):
    """
    Conjunto de pruebas para el controlador de tarjetas de crédito
    """

    @classmethod
    def setUpClass(cls):
        """
        Configuración inicial de las pruebas
        """
        print("Invoking setUpClass")
        ControllerCreditCard.create_table()

    @classmethod
    def tearDownClass(cls):
        """
        Limpieza después de las pruebas
        """
        print("Invoking tearDownClass")
        ControllerCreditCard.delete_all_rows()

    def test_1(self):
        """
        Prueba de inserción de una tarjeta de crédito en la base de datos
        """
        card_number: str = "556677"
        owner_id: str = "1010123456"
        owner_name: str = "comprador compulsivo"
        bank_name: str = "Bancolombia"
        due_date: date = date.fromisoformat("2027-12-31")
        franchise: str = "VISA"
        payment_day: int = 10
        monthly_fee: float = 24000
        interest_rate: float = 3.1

        credit_card_test = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate)

        ControllerCreditCard.insert_credit_card(credit_card_test)

        searched_credit_card = ControllerCreditCard.search_by_card_id(credit_card_test.card_number)

        self.assertEqual(credit_card_test.card_number, searched_credit_card.card_number)
        self.assertEqual(credit_card_test.owner_id, searched_credit_card.owner_id)
        self.assertEqual(credit_card_test.owner_name, searched_credit_card.owner_name)
        self.assertEqual(credit_card_test.bank_name, searched_credit_card.bank_name)
        self.assertEqual(credit_card_test.due_date, searched_credit_card.due_date)
        self.assertEqual(credit_card_test.franchise, searched_credit_card.franchise)
        self.assertEqual(credit_card_test.payment_day, searched_credit_card.payment_day)
        self.assertEqual(credit_card_test.monthly_fee, searched_credit_card.monthly_fee)
        self.assertEqual(credit_card_test.interest_rate, searched_credit_card.interest_rate)

    def test_2(self):
        """
        Prueba de inserción de otra tarjeta de crédito en la base de datos
        """
        card_number: str = "442233"
        owner_id: str = "1010123456"
        owner_name: str = "comprador compulsivo"
        bank_name: str = "Popular"
        due_date: date = date.fromisoformat("2022-12-31")
        franchise: str = "Mastercard"
        payment_day: int = 5
        monthly_fee: float = 34000
        interest_rate: float = 3.4

        credit_card_test = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate)

        ControllerCreditCard.insert_credit_card(credit_card_test)

        searched_credit_card = ControllerCreditCard.search_by_card_id(credit_card_test.card_number)

        self.assertEqual(credit_card_test.card_number, searched_credit_card.card_number)
        self.assertEqual(credit_card_test.owner_id, searched_credit_card.owner_id)
        self.assertEqual(credit_card_test.owner_name, searched_credit_card.owner_name)
        self.assertEqual(credit_card_test.bank_name, searched_credit_card.bank_name)
        self.assertEqual(credit_card_test.due_date, searched_credit_card.due_date)
        self.assertEqual(credit_card_test.franchise, searched_credit_card.franchise)
        self.assertEqual(credit_card_test.payment_day, searched_credit_card.payment_day)
        self.assertEqual(credit_card_test.monthly_fee, searched_credit_card.monthly_fee)
        self.assertEqual(credit_card_test.interest_rate, searched_credit_card.interest_rate)

    def test_3(self):
        """
        Prueba de inserción de una tarjeta de crédito duplicada
        """
        card_number: str = "556677"
        owner_id: str = "1020889955"
        owner_name: str = "Estudiante pelao"
        bank_name: str = "Bancolombia"
        due_date: date = date.fromisoformat("2027-12-31")
        franchise: str = "VISA"
        payment_day: int = 10
        monthly_fee: float = 24000
        interest_rate: float = 3.1

        credit_card_test = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate)

        self.assertRaises(Exceptions.CreditCardAlreadyExists, ControllerCreditCard.insert_credit_card, credit_card_test)

    def test_4(self):
        """
        Prueba de inserción de una tarjeta de crédito con tasa de interés cero
        """
        card_number: str = "223344"
        owner_id: str = "1010123456"
        owner_name: str = "comprador compulsivo"
        bank_name: str = "Falabella"
        due_date: date = date.fromisoformat("2025-12-31")
        franchise: str = "VISA"
        payment_day: int = 16
        monthly_fee: float = 0
        interest_rate: float = 3.4

        credit_card_test = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate)

        ControllerCreditCard.insert_credit_card(credit_card_test)

        searched_credit_card = ControllerCreditCard.search_by_card_id(credit_card_test.card_number)

        self.assertEqual(credit_card_test.card_number, searched_credit_card.card_number)
        self.assertEqual(credit_card_test.owner_id, searched_credit_card.owner_id)
        self.assertEqual(credit_card_test.owner_name, searched_credit_card.owner_name)
        self.assertEqual(credit_card_test.bank_name, searched_credit_card.bank_name)
        self.assertEqual(credit_card_test.due_date, searched_credit_card.due_date)
        self.assertEqual(credit_card_test.franchise, searched_credit_card.franchise)
        self.assertEqual(credit_card_test.payment_day, searched_credit_card.payment_day)
        self.assertEqual(credit_card_test.monthly_fee, searched_credit_card.monthly_fee)
        self.assertEqual(credit_card_test.interest_rate, searched_credit_card.interest_rate)

    def test_5(self):
        """
        Prueba de inserción de una tarjeta de crédito con tasa de interés cero
        """
        card_number: str = "445566"
        owner_id: str = "1010123456"
        owner_name: str = "comprador compulsivo"
        bank_name: str = "BBVA"
        due_date: date = date.fromisoformat("2027-12-31")
        franchise: str = "Mastercard"
        payment_day: int = 5
        monthly_fee: float = 34000
        interest_rate: float = 0

        credit_card_test = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate)

        ControllerCreditCard.insert_credit_card(credit_card_test)

        searched_credit_card = ControllerCreditCard.search_by_card_id(credit_card_test.card_number)

        self.assertEqual(credit_card_test.card_number, searched_credit_card.card_number)
        self.assertEqual(credit_card_test.owner_id, searched_credit_card.owner_id)
        self.assertEqual(credit_card_test.owner_name, searched_credit_card.owner_name)
        self.assertEqual(credit_card_test.bank_name, searched_credit_card.bank_name)
        self.assertEqual(credit_card_test.due_date, searched_credit_card.due_date)
        self.assertEqual(credit_card_test.franchise, searched_credit_card.franchise)
        self.assertEqual(credit_card_test.payment_day, searched_credit_card.payment_day)
        self.assertEqual(credit_card_test.monthly_fee, searched_credit_card.monthly_fee)
        self.assertEqual(credit_card_test.interest_rate, searched_credit_card.interest_rate)


if __name__ == '__main__':
    unittest.main()