import React, {useState} from "react";
import {faEdit, faTrash} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {API} from "../api-service";

function MovieList(props) {
  const defaultMovieId = -1
  const [hoveredMovie, setHoveredMovie] = useState(defaultMovieId)

  const movieClicked = movie => evt => {
    props.movieClicked(movie, evt)
  }

  const editClicked = movie => {
    props.editClicked(movie);
  }

  const removeClicked = movie => {
    API.deleteMovie(movie.id)
      .then(resp => {
      if (resp.status === 204){
        props.removeClicked(movie)
      }
    })

  }

  return (
    <div>
      {props.movies && props.movies.map(movie => {
        return (
          <div key={movie.id} className={"movie-item"}>
            <h2 onClick={movieClicked(movie)}
                className={hoveredMovie === movie.id ? "movie-list-title hover" : "movie-list-title"}
                onMouseEnter={() => setHoveredMovie(movie.id)}
                onMouseLeave={() => setHoveredMovie(defaultMovieId)}>
              {movie.title}
            </h2>
            <FontAwesomeIcon
              icon={faEdit}
              onClick={() => editClicked(movie)}/>
            <FontAwesomeIcon
              icon={faTrash}
              onClick={() => removeClicked(movie)}/>
          </div>)
      })}
    </div>
  )
}

export default MovieList;