select s.name as 학생명, m.major_title as 원전공, p.bl_major_id as 전공코드, p.name as 교수명 
from class.student s 
	inner join class.professor p
    inner join class.major m
		on p.bl_major_id = m.major_id
			and s.bl_prfs_id = prfs_id;