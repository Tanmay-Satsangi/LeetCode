# Write your MySQL query statement below

-- Select p2 because it has a greater id then p1 (check the below where query.)

delete p2
from Person p1
join Person p2
on p1.email = p2.email
where p2.id > p1.id
