-- select now(),sysdate(),current_timestamp(),curdate(),current_date(),current_time(),now(),current_time()+0,now()+0;

-- select dayofweek('2021-09-23 11:47:48'),
-- weekday('2021-09-23 11:47:48'),
-- dayofmonth('2021-09-23 11:47:48'),
-- dayofyear('2021-09-23 11:47:48'),
-- month('2021-09-23 11:47:48'),
-- dayname('2021-09-23 11:47:48'),
-- monthname('2021-09-23 11:47:48'),
-- quarter('2021-09-23 11:47:48'),
-- week('2021-09-23 11:47:48'),
-- year('2021-09-23 11:47:48'),
-- hour('2021-09-23 11:47:48'),
-- minute('2021-09-23 11:47:48');

-- select date_add('2021-09-21 23:23:23', interval 1 second),
-- date_add('2021-09-21 23:23:23', interval 31 day ),
-- date_add('2021-09-21 23:23:23', interval '1:1' minute_second),
-- date_add('2021-09-21 23:23:23', interval '-2 15' day_hour);

-- select date_add('2021-09-23 11:47:48', interval 1 second),
-- adddate('2021-09-23 11:47:48', interval 1 second),
-- date_sub('2021-09-23 11:47:48', interval 1 second),
-- subdate('2021-09-23 11:47:48', interval 1 second);

select date_format(now(), '%Y-%m-%d-%W')












