import sqlalchemy as db

'''
Should look like this:
+----+----------+-----------+----------------------------------+
| id | word     | synonyms  |           sentence               |
+----+----------+-----------+----------------------------------+
| 1  | happy    | joyful    | "I love feeling ___."            |
| 2  | happy    | cheerful  | "I love feeling ___."            |
| 3  | happy    | glad      | "I love feeling ___."            |
| 4  | sad      | unhappy   | "I feel so ___ when it rains."   |
| 5  | sad      | gloomy    | "I feel so ___ when it rains."   |
+----+----------+-----------+----------------------------------+

get  sentence, get user inputted word, and its synonyms from wordapi
'''

def init_db():
   engine = db.create_engine('sqlite:///allwords.db')
   #create or connect to the table if it exists already
   create_table_sql = '''
      CREATE TABLE IF NOT EXISTS table_allwords (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      original TEXT NOT NULL,
      synonyms TEXT NOT NULL,
      sentence TEXT NOT NULL);
   '''

   with engine.connect() as connection:
   query_result = connection.execute(db.text(create_table_sql))
   connection.commit()

# #def listallWords(self, sentence, dict_synonyms):
#    engine = db.create_engine('sqlite:///allwords.db')

#    #create or connect to the table if it exists already
#    create_table_sql = '''
#       CREATE TABLE IF NOT EXISTS table_allwords (
#       id INTEGER PRIMARY KEY AUTOINCREMENT,
#       original TEXT NOT NULL,
#       synonyms TEXT NOT NULL,
#       sentence TEXT NOT NULL);
#    '''

#    with engine.connect() as connection:
#       query_result = connection.execute(db.text(create_table_sql))
#       connection.commit()

   # #now add rows
   # add_rows = """
   #    INSERT INTO table_allwords (original, synonyms, sentence)
   #    VALUES (:original, :synonym, :sentence);
   # """

   # with engine.connect() as connection:
   #    #key is the original word, value is a list of its synonyms
   #    for original_word, synonym_list in dict_synonyms.items():
   #       for word in synonym_list:
   #          connection.execute(db.text(add_rows), 
   #          {
   #             "original": original_word
   #             "synonmy": word,
   #             "sentence": sentence
   #          }
   #       )
   #    connection.commit()