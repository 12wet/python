Autor: Łukasz Świder

Projekt jest api wykorzystującym bibliotekę FastAPI, obsługujący requesty GET, POST oraz DELETE.

Składa się z 5 plików: 

controller.py - odpowiada za uruchomienie aplikacji domyślnie pod adresem http://localhost:8000  
databse_connector.py - proste nawiązanie połączenia z bazą sqlite3  
movie.py - zawiera definicję klasy Model oraz jego 'lżejszego' odpowiednika ModelDao pozbawionego zmiennej 'id'  
repository.py - odpowiada za komunikację z bazą danych  
movies_database.db - zawiera bazę danych  

Aplikację urochamiamy za pomocą komendy: 

  ```python -m uvicorn controller:app --reload```
  
Do uruchomienia aplikacji potrzebne są nam zainstalowane biblioteki FastAPI oraz Uvicorn w wersji standard.  
Aby je zainstalować wykonujemy:

  ```pip install "fastapi[all]"```  
  ```pip install "uvicorn[standard]"```

W razie problemów przy instalacji należy skorzystać z flagi ```--user```

Aplikacja obsługuje 10 endpointów:

```GET "/movies"
```GET "/movies/{director}"
```@app.get("/movies/of_date/{date}")
```@app.get("/movie/{id}")
```@app.get("/movie/of_title/{title}")
```@app.post("/movie/new")
```@app.delete("/movie/{id}/delete")
```@app.delete("/movie/of_title/{title}/delete")
```@app.delete("/movies/of_date/{date}/delete")
```@app.delete("/movies/{director}/delete")
