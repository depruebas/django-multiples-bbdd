from django.db import connections

class BaseModel:

  def __init__(self, db_alias='default'):
        self._db_alias = db_alias
    
  @property
  def db_alias(self):
      return self._db_alias
  
  @db_alias.setter
  def db_alias(self, value):
      if value not in connections:
          raise ValueError(f"La base de datos '{value}' no está configurada en settings.DATABASES.")
      self._db_alias = value
  
  def ExecuteQuery (self, sql):

    if self.db_alias not in connections:
        raise ValueError(f"La base de datos '{self.db_alias}' no está configurada en settings.DATABASES.")
    
    connection = connections[self.db_alias]
    
    cursor = connection.cursor()
    
    cursor.execute( sql)

    columns = [col[0] for col in cursor.description]

    rows = [ dict(zip(columns, row)) for row in cursor.fetchall() ]

    return [ { 'columns': columns, 
               'rows': rows,
               'total': cursor.rowcount       
            } ]
    

  def Execute (self, sql):

    if self.db_alias not in connections:
        raise ValueError(f"La base de datos '{self.db_alias}' no está configurada en settings.DATABASES.")
    
    connection = connections[self.db_alias]

    cursor = connection.cursor()
    
    cursor.execute( sql)

    return [ cursor.fetchone() ]