select a.row_num, b.col_num, SUM(a.value * b.value) from (select *
  from (select * from a
    union select *
      from (select 0 as 'row_num', 0 as 'col_num', 0 as 'value'
        union select 0, 1, 0
        union select 0, 2, 0
        union select 0, 3, 0
        union select 0, 4, 0
        union select 1, 0, 0
        union select 1, 1, 0
        union select 1, 2, 0
        union select 1, 3, 0
        union select 1, 4, 0
        union select 2, 0, 0
        union select 2, 1, 0
        union select 2, 2, 0
        union select 2, 3, 0
        union select 2, 4, 0
        union select 3, 0, 0
        union select 3, 1, 0
        union select 3, 2, 0
        union select 3, 3, 0
        union select 3, 4, 0
        union select 4, 0, 0
        union select 4, 1, 0
        union select 4, 2, 0
        union select 4, 3, 0
        union select 4, 4, 0))
  group by row_num, col_num) as a,
  (select *
    from (select * from b
    union select *
      from (select 0 as 'row_num', 0 as 'col_num', 0 as 'value'
        union select 0, 1, 0
        union select 0, 2, 0
        union select 0, 3, 0
        union select 0, 4, 0
        union select 1, 0, 0
        union select 1, 1, 0
        union select 1, 2, 0
        union select 1, 3, 0
        union select 1, 4, 0
        union select 2, 0, 0
        union select 2, 1, 0
        union select 2, 2, 0
        union select 2, 3, 0
        union select 2, 4, 0
        union select 3, 0, 0
        union select 3, 1, 0
        union select 3, 2, 0
        union select 3, 3, 0
        union select 3, 4, 0
        union select 4, 0, 0
        union select 4, 1, 0
        union select 4, 2, 0
        union select 4, 3, 0
        union select 4, 4, 0))
  group by row_num, col_num) as b
  where a.col_num = b.row_num
  group by a.row_num, b.col_num;