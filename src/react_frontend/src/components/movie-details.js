import React, {useState, useEffect} from "react";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faStar} from "@fortawesome/free-solid-svg-icons";
import axios from "axios";


function MovieDetails(props) {

    const [selectedRate, setSelectedRate] = useState(-1)

    const [highlighted, setHighlighted] = useState(-1);


    let mov = props.movie

    useEffect(() => {
        if (props.movie) {
            axios.get(
                `http://127.0.0.1:8000/api/movies/${props.movie.id}/rate_movie/`,
                {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': 'Token 0c95087e3f74faa2745c8a69fbc7e4f842ad5ae0'
                    }
                }
            ).then(resp => {
                let rating = resp.data.result.stars - 1
                setSelectedRate(rating)
                setHighlighted(rating)
            }).catch(error => {
                console.log(error)
            })
        }
    }, [props.movie])

    const highlightRate = high => evt => {
        setHighlighted(high);
    }

    const rateClicked = rate => evt => {
        axios.post(
            `http://127.0.0.1:8000/api/movies/${mov.id}/rate_movie/`,
            JSON.stringify({stars: rate + 1}),
            {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token 0c95087e3f74faa2745c8a69fbc7e4f842ad5ae0'
                }
            }
        ).then(resp => {
                setSelectedRate(resp.data.result.stars - 1)
            }
        ).then(() => getDetails()
        ).catch(error => {
            console.log(error)
        })
    }

    const getDetails = () => {
        axios.get(
            `http://127.0.0.1:8000/api/movies/${mov.id}/`,
            {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token 0c95087e3f74faa2745c8a69fbc7e4f842ad5ae0'
                }
            }
        ).then(response => {
            props.updateMovie(response.data)
        }).catch(error => {
            console.log(error)
        })
    }

    return (
        <div>
            {mov ? (<React.Fragment>
                <div>
                    <h1>{mov.title}</h1>
                    <p>{mov.description}</p>
                    <FontAwesomeIcon icon={faStar} className={mov.avg_rating >= 1 ? 'orange' : ''}/>
                    <FontAwesomeIcon icon={faStar} className={mov.avg_rating >= 2 ? 'orange' : ''}/>
                    <FontAwesomeIcon icon={faStar} className={mov.avg_rating >= 3 ? 'orange' : ''}/>
                    <FontAwesomeIcon icon={faStar} className={mov.avg_rating >= 4 ? 'orange' : ''}/>
                    <FontAwesomeIcon icon={faStar} className={mov.avg_rating >= 5 ? 'orange' : ''}/>
                    ({mov.no_of_ratings})
                </div>
                <div className={"rate-container"}>
                    <h2>Rate it</h2>
                    {[...Array(5)].map((e, i) => {
                        return <FontAwesomeIcon
                            icon={faStar}
                            className={highlighted < i ? '' : 'orange'}
                            key={i}
                            onMouseEnter={highlightRate(i)}
                            onMouseLeave={highlightRate(selectedRate)}
                            onClick={rateClicked(i)}
                        />
                    })}
                </div>
            </React.Fragment>) : null}

        </div>
    )
}

export default MovieDetails;