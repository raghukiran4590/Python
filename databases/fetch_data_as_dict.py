import psycopg2

def fetch_query_to_dict(query, db_config):
    
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        cur.execute(query)
        rows = cur.fetchall()

        # Get column names from cursor description
        column_names = [desc[0] for desc in cur.description]

        results_as_dict = []
        for row in rows:
            row_dict = dict(zip(column_names, row))
            results_as_dict.append(row_dict)

        cur.close()
        return results_as_dict

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL or executing query: {error}")
        return []
    finally:
        if conn:
            conn.close()

# Example usage:
if __name__ == "__main__":
    db_config = {
        'dbname': 'your_database_name',
        'user': 'your_username',
        'password': 'your_password',
        'host': 'localhost',
        'port': '5432'
    }

    sql_query = "SELECT id, name, email FROM users WHERE age > 25;"

    query_results = fetch_query_to_dict(sql_query, db_config)

    if query_results:
        print("Query results as a list of dictionaries:")
        for row_dict in query_results:
            print(row_dict)
    else:
        print("No results found or an error occurred.")