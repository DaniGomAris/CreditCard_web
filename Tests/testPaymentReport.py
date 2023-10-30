import unittest
from datetime import date

from Controllers import ControllerPaymentPlan
from Controllers import ControllerCreditCard
from Tests import testControllerCreditCards
from testPaymentPlan import ControllerPaymentPlanTest


class TestPaymentReport(unittest.TestCase):
    """
    Clase de prueba para el reporte de pagos
    """

    def setUp(self):
        """
        Configuración previa a cada prueba
        """
        # Plan de pagos 1
        card_number: str = "556677"
        purchase_date: date = date.fromisoformat("2023-09-22")
        amount: float = 200000
        installments: int = 36
        payment_plan = ControllerPaymentPlan.insert_payment_plan(card_number, amount, purchase_date, installments)

        # Plan de pagos 2
        card_number: str = "223344"
        purchase_date: date = date.fromisoformat("2023-09-25")
        amount: float = 850000
        installments: int = 24
        payment_plan = ControllerPaymentPlan.insert_payment_plan(card_number, amount, purchase_date, installments)

        # Plan de pagos 3
        card_number: str = "445566"
        purchase_date: date = date.fromisoformat("2023-09-29")
        amount: float = 480000
        installments: int = 48
        payment_plan = ControllerPaymentPlan.insert_payment_plan(card_number, amount, purchase_date, installments)

        # Pago único
        card_number: str = "445566"
        purchase_date: date = date.fromisoformat("2023-11-17")
        amount: float = 90000
        installments: int = 1
        payment_plan = ControllerPaymentPlan.insert_payment_plan(card_number, amount, purchase_date, installments)


    @classmethod
    def setUpClass(cls):
        """
        Configuración inicial para todas las pruebas
        """
        print("Invocando setUpClass")
        ControllerPaymentPlan.create_table()
        ControllerCreditCard.delete_all_rows()
        print("Invocando setUpClass")
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
        Limpieza después de todas las pruebas
        """
        print("Invocando tearDownClass")
        ControllerCreditCard.delete_all_rows()
        ControllerPaymentPlan.delete_all_rows()


    def test_payment_report_1(self):
        """
        Prueba del reporte de pagos para octubre de 2023
        """
        initial_date: date = date.fromisoformat("2023-10-01")
        final_date: date = date.fromisoformat("2023-10-31")

        total: float = ControllerPaymentPlan.calc_total_payment_in_x_interval(initial_date, final_date)
        expected: float = 71675
        ControllerPaymentPlan.delete_all_rows()

        self.assertEqual(total, expected)


    def test_payment_report_2(self):
        """
        Prueba del reporte de pagos para el cuarto trimestre de 2023
        """
        initial_date: date = date.fromisoformat("2023-10-01")
        final_date: date = date.fromisoformat("2023-12-31")

        total: float = ControllerPaymentPlan.calc_total_payment_in_x_interval(initial_date, final_date)
        expected: float = 305026
        ControllerPaymentPlan.delete_all_rows()

        self.assertEqual(total, expected)


    def test_payment_report_3(self):
        """
        Prueba del reporte de pagos para el año 2026
        """
        initial_date: date = date.fromisoformat("2026-01-01")
        final_date: date = date.fromisoformat("2026-12-31")

        total: float = ControllerPaymentPlan.calc_total_payment_in_x_interval(initial_date, final_date)
        expected: float = 203682
        ControllerPaymentPlan.delete_all_rows()

        self.assertEqual(total, expected)
