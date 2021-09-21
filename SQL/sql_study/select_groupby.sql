select if(do in ('서울특별시','경기도'), '수도권' , '지방' ), avg(budget_value) as 예산평균, sum(budget_value) as 예산합계 
from budget
group by if(do in ('서울특별시','경기도'), '수도권' , '지방' ); 

# group by 절에 단순 column 명이 아닌 함수를 이용할 경우 group by절에서 쓴 함수를 그대로 select절에서도 사용해야 한다. 

