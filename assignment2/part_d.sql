select count(*)
from (select docid
  from frequency
  where term = "law" or term = "legal"
  group by docid);