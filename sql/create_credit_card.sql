-- Declaración CREATE TABLE para la tabla 'credit_card'

CREATE TABLE credit_card (
    card_number VARCHAR(20) NOT NULL, -- Identificador único para la tarjeta de crédito
    owner_id VARCHAR(20) NOT NULL, -- Identificador para el propietario de la tarjeta de crédito
    owner_name VARCHAR(100) NOT NULL, -- Nombre del propietario de la tarjeta de crédito
    bank_name VARCHAR(100) NOT NULL, -- Nombre del banco asociado con la tarjeta de crédito
    due_date DATE NOT NULL, -- Fecha de vencimiento para los pagos asociados con la tarjeta de crédito
    franchise VARCHAR(15) NOT NULL, -- Franquicia o tipo de la tarjeta de crédito (por ejemplo, Visa, MasterCard)
    payment_day INTEGER, -- Día del mes en que vencen los pagos
    monthly_fee FLOAT, -- Cuota mensual cargada para la tarjeta de crédito
    interest_rate FLOAT -- Tasa de interés asociada con la tarjeta de crédito
);