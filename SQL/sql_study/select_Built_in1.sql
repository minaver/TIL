# 다양한 select 내장 문자 함수들
select 
country_name as 국가, 
upper(country_name) as 대문자변환, 
length(country_name) as 나라이름길이, 
mid(country_name,1,3) as 부분추출 ,
instr(country_name,'A') as A의위치 ,
lpad(country_name,10,'_') as 자리수채우기 ,
replace(country_name, 'a' ,'@') as 치환,
concat(country_name,'의 수도는 ',capital_city,'입니다') as 수도소개
from country;