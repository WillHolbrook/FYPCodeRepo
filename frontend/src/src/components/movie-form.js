import React, {useState, useEffect} from "react";
import {API} from "../api-service";

function MovieForm(props) {
  const [title, setTitle] = useState(props.movie.title);
  const [description, setDescription] = useState(props.movie.description);

  const updateClicked = () => {
    API.updateMovie(props.movie.id, {title, description}
    ).then(
      resp => props.updateMovie(resp.data)
    )
  }

  const createClicked = () => {
    API.createMovie({title, description}).then(
      resp => props.createMovie(resp.data)
    )
  }

  useEffect(() => {
    if (props.movie) {
      setTitle(props.movie.title);
      setDescription(props.movie.description);
    } else {
      setTitle(null)
      setDescription(null)
    }
  }, [props.movie])

  const isDisabled = title.length === 0 || description.length === 0;

  return (
    <React.Fragment>
      {props.movie ? (<div>
        <label htmlFor={"title"}>Title</label><br/>
        <input id={"title"} type={"text"} placeholder={"title"} value={title}
               onChange={evt => setTitle(evt.target.value)}/><br/>
        <label htmlFor={"description"}>Description</label><br/>
        <textarea id={"description"} placeholder={"Description"} value={description}
                  onChange={evt => setDescription(evt.target.value)}/><br/>
        { props.movie.id ?
          <button onClick={updateClicked} disabled={isDisabled}>Update</button>:
          <button onClick={createClicked} disabled={isDisabled}>Create</button>
        }

      </div>) : null}

    </React.Fragment>
  )
}

export default MovieForm