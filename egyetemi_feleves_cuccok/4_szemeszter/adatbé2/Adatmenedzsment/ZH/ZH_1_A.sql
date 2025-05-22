set serveroutput on

/*
1.
*/

declare
    title jobs.job_title%type;
    
    type emp is record(
        dep_id_db number,
        min_avg_sal_job_id jobs.job_id%type,
        job_id_db number);
    dolg emp;
    
    function dolgozok (dep_id departments.department_id%type)
        return emp is munkas emp;

    begin
        select count(*) into munkas.dep_id_db from employees
            where department_id = dep_id;
            
        select job_id into munkas.min_avg_sal_job_id from
            (select job_id, avg(salary) from employees
            where department_id = dep_id group by job_id
            order by avg(salary))
            where rownum = 1;
        
        select count(*) into munkas.job_id_db from employees
            where department_id = dep_id and job_id = munkas.min_avg_sal_job_id;
        
        return emp(munkas.dep_id_db, munkas.min_avg_sal_job_id, munkas.job_id_db);
        
    end dolgozok;
    
begin
    dolg := dolgozok(30);
    select job_title into title from jobs
        where job_id = dolg.min_avg_sal_job_id;
    dbms_output.put_line(title || ': '
        || to_char(trunc(dolg.job_id_db / dolg.dep_id_db * 100)) || '%');
end;




/*
2. 
*/

declare
    type beagy_tabla is table of employees.manager_id%type;
    tabla beagy_tabla;
    
    v_nev employees.first_name%type;
    k_nev employees.first_name%type;

    function menedzser (szam number)
        return beagy_tabla is man beagy_tabla := beagy_tabla();
    
    begin
        for c in (select manager_id from employees
            group by manager_id having count(*) > 7)
        loop
            man.extend();
            man(man.count) := c.manager_id;
        end loop;
        
        return man;
    end menedzser;

begin
    tabla := menedzser(7);
    for i in 1..tabla.count
    loop
        select first_name, last_name into v_nev, k_nev from employees
            where employee_id = tabla(i);
        dbms_output.put_line(v_nev || ' ' || k_nev);
    end loop;
end;