
import psycopg2

# Using ElephantSQL
dbname = 'zdkyfkhh'
user = 'zdkyfkhh'
password = 'secret'
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

def get_result(query):
    pg_curs.execute(query)
    return pg_curs.fetchall()

# Q1: How many passengers survived, died?
query1 = 'SELECT survived, COUNT(survived) AS num_passengers FROM titanic_table GROUP BY survived;'
get_result(query1)
[(0, 545), (1, 342)]

# Q2: How many passengers were in each class?
query2 = 'SELECT pclass, COUNT(pclass) AS num_per_class FROM titanic_table GROUP BY pclass;'
get_result(query2)
[(1, 216), (3, 487), (2, 184)]

#Q3: How many passengers survived, died within each class?
query3 = 'SELECT pclass, survived, COUNT(survived) AS num_passengers FROM titanic_table GROUP BY survived, pclass ORDER BY pclass;'
get_result(query3)
[(1, 0, 80), (1, 1, 136), (2, 1, 87), (2, 0, 97), (3, 0, 368), (3, 1, 119)]

#Q4: What was the average age of survivors v. non survivors?
query4 = 'SELECT survived, AVG(age) AS avg_age FROM titanic_table GROUP BY survived;'
get_result(query4)
[(0, Decimal('30.1541284403669725')), (1, Decimal('28.4122807017543860'))]

#Q5: What was the average age of each passenger class?
query5 = 'SELECT pclass, AVG(age) AS avg_age FROM titanic_table GROUP BY pclass;'
get_result(query5)
[(1, Decimal('38.7916666666666667')), (3, Decimal('25.2032854209445585')), (2, Decimal('29.8804347826086957'))]

#Q6: What was the average fare by passenger class? Survival?
query6 = 'SELECT pclass, survived, AVG(fare) AS avg_fare FROM titanic_table GROUP BY pclass, survived ORDER BY pclass, survived;'
get_result(query6)
[(1, 0, 64.6840073347092), (1, 1, 95.6080288185793), (2, 0, 19.4123278549037), (2, 1, 22.0557000390415), (3, 0, 13.7118531063847), (3, 1, 13.6948874778106)]

#Q7: How many siblings/spouses aboard on average, by passenger class? Survival?
query7 = 'SELECT pclass, survived, AVG(siblings_spouses_aboard) AS avg_sibs_spouses FROM titanic_table GROUP BY pclass, survived ORDER BY pclass, survived;'
get_result(query7)
[(1, 0, Decimal('0.28750000000000000000')), (1, 1, Decimal('0.49264705882352941176')), (2, 0, Decimal('0.31958762886597938144')), (2, 1, Decimal('0.49425287356321839080')), (3, 0, Decimal('0.67934782608695652174')), (3, 1, Decimal('0.43697478991596638655'))]

#Q8: How many parents/children aboard on average, by class? survival?
query8 = 'SELECT pclass, survived, AVG(parents_children_aboard) AS avg_parents_child FROM titanic_table GROUP BY pclass, survived ORDER BY pclass, survived;'
get_result(query8)
[(1, 0, Decimal('0.30000000000000000000')), (1, 1, Decimal('0.38970588235294117647')), (2, 0, Decimal('0.14432989690721649485')), (2, 1, Decimal('0.64367816091954022989')), (3, 0, Decimal('0.38858695652173913043')), (3, 1, Decimal('0.42016806722689075630'))]

#Q9: Do any passengers have the same name?
query9 = 'SELECT name FROM titanic_table GROUP BY name HAVING COUNT(name) > 1;'
get_result(query9)
[] # No two passengers have the same name.



