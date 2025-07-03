import sqlalchemy as db
from sqlalchemy.exc import OperationalError


engine = db.create_engine('sqlite:///allwords.db')


def store_synonyms(synonym_dict, sentence):
    add_rows = """
                INSERT INTO table_allwords (original, synonyms, sentence)
                VALUES (:original, :synonym, :sentence); """

    with engine.connect() as connection:
        for original_word, synonyms in synonym_dict.items():
            for synonym in synonyms:
                connection.execute(db.text(add_rows), {
                    "original": original_word,
                    "synonym": synonym,
                    "sentence": sentence
                })
        connection.commit()


def fetch_all_synonyms(sentence):
    select_row = """
                    SELECT original, synonyms FROM table_allwords
                    WHERE sentence = :sentence
                """
    result_dict = {}

    with engine.connect() as connection:
        result = (
                    connection.execute(db.text(select_row),
                    {"sentence": sentence})
                 )
        for row in result.fetchall():
            orig = row[0]
            syn = row[1]
            result_dict.setdefault(orig, []).append(syn)
    return result_dict


def print_entire_table():
    try:
        query = "SELECT * FROM table_allwords"
        with engine.connect() as connection:
            result = connection.execute(db.text(query))
            rows = result.fetchall()

            if not rows:
                print("The table is empty.")
                return

            print(" | ".join(result.keys()))
            print("-" * 50)

            for row in rows:
                print(" | ".join(str(value) if value is not None
                else "NULL" for value in row))
    except OperationalError:
        print("Synonym history does not exist. Please look up words first.")


def clear_table_allwords():
    try:
        with engine.connect() as connection:
            connection.execute(db.text("DELETE FROM table_allwords"))
            connection.commit()
        print("Table has been cleared.")
    except OperationalError:
        print("Synonym history does not exist. Please look up words first.")
