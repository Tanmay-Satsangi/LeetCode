# Write your MySQL query statement below

-- https://www.youtube.com/watch?v=Cm3Phvdjnuk

select * 
from Patients
where conditions LIKE "DIAB1%" or conditions LIKE "% DIAB1%"
