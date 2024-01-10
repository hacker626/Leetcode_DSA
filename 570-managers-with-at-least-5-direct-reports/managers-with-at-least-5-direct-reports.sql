# # Write your MySQL query statement below

# select e1.name from Employee e1 join Employee e2 on e1.managerId = e2.id group by e1.managerId having count(e1.id)>=5 ;



# Write your MySQL query statement below
Select m.name
from employee as e
inner join employee as m
on e.managerId=m.id
group by e.managerId 
having count(e.id)>=5
# ```please upvote to motivate me write more solution
