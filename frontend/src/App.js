import "./App.css";
import { API } from "./api-service";
import Error from "./components/error";
import Loading from "./components/loading";
import MovieDetails from "./components/movie-details";
import MovieForm from "./components/movie-form";
import MovieList from "./components/movie-list";
import { useFetch } from "./hooks/useFetch";
import { faFilm, faSignOutAlt } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

function App() {
  const [movies, setMovies] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState(null);
  const [editedMovie, setEditedMovieMovie] = useState(null);
  // eslint-disable-next-line no-unused-vars -- unnecessary variable of setToken is needed for return type
  const [token, setToken, removeToken] = useCookies(["rs_token"]);
  const [data, loading, error] = useFetch();

  useEffect(() => {
    setMovies(data);
  }, [data]);

  useEffect(() => {
    if (!token.rs_token) {
      window.location.href = "/";
    }
  }, [token]);

  const editClicked = (movie) => {
    setEditedMovieMovie(movie);
    setSelectedMovie(null);
  };

  const removeClicked = (movie) => {
    const newMovies = movies.filter((mov) => mov.id !== movie.id);
    setMovies(newMovies);
  };

  const loadMovieDetails = (movie) => {
    setEditedMovieMovie(null);
    setSelectedMovie(movie);
  };

  const updateMovie = (movie) => {
    const newMovies = movies.map((mov) => {
      if (mov.id === movie.id) {
        return movie;
      }
      return mov;
    });
    setMovies(newMovies);
  };

  const updateMovieById = (movieId) => {
    API.getMovie(movieId).then((resp) => {
      if (resp.status === 200) {
        const newMovies = movies.map((mov) => {
          if (mov.id === movieId) {
            return resp.data;
          }
          return mov;
        });
        setMovies(newMovies);
      } else {
        console.log("Error", resp);
      }
    });
  };

  const newBlankMovie = () => {
    setEditedMovieMovie({ title: "", description: "" });
    setSelectedMovie(null);
  };

  const addCreatedMovie = (movie) => {
    const newMovies = [...movies, movie];
    setMovies(newMovies);
  };

  const logoutUser = () => {
    removeToken("rs_token", { path: "/" });
  };

  if (error) {
    return (
      <div className="App">
        <Error />
      </div>
    );
  }
  if (loading) {
    return (
      <div className="App">
        <Loading />
      </div>
    );
  }
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          <FontAwesomeIcon icon={faFilm} />
          <span>Movie rater</span>
        </h1>
        <FontAwesomeIcon
          icon={faSignOutAlt}
          className={"hover"}
          onClick={logoutUser}
        />
      </header>
      <div className="layout">
        <div>
          <MovieList
            movies={movies}
            movieClicked={loadMovieDetails}
            editClicked={editClicked}
            removeClicked={removeClicked}
          />
          <button onClick={newBlankMovie}>Add New Movie</button>
        </div>
        <MovieDetails
          movie={selectedMovie}
          setMovie={setSelectedMovie}
          updateMovie={updateMovie}
          updateMovieById={updateMovieById}
        />
        {editedMovie ? (
          <MovieForm
            movie={editedMovie}
            updateMovie={updateMovie}
            createMovie={addCreatedMovie}
          />
        ) : null}
      </div>
    </div>
  );
}

export default App;
