from movie import MovieDao
from fastapi import FastAPI, HTTPException
import repository as rep


app = FastAPI()

@app.get("/movies")
async def listAll(): 
    return rep.all_movies()


@app.get("/movies/{director}")
async def listAllByDirector(director: str): 
    movies = rep.movies_director(director)
    if len(movies) != 0:
        return movies
    else:
        raise HTTPException(
            status_code = 404,
            detail = "Director {0} not found".format(director)
        )
        

@app.get("/movies/of_date/{date}")
async def listAllByDirector(date: str): 
    return rep.movies_date(date)


@app.get("/movie/{id}")
async def findById(id):
    try:
        return rep.movie_id(id)
    except:
        raise HTTPException(
            status_code = 404,
            detail = "movie of id '{}' not found".format(id)
        )


@app.get("/movie/of_title/{title}")
async def findByTitle(title): 
    try:
        return rep.movie_title(title)
    except:
        raise HTTPException(
            status_code = 404,
            detail = "movie of title '{}' not found".format(title)
        )


@app.post("/movie/new")
async def add(movie: MovieDao): 
    try:
        rep.add_movie(movie)
        return {"request_status": "movie_added"}
    except:
        raise HTTPException(
            status_code = 404,
            detail = "Movie '{0}' cannot be added".format(movie.title)
        )

       
@app.delete("/movie/{id}/delete")
async def deleteById(id):
    try:
        rep.delete_by_id(id)
        return {"request_status": "movie_deleted"}
    except:
        raise HTTPException(
            status_code = 404,
            detail = "Cannot delete movie of id '{}". format(id)
        )
    
@app.delete("/movie/of_title/{title}/delete")
async def deleteByTitle(title): 
    try:
        rep.delete_by_title(title)
        return {"request_status": "movie_deleted"}
    except:
        raise HTTPException(
            status_code = 404,
            detail = "Cannot delete movie of title '{}". format(title)
        )
    

@app.delete("/movies/of_date/{date}/delete")
async def deleteByDate(date): 
    try:
        rep.delete_by_date(date)
        return {"request_status": "movie_deleted"}
    except:
        raise HTTPException(
            status_code = 404,
            detail = "Cannot delete movies released at '{}". format(date)
        )
    

@app.delete("/movies/{director}/delete")
async def deleteByDirector(director): 
    try:
        rep.delete_by_director(director)
        return {"request_status": "movie_deleted"}
    except:
        raise HTTPException(
            status_code = 404,
            detail = "Cannot delete movies directed by '{}". format(director)
        )