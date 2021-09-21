select *,ifnull(korean,'정보없음!') from exam_test;

select *,if(math >= 80,'이과 고려','문과 고려'),if(korean is null,'정보 없습니다',korean) from exam_test;