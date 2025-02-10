import psycopg2


def load_data(data):
    conn = psycopg2.connect(
        dbname="wildfires_db",
        user="postgres",
        password="etl123",
        host="localhost",
        port="5432",
    )

    conn.rollback()

    cur = conn.cursor()

    for index, row in data.iterrows():
        cur.execute(
            """
            INSERT INTO wildfires (fire_year, discovery_date, discovery_doy,
        nwcg_cause_classification, nwcg_general_cause, cont_date,
        cont_doy, fire_size, fire_size_class, owner_descr, month,
        season)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
            (
                row["fire_year"],
                row["discovery_date"],
                row["discovery_doy"],
                row["nwcg_cause_classification"],
                row["nwcg_general_cause"],
                row["cont_date"],
                row["cont_doy"],
                row["fire_size"],
                row["fire_size_class"],
                row["owner_descr"],
                row["month"],
                row["season"],
            ),
        )

    conn.commit()  # Зафиксировать изменения в базе данных

    cur.close()
    conn.close()
