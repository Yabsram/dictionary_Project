import sqlalchemy as db

engine = db.create_engine('sqlite:///allwords.db')

def store_synonyms(synonym_dict, sentence):
    add_rows = """
        INSERT INTO table_allwords (original, synonyms, sentence)
        VALUES (:original, :synonym, :sentence);
    """

    with engine.connect() as connection:
        #key is the original word, value is a list of its synonyms
        for original_word, synonyms in synonym_dict.items():
            for synonym in synonyms:
                connection.execute(db.text(add_rows), {
                    "original": original_word,
                    "synonym": synonym,
                    "sentence": sentence
                })
        connection.commit()

def fetch_all_synonyms(sentence):
    select_row = "SELECT original, synonyms FROM table_allwords WHERE sentence = :sentence"
    result_dict = {}

    with engine.connect() as connection:
        result = connection.execute(db.text(select_row), {"sentence": sentence})
        for row in result.fetchall():
            orig = row[0]
            syn = row[1]
            result_dict.setdefault(orig, []).append(syn)
    return result_dict
