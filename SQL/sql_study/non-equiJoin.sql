select c.name as 고객명, c.point as 고객_포인트, g.name as 상품
from class.customer c join class.gift g 
on c.point between g.point_s and g.point_e;