import axios from "axios";
import React from "react";

export let axapi = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  timeout: 10000,
  headers: {'Content-Type': 'application/json'}
});



export class API {

  static updateMovieRating(mov_id, rate) {
    return axapi.post(
      `api/movies/${mov_id}/rate_movie/`,
      {stars: rate + 1},
      null
    );
  };

  static updateMovie(mov_id, body) {
    return axapi.put(
      `api/movies/${mov_id}/`,
      body,
      null
    );
  };

  static getMyMovieRating(mov_id) {
    return axapi.get(
      `api/movies/${mov_id}/rate_movie/`
    );
  };

  static getMovie(mov_id) {
    return axapi.get(
      `api/movies/${mov_id}/`
    );
  };

  static getMovies() {
    return axapi.get(
      `api/movies/`
    );
  };

  static createMovie(body) {
    return axapi.post(
      `api/movies/`,
      body,
      null
    );
  }

  static deleteMovie(mov_id) {
    return axapi.delete(
      `api/movies/${mov_id}/`
    );
  }

  static loginUser(body) {
    return axapi.post(
      'auth/',
      body,
      {
        headers:{
          'Authorization': null
        }
      }
    );
  }

  static registerUser(body) {
    return axapi.post(
      'api/users/',
      body,
      {
        headers:{
          'Authorization': null
        }
      }
    );
  }
}