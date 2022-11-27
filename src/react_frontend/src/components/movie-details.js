import React from "react";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faStar} from "@fortawesome/free-solid-svg-icons";


function MovieDetails(props) {
  
  const mov = props.movie
  return (
    <div>
      {mov ? (<div>
        <h1>{mov.title}</h1>
        <p>{mov.description}</p>
        <FontAwesomeIcon icon={faStar} className={mov.avg_rating >= 1 ? 'orange' : ''}/>
        <FontAwesomeIcon icon={faStar} className={mov.avg_rating >= 2 ? 'orange' : ''}/>
        <FontAwesomeIcon icon={faStar} className={mov.avg_rating >= 3 ? 'orange' : ''}/>
        <FontAwesomeIcon icon={faStar} className={mov.avg_rating >= 4 ? 'orange' : ''}/>
        <FontAwesomeIcon icon={faStar} className={mov.avg_rating >= 5 ? 'orange' : ''}/>
        ({mov.no_of_ratings})
      </div>) : null}

    </div>
  )
}

export default MovieDetails;