-- Declaración CREATE TABLE para la tabla 'payment_plans'

CREATE TABLE payment_plans (
    Number INTEGER NOT NULL, -- Número único de identificación para el plan de pagos
    card_number VARCHAR(20) NOT NULL, -- Número de tarjeta de crédito asociada al plan de pagos
    purchase_date DATE, -- Fecha de compra asociada al plan de pagos
    purchase_amount FLOAT, -- Monto de la compra asociada al plan de pagos
    payment_date DATE, -- Fecha de pago asociada al plan de pagos
    payment_amount FLOAT, -- Monto del pago realizado en el plan de pagos
    interest_amount FLOAT, -- Monto de intereses calculados en el plan de pagos
    capital_amount FLOAT, -- Monto de capital pagado en el plan de pagos
    balance FLOAT -- Saldo restante en el plan de pagos
);