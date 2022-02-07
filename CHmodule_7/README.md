# Module 7 | Assignment - Employee Database

Create entity relationship diagrams, perform data modeling and analysis on an employee database using SQL.


## Overview

To evaluate retirement age employees and forecast for replacements by role and department.

## Results

* 134k roles will need to be replaced due to retirement age ready employees. 
* There are less than 2k employees eligible for mentorship. 
* There does not seem to be sufficient existing employees who are eligible for mentorship to back-fill the 134k ready employees.
* Depending upon the current date, and the fore-cast for retiring age employees, this will constitute a significant loss in tribal knowledge and negatively impact the organizations bottom line earnings for the next decade.

## Summary

Below we can see this disparity by titles more clearly:

### Query
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
            on ment.title = ret.title

### Results
    title retirees, mentees
    Senior Engineer,25916,144
    Senior Staff,24926,130
    Engineer,9285,136
    Staff,7636,143
    Technique Leader,3603,70
    Assistant Engineer,1090,28
    Manager,2,NULL

