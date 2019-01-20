#!/usr/bin/python3
import psycopg2

DBNAME = "news"
print("connected to the database successfully!")
""" Create query objects and assign the query value for each"""
query1 = "select title, count(*) as views from articles \
join log on log.path = CONCAT('/article/', articles.slug) \
group by articles.title order by views DESC limit 3"
query2 = "select authors.name, sum(popular_articles_view.views) as \
views from authors join \
popular_articles_view on authors.id = popular_articles_view.author \
group by authors.name order by views desc"
query3 = "select * from(select date(time), \
                        round(100.0*sum(case log.status when '200 OK' \
                              then 0 else 1 end) \
                        / count(log.status), 2) as error_perc \
                        from log group by date(time) \
                        order by error_perc desc) as res \
where error_perc > 1\
"


def get_results(query):
    """Return all results from the defined individual query above"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_results(result_Query, text):
    """Print all results from the defined individual query above"""
    for result in result_Query:
        print(str(result[0]) + " ---" + str(result[1]) + " " + text)


if __name__ == "__main__":
    print("\nThe most popular three articles of all time are:")
    print("----------------------------------------------------")
    print_results(get_results(query1), 'views')

    print("\nThe most popular article authors of all time are:")
    print("----------------------------------------------------")
    print_results(get_results(query2), 'views')

    print("\nDays with more than 1% of request that lead to an error:")
    print("-----------------------------------------------------------")
    print_results(get_results(query3), '% errors')
