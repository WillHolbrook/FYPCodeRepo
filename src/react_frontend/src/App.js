import React, {useEffect, useState} from "react";
import MovieList from "./components/movie-list";
import MovieDetails from "./components/movie-details";
import MovieForm from "./components/movie-form";
import './App.css';
import {API} from "./api-service";

function App() {

  const [movies, setMovies] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState(null);
  const [editedMovie, setEditedMovieMovie] = useState(null);

  useEffect(() => {
    API.getMovies().then(response => {
      setMovies(response.data)
    })
  }, [])


  const editClicked = movie => {
    setEditedMovieMovie(movie)
    setSelectedMovie(null)
  }


  const removeClicked = movie => {
    const newMovies = movies.filter(mov => mov.id !== movie.id)
    setMovies(newMovies)
  }

  const loadMovieDetails = movie => {
    setEditedMovieMovie(null)
    setSelectedMovie(movie)
  }

  const updateMovie = movie => {
    const newMovies = movies.map(mov => {
      if (mov.id === movie.id) {
        return movie
      }
      return mov
    })
    setMovies(newMovies)
  }

  const newBlankMovie = () => {
    setEditedMovieMovie({title: '', description: ''})
    setSelectedMovie(null)
  }

  const addCreatedMovie = movie => {
    const newMovies = [...movies, movie];
    setMovies(newMovies)
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Movie rater</h1>
      </header>
      <div className="layout">
        <div>
          <MovieList
            movies={movies}
            movieClicked={loadMovieDetails}
            editClicked={editClicked}
            removeClicked={removeClicked}/>
          <button onClick={newBlankMovie}>Add New Movie</button>
        </div>
        <MovieDetails movie={selectedMovie} updateMovie={loadMovieDetails}/>
        {editedMovie ? <MovieForm movie={editedMovie} updateMovie={updateMovie} createMovie={addCreatedMovie}/> : null}
      </div>
    </div>
  );
}

export default App;
