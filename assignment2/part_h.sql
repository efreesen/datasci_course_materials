select sum(doc1.count * doc2.count) as count
from (select * from frequency where docid = '10080_txt_crude') doc1
join frequency doc2 on doc1.term = doc2.term and doc2.docid = '17035_txt_earn'
group by doc1.docid;