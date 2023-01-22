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
Gdzie controller to nazwa pliku uruchamiającego aplikację.
  
Do uruchomienia aplikacji potrzebne są nam zainstalowane biblioteki FastAPI oraz Uvicorn w wersji standard.  
Aby je zainstalować wykonujemy:

  ```pip install "fastapi[all]"```  
  ```pip install "uvicorn[standard]"```

W razie problemów przy instalacji należy skorzystać z flagi ```--user```

  
Aplikacja obsługuje 10 endpointów.

UWAGA! Tytuły filmów oraz imiona i nazwiska reżyserów podajemy w lower case, bez kropek,  
a whitespace deklarujemy jako "_" np.:
```John G. Avildsen``` -> ```john_gulibert_avildsen``` lub ```john_g_avildsen```

Obsługiwane endpointy:

```GET "/movies"```  
Pobiera listę wszystkich filmów.


```GET "/movies/{director}"```  
Pobiera listę wszystkich filmów danego reżysera


```GET "/movies/of_date/{date}"```  
Pobiera listę wszystkich filmów wydanych konkretnego dnia


```GET "/movie/{id}"```  
Pobiera film o danym id


```GET "/movie/of_title/{title}"```  
Pobiera film o danym tytule


```POST "/movie/new"```  
Wysyła nowy film, konieczne jest załączenie Jsonowej definicji nowego filmu np:  
```{"title":"Rocky", "release_date":"1976-12-21", "director":"John Guilbert Avildsen"}```


```DELETE "/movie/{id}/delete"```  
Usuwa film o danym id


```DELETE "/movie/of_title/{title}/delete"```  
Usuwa film o danym tytule


```DELETE "/movies/of_date/{date}/delete"```  
Usuwa wszystkie filmy wydane konkretnego dnia


```DELETE "/movies/{director}/delete"```  
Usuwa wszystkie filmy danego reżysera
