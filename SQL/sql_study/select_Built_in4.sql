select *,ifnull(korean,'정보없음!') from exam_test;

select *,if(math >= 80,'이과 고려','문과 고려'),if(korean is null,'정보 없습니다',korean) from exam_test;

select name 
	, case 	when english = 76 then '영어 D반'
			when english = 82 then '영어 C반'
            when english = 90 then '영어 B반'
            when english = 95 then '영어 A반' end as english
	, english
    , korean
    from exam_test;