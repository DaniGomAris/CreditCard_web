from datetime import date

from flask import Flask, request, jsonify, render_template
from Controllers import ControllerCreditCard, ControllerPaymentPlan
from Models.CreditCard import CreditCard


view = Flask(__name__)


# Ventana main(Menu)
@view.route("/")
def home():
    """
    Renderiza la página principal (index.html)
    """
    return render_template("index.html")


# http://127.0.0.1:5000/view/create_credit_card
# Ventana para insertar nueva tarjeta de credito
@view.route("/view/create_credit_card")
def view_new_credit_card():
    """
    Renderiza la página para insertar una nueva tarjeta de crédito (create_credit_card.html)
    """
    return render_template("create_credit_card.html")


# http://127.0.0.1:5000/view/simulate_purchase
# Ventana para simular una compra
@view.route("/view/simulate_purchase")
def view_simulate_purchase():
    """
    Renderiza la página para simular una compra (simulate_purchase.html)
    """
    return render_template("simulate_purchase.html")


# http://127.0.0.1:5000/view/payment_plan
# Ventana para simular un plan de pago
@view.route("/view/payment_plan")
def view_payment_plan():
    """
    Renderiza la página para simular un plan de pago (payment_plan.html)
    """
    return render_template("payment_plan.html")


# http://127.0.0.1:5000/view/view_payments
# Ventana para obtener el pago en un rango de meses especifico
@view.route("/view/view_payments")
def view_payments():
    """
    Renderiza la página para obtener el pago en un rango de meses específico (view_payments.html)
    """
    return render_template("view_payments.html")


# http://127.0.0.1:5000/view/insert/credit_card
# Insertar nueva tarjeta de credito en la base de datos
@view.route('/view/insert/credit_card')
def view_insert_credit_card():
    """
    Inserta una nueva tarjeta de crédito en la base de datos
    """
    try:
        card_number = request.args["card_number"]
        owner_id = request.args["owner_id"]
        owner_name = request.args["owner_name"]
        bank_name = request.args["bank_name"]
        due_date = date.fromisoformat(request.args["due_date"])
        franchise = request.args["franchise"]
        payment_day = int(request.args["payment_day"])
        monthly_fee = float(request.args["monthly_fee"])
        interest_rate = float(request.args["interest_rate"])

        credit_card = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day,
                                 monthly_fee, interest_rate)

        ControllerCreditCard.insert_credit_card(credit_card)

        search_credit_card = ControllerCreditCard.search_by_card_id(card_number)

        result: str = f"Tarjeta de credito {search_credit_card.card_number} guardada exitosamente!"
        return result
    except Exception as err:
        return str(err)


# http://127.0.0.1:5000/view/simulate/purchase
# Simula una compra y muestra la cuota mensual, el interés total y el ahorro planificado sugerido.
@view.route('/view/simulate/purchase')
def view_show_purchase():
    """
    Simula una compra y muestra la cuota mensual, el interés total y el ahorro planificado sugerido
    """
    try:
        card_number = request.args["card_number"]
        purchase_amount = float(request.args["purchase_amount"])
        payments = int(request.args["payments"])

        search_credit_card = ControllerCreditCard.search_by_card_id(card_number)

        monthly_amount = CreditCard.calc_monthly_payment(search_credit_card, purchase_amount, payments)
        total_interest = CreditCard.calc_total_interest(search_credit_card, purchase_amount, payments)

        planned_saving = CreditCard.calc_planned_saving(search_credit_card, monthly_amount, purchase_amount)

        result: str = f"""
        Pago mensual: ${monthly_amount}... \n
        Interes total de pago: ${total_interest}... \n

        Te sugerimos que ahorres por {planned_saving} meses para realizar la compra de contado
        """

        return result

    except Exception as err:
        return str(err)


# http://127.0.0.1:5000/view/insert/payment_plan
# Inserta un plan de pago en la base de datos
@view.route('/view/insert/payment_plan')
def insert_payment_plan():
    """
    Inserta un plan de pago en la base de datos
    """
    try:
        card_number = request.args["card_number"]
        purchase_amount = float(request.args["purchase_amount"])
        purchase_date = date.fromisoformat(request.args["purchase_date"])
        payments = int(request.args["payments"])

        ControllerPaymentPlan.insert_payment_plan(card_number, purchase_amount, purchase_date, payments)

        result: str = "Plan de amortización guardado exitosamente en la base de datos."

        return result

    except Exception as err:
        return str(err)


# http://127.0.0.1:5000/view/calc/payments
# Muestra el pago total pendiente en un intervalo determinado de meses
@view.route("/view/calc/payments")
def calc_payments():
    """
    Muestra el pago total pendiente en un intervalo determinado de meses
    """
    try:
        inintial_date = request.args["initial_date"]
        final_date = request.args["final_date"]

        total = ControllerPaymentPlan.calc_total_payment_in_x_interval(date.fromisoformat(inintial_date),
                                                                       date.fromisoformat(final_date))

        result: str = f"El total a pagar desde {inintial_date} hasta {final_date} es: ${total}"

        return result

    except Exception as err:
        return str(err)


if __name__ == '__main__':
    view.run(debug=True)