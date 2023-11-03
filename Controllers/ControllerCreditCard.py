import sys
import psycopg2
from datetime import date

import SecretConfig
import Exceptions
from Models.CreditCard import CreditCard


def get_cursor():
    """
    Establece la conexión a la base de datos y devuelve un cursor para realizar operaciones
    """
    DATABASE = SecretConfig.DATABASE
    USER = SecretConfig.USER
    PASSWORD = SecretConfig.PASSWORD
    HOST = SecretConfig.HOST
    PORT = SecretConfig.PORT
    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    return connection.cursor()


def create_table():
    """
    Crea la tabla en la base de datos según la definición en el archivo SQL correspondiente
    """
    sql = ""
    with open("../sql/create_credit_card.sql", "r") as f:
        sql = f.read()

    cursor = get_cursor()

    try:
        # Intenta ejecutar la creación de la tabla en la base de datos
        cursor.execute(sql)
        cursor.connection.commit()
        print("Table created successfully")
    except Exception as err:
        # La tabla ya existe
        print(err)
        cursor.connection.rollback()


def delete_table():
    """
    Elimina la tabla y todos sus datos de la base de datos
    """
    sql = "DROP TABLE credit_cards;"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()


def delete_all_rows():
    """
    Elimina todas las filas de la tabla en la base de datos
    """
    sql = "DELETE FROM credit_cards"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()


def delete_single_credit_card(credit_card):
    """
    Elimina una tarjeta de crédito específica de la base de datos
    """
    sql = f"DELETE FROM credit_cards WHERE card_number = '{credit_card.card_number}'"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()


def insert_credit_card(credit_card: CreditCard):
    """
    Inserta una nueva tarjeta de crédito en la base de datos
    """
    cursor = get_cursor()

    try:
        # Busca la tarjeta de crédito por su número
        card_number_search = search_by_card_id(credit_card.card_number)

        # Si la tarjeta ya existe, lanza una excepción
        if card_number_search is not None and card_number_search.card_number == credit_card.card_number:
            raise Exceptions.CreditCardAlreadyExists(f"The credit card {card_number_search.card_number} already exists")

    except Exceptions.CardNotFoundError:
        pass

    try:
        # Inserta la nueva tarjeta de crédito en la base de datos
        cursor.execute(f"""
                INSERT INTO credit_cards (
                    card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate
                )
                VALUES
                (
                    '{credit_card.card_number}', '{credit_card.owner_id}', '{credit_card.owner_name}', 
                    '{credit_card.bank_name}', '{credit_card.due_date}', '{credit_card.franchise}', {credit_card.payment_day},
                    '{credit_card.monthly_fee}', '{credit_card.interest_rate}'
                );
                                """)

        cursor.connection.commit()
        print("Credit card saved successfully")
    except Exception as err:
        print(err)
        cursor.connection.rollback()


def search_by_card_id(card_number):
    """
    Busca una tarjeta de crédito por su número en la base de datos
    """
    cursor = get_cursor()
    cursor.execute(f"""SELECT card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, 
    monthly_fee, interest_rate FROM credit_cards where card_number = '{card_number}'""")
    row = cursor.fetchone()

    if row is None:
        raise Exceptions.CardNotFoundError(f"Could not find the credit card {card_number}")

    result = CreditCard(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    return result