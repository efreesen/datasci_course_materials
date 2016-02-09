select count(*)
  from frequency as f
  join frequency as fw on fw.docid = f.docid
  where f.term = "transactions"
    and fw.term = "world";
