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
      sentence TEXT DEFAULT NULL);
   '''

   with engine.connect() as connection:
      query_result = connection.execute(db.text(create_table_sql))
      connection.commit()

