select count(*)
from (select count(count) as term_count
  from frequency
  group by docid)
where term_count > 300;