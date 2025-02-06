# Write your MySQL query statement below

-- We usually use group by with an aggregate function like :COUNT, SUM, AVG, MAX or MIN etc..

select customer_id, count(customer_id) as count_no_trans
from Visits v
left join Transactions t
on v.visit_id = t.visit_id
where transaction_id is null
group by customer_id
