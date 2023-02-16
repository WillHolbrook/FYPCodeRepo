import { API } from "../api-service";
import { faStar } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import React, { useEffect, useState } from "react";

function MovieDetails(props) {
  const [selectedRate, setSelectedRate] = useState(-1);

  const [highlighted, setHighlighted] = useState(-1);

  let mov = props.movie;

  useEffect(() => {
    if (props.movie) {
      getDetails(props.movie.id);
    }
  }, [props.movie]);

  const highlightRate = (high) => (evt) => {
    setHighlighted(high);
  };

  const rateClicked = (rate) => (evt) => {
    API.updateMovieRating(mov.id, rate)
      .then((resp) => {
        setSelectedRate(resp.data.result.stars - 1);
        setHighlighted(resp.data.result.stars - 1);
        return resp;
      })
      .then((resp) => {
        let updated_mov = props.movie;
        updated_mov.avg_rating = resp.data.avg_rating;
        updated_mov.no_of_ratings = resp.data.no_of_ratings;
        props.setMovie(updated_mov);
        props.updateMovie(updated_mov);
        return updated_mov;
      });
  };

  const getDetails = (mov_id) => {
    API.getMyMovieRating(mov_id).then((resp) => {
      if (resp.status === 204) {
        let rating = -1;
        setSelectedRate(rating);
        setHighlighted(rating);
      } else {
        let rating = resp.data.result.stars - 1;
        setSelectedRate(rating);
        setHighlighted(rating);
      }
    });
  };

  return (
    <React.Fragment>
      {mov ? (
        <div>
          <div>
            <h1>{mov.title}</h1>
            <p>{mov.description}</p>
            <FontAwesomeIcon
              icon={faStar}
              className={mov.avg_rating >= 1 ? "orange" : ""}
            />
            <FontAwesomeIcon
              icon={faStar}
              className={mov.avg_rating >= 2 ? "orange" : ""}
            />
            <FontAwesomeIcon
              icon={faStar}
              className={mov.avg_rating >= 3 ? "orange" : ""}
            />
            <FontAwesomeIcon
              icon={faStar}
              className={mov.avg_rating >= 4 ? "orange" : ""}
            />
            <FontAwesomeIcon
              icon={faStar}
              className={mov.avg_rating >= 5 ? "orange" : ""}
            />
            ({mov.no_of_ratings})
          </div>
          <div className={"rate-container"}>
            <h2>Rate it</h2>
            {[...Array(5)].map((e, i) => {
              return (
                <FontAwesomeIcon
                  icon={faStar}
                  className={highlighted < i ? "hover" : "orange hover"}
                  key={i}
                  onMouseEnter={highlightRate(i)}
                  onMouseLeave={highlightRate(selectedRate)}
                  onClick={rateClicked(i)}
                />
              );
            })}
          </div>
        </div>
      ) : null}
    </React.Fragment>
  );
}

export default MovieDetails;