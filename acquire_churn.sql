# Querry used to access Telco Churn data
SELECT *
FROM customers AS c
JOIN contract_types AS ct ON c.contract_type_id = ct.contract_type_id
JOIN payment_types AS pt ON c.payment_type_id = pt.payment_type_id
JOIN internet_service_types AS ist ON c.internet_service_type_id = ist.internet_service_type_id;