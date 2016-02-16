create view search as
  SELECT 'q' as docid, 'washington' as term, 1 as count 
  UNION
  SELECT 'q' as docid, 'taxes' as term, 1 as count
  UNION 
  SELECT 'q' as docid, 'treasury' as term, 1 as count;

select frequency.docid, sum(search.count * frequency.count) as similarity
from search
join frequency on frequency.term = search.term
group by frequency.docid
order by similarity desc
limit 10;

drop view if exists search;