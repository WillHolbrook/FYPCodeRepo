import React, {useState, useEffect} from "react";

function MovieForm(props) {
  const [title, setTitle] = useState(props.movie.title);
  const [description, setDescription] = useState(props.movie.description);

  const updateClicked = () => {
    console.log('update')
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

  return (
    <React.Fragment>
      {props.movie ? (<div>
        <label htmlFor={"title"}>Title</label><br/>
        <input id={"title"} type={"text"} placeholder={"title"} value={title}
               onChange={evt => setTitle(evt.target.value)}/><br/>
        <label htmlFor={"description"}>Description</label><br/>
        <textarea id={"description"} placeholder={"Description"} value={description}
                  onChange={evt => setDescription(evt.target.value)}/><br/>
        <button onClick={updateClicked}>Update</button>
      </div>) : null}

    </React.Fragment>
  )
}

export default MovieForm