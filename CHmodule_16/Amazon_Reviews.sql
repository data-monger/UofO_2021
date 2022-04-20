
-- Data validation, test, and review scripts
	select count(*) from customers_table    ;
	select count(*) from products_table     ;
	select count(*) from review_id_table    ;
	select count(*) from vine_table         ;


	/*
		truncate  table  customers_table        ;
		truncate  table  products_table         ;
		truncate  table  review_id_table        ;
		truncate  table  vine_table             ;
	*/

	select * from customers_table   ;
	select * from products_table    ;
	select * from review_id_table   ;
	select * from vine_table		;



/*
Work begins here... 
*/
-- Deliverable 2:
	select *, cast(helpful_votes as float) / cast(total_votes as float) as perc_votes
	into t_paid
	from vine_table
	where
		total_votes > 20 													-- 20 or more votes ; 2.1
	and vine = 'Y' 															-- vine == 'y' ; 2.3
	group by review_id, star_rating, helpful_votes, total_votes, vine, verified_purchase
	having cast(helpful_votes as float) / cast(total_votes as float)> 0.5; 	-- >50% ; 2.2



-- Deliverable 2.4 ; repeat step 3, (2 and 1)
	select *, cast(helpful_votes as float) / cast(total_votes as float) as perc_votes
	into t_unpaid
	from vine_table
	where
		total_votes > 20 													-- 20 or more votes ; 2.1
	and vine = 'N' 															-- vine == 'n' ; 2.3
	group by review_id, star_rating, helpful_votes, total_votes, vine, verified_purchase
	having cast(helpful_votes as float) / cast(total_votes as float)> 0.5; 	-- >50% ; 2.2


-- review t_paid table
	select * from t_paid ;

-- review t_unpaid table
	select * from t_unpaid ;


-- Deliverable 2.5
-- this produces 2 distint record sets. see: ReadMe and Screen Shot
	select
			'paid' as type	
		,  (select count (*)                from t_paid)                                        as total_review		-- total number of reviews
		,  (select count (star_rating)      from t_paid where star_rating = 5)                  as five_star		-- number of five star reviews
		,  cast((select count (star_rating) from t_paid where star_rating = 5) as float ) /
		   cast((select count (*)           from t_paid) as float)                              as perc_five_star	-- percentage of 5 star reviews

	union all

	select
			'unpaid' as type
		,  (select count (*)                from t_unpaid)                                      as total_review		-- total number of reviews
		,  (select count (star_rating)      from t_unpaid where star_rating = 5)                as five_star		-- number of five star reviews
		,  cast((select count (star_rating) from t_unpaid where star_rating = 5) as float ) /
		   cast((select count (*)           from t_unpaid) as float)                            as perc_five_star;	-- percentage of 5 star reviews
