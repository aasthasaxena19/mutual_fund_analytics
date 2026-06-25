SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

SELECT
strftime('%Y-%m',date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

SELECT *
FROM monthly_sip_inflows;

SELECT
state,
SUM(amount)
FROM fact_transactions
GROUP BY state;

SELECT *
FROM dim_fund
WHERE expense_ratio <1;