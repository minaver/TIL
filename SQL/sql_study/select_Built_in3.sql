# select now(),sysdate(),current_timestamp(),curdate(),current_date(),current_time(),now(),current_time()+0,now()+0;

# select dayofweek('2021-09-21 23:23:23');

select date_add('2021-09-21 23:23:23', interval 1 second),
date_add('2021-09-21 23:23:23', interval 31 day ),
date_add('2021-09-21 23:23:23', interval '1:1' minute_second),
date_add('2021-09-21 23:23:23', interval '-2 15' day_hour);
