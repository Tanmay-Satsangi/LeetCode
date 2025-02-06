# Write your MySQL query statement below

select unique_id, name
from Employees emp 
left join EmployeeUNI empu
on emp.id = empu.id
