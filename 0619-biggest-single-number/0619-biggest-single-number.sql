# Write your MySQL query statement below

-- here aliasing is compulsory otherwise it gives the error: "every derived table must have its own alias"

-- Reason of Error: This error occurs when you use a subquery (derived table) inside a FROM clause without assigning it an alias.

-- https://stackoverflow.com/questions/1888779/what-is-the-error-every-derived-table-must-have-its-own-alias-in-mysql

select max(num) as num from (select num
from MyNumbers
group by num
having count(num) = 1) as group_table
