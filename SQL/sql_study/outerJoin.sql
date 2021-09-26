select s.name, s.bl_prfs_id, p.name, p.prfs_id
from class.professor p right outer join class.student s
on s.bl_prfs_id = p.prfs_id;