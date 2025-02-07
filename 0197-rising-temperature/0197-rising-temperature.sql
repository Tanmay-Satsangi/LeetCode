# Write your MySQL query statement below

-- self join 

select w2.id 
from Weather w1
join Weather w2
on DateDiff(w2.recordDate, w1.recordDate) = 1 
where w2.temperature > w1.temperature
