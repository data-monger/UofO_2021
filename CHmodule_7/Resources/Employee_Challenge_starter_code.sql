/*-- Use Dictinct with Orderby to remove duplicate rows
SELECT DISTINCT ON (______) _____,
______,
______,
______

INTO nameyourtable
FROM _______
WHERE _______
ORDER BY _____, _____ DESC;

*/


--- Retiring employees
----------------------------------------
select
    e.emp_no, e.first_name, e.last_name,
    t.title, t.from_date, t.to_date

into T_retirement_titles
    from public.employee e
        left join title t
            on e.emp_no = t.emp_no

where e.birth_date between '1952-01-01' and '1955-12-31'
order by e.emp_no;
--- data check
----------------------------------------
select * from T_retirement_titles;
select count(*) from t_retirement_titles;
----------------------------------------


--- Distinct Retiring employees still with the company
----------------------------------------
select distinct on(rt.emp_no)
    rt.emp_no, rt.first_name, rt.last_name,
    rt.title
into T_retirement_eligible
    from T_retirement_titles rt
where rt.to_date = '9999-01-01'
order by rt.emp_no;
--- data check
----------------------------------------
select * from T_retirement_eligible;
select count(*) from t_retiree_eligible;
---------------------------------------


--- distinct titles // count
----------------------------------------
select count(*) as count, title
into T_retiring_titles
    from T_retirement_eligible
group by title
order by count(*) desc;



--- clean up
----------------------------------------
drop table T_retirement_titles;
drop table T_retirement_eligible;
drop table T_retiring_titles;