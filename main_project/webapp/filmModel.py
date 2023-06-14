from .baseModel import BaseModel

class FilmModel(BaseModel):

  def GetAllFilms():

    model = BaseModel()
    model.db_alias = 'sakila'

    sql = "SELECT film_id, title, release_year, language_id, special_features \
          FROM `film` \
          Order by film_id desc limit 3"
    return ( model.ExecuteQuery( sql))
  
 
  def GeAllUSers():

    model = BaseModel()
    model.db_alias = 'sql_lite'

    sql = "SELECT * FROM users"
    return ( model.ExecuteQuery( sql))