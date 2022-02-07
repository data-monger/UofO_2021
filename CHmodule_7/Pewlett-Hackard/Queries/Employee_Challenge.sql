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
        left join public.title t
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
select count(*) from T_retirement_eligible;
---------------------------------------


--- distinct titles // count
----------------------------------------
select count(*) as count, title
into T_retiring_titles
    from T_retirement_eligible
group by title
order by count(*) desc;


--- data check
----------------------------------------
select * from T_retiring_titles;
select count(*) from T_retiring_titles;
---------------------------------------


--- Distinct employees eligible for mentorship
----------------------------------------
select e.emp_no, e.first_name, e.last_name, e.birth_date
       ,d.from_date, d.to_date
into T_mentorship
    from public.employee e

        left join public.title t
            on e.emp_no = t.emp_no

        left join public.dept_emp d
            on e.emp_no = d.emp_no
           and t.to_date = d.to_date

where
    t.to_date = '9999-01-01'
and d.to_date = '9999-01-01'
and e.birth_date between '1965-01-01' and '1965-12-31';


--- data check
----------------------------------------
select * from T_mentorship;
select count(*) from T_mentorship;
---------------------------------------


--- employee titles eligible for mentorship
----------------------------------------
select mts.* , t.title
into t_mentorship_titles
    from t_mentorship mts
        left join title t
            on mts.emp_no = t.emp_no
            and mts.from_date = t.from_date
            and mts.to_date = t.to_date;


--- count of titles eligible for mentorship
----------------------------------------
select distinct count(*) as count, title
    from t_mentorship_titles
group by title;


/*
select * from t_mentorship_titles;
select * from title limit 10;

*/
--- data check
----------------------------------------
select * from t_mentorship_titles;
select count(*) from t_mentorship_titles;
---------------------------------------




--- some comparisons
----------------------------------------
select ret.title, ret.retirees, ment.mentees
    from (select count(*) as retirees, title
                from T_retirement_eligible
            group by title
            order by count(*) desc) ret
    left join
        (select count(*) as mentees, title
                from t_mentorship_titles
            group by title
            order by count(*) desc) ment
            on ment.title = ret.title;


--- clean up
----------------------------------------
drop table T_retirement_titles;
drop table T_retirement_eligible;
drop table T_retiring_titles;
drop table T_mentorship;
drop table t_mentorship_titles;