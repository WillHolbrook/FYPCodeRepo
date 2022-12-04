import React, {useState, useEffect} from "react";
import axios from "axios";
import MovieList from "./components/movie-list";
import MovieDetails from "./components/movie-details";
import MovieForm from "./components/movie-form";
import './App.css';

function App() {

  const [movies, setMovies] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState(null);
  const [editedMovie, setEditedMovieMovie] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/movies/",
      {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Token 0c95087e3f74faa2745c8a69fbc7e4f842ad5ae0'
        }
      }).then(response => {
      setMovies(response.data)
    }).catch(error => {
      console.log(error)
    })
  }, [])

  const editClicked = movie => {
    setEditedMovieMovie(movie)
    setSelectedMovie(null)
  }

  const updateMovie = movie => {
    setEditedMovieMovie(null)
    setSelectedMovie(movie)
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Movie rater</h1>
      </header>
      <div className="layout">
        <MovieList movies={movies} movieClicked={updateMovie} editClicked={editClicked}/>
        <MovieDetails movie={selectedMovie} updateMovie={updateMovie}/>
        {editedMovie ? <MovieForm movie={editedMovie}/> : null}
      </div>
    </div>
  );
}

export default App;
