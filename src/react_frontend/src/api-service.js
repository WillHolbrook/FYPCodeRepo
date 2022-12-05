import axios from "axios";
import React, {useEffect} from "react";

axios.defaults.headers.common['Content-Type'] = 'application/json';
axios.defaults.baseURL = 'http://127.0.0.1:8000/';

export class API {

  static updateMovieRating(mov_id, rate) {
    return axios.post(
      `api/movies/${mov_id}/rate_movie/`,
      {stars: rate + 1},
      null
    ).catch(error => {
      console.log(error)
    });
  };

  static updateMovie(mov_id, body) {
    return axios.put(
      `api/movies/${mov_id}/`,
      body,
      null
    ).catch(error => {
      console.log(error)
    });
  };

  static getMyMovieRating(mov_id) {
    return axios.get(
      `api/movies/${mov_id}/rate_movie/`
    ).catch(error => {
      console.log(error)
    });
  };

  static getMovie(mov_id) {
    return axios.get(
      `api/movies/${mov_id}/`
    ).catch(error => {
      console.log(error)
    });
  };

  static getMovies() {
    return axios.get(
      `api/movies/`
    ).catch(error => {
      console.log(error)
    });
  };

  static createMovie(body) {
    return axios.post(
      `api/movies/`,
      body,
      null
    ).catch(error => {
      console.log(error)
    });
  }

  static deleteMovie(mov_id) {
    return axios.delete(
      `api/movies/${mov_id}/`
    ).catch(error => {
      console.log(error)
    });
  }

  static loginUser(body) {
    return axios.post(
      'auth/',
      body,
      {
        headers:{
          'Authorization': null
        }
      }
    ).catch(error => {
      console.log(error)
    });
  }

  static registerUser(body) {
    return axios.post(
      'api/users/',
      body,
      {
        headers:{
          'Authorization': null
        }
      }
    ).catch(error => {
      console.log(error)
    });
  }
}