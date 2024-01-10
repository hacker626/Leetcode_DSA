# Write your MySQL query statement below
select e.name,b.bonus from Employee e left join Bonus b ON e.empId = b.empId where bonus is NULL or bonus<1000;
