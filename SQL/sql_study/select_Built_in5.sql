
select count(ifnull(korean,0)),
sum(korean),
avg(korean),avg(ifnull(korean,0)),
max(korean),min(korean),
stddev(korean),
variance(korean)
from exam_test;