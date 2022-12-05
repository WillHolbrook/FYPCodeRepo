import axios from "axios";
import React from "react";

export let axapi = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  timeout: 1000,
  headers: {'Content-Type': 'application/json'}
});



export class API {

  static updateMovieRating(mov_id, rate) {
    return axapi.post(
      `api/movies/${mov_id}/rate_movie/`,
      {stars: rate + 1},
      null
    ).catch(error => {
      console.log(error)
    });
  };

  static updateMovie(mov_id, body) {
    return axapi.put(
      `api/movies/${mov_id}/`,
      body,
      null
    ).catch(error => {
      console.log(error)
    });
  };

  static getMyMovieRating(mov_id) {
    return axapi.get(
      `api/movies/${mov_id}/rate_movie/`
    ).catch(error => {
      console.log(error)
    });
  };

  static getMovie(mov_id) {
    return axapi.get(
      `api/movies/${mov_id}/`
    ).catch(error => {
      console.log(error)
    });
  };

  static getMovies() {
    return axapi.get(
      `api/movies/`
    ).catch(error => {
      console.log(error)
    });
  };

  static createMovie(body) {
    return axapi.post(
      `api/movies/`,
      body,
      null
    ).catch(error => {
      console.log(error)
    });
  }

  static deleteMovie(mov_id) {
    return axapi.delete(
      `api/movies/${mov_id}/`
    ).catch(error => {
      console.log(error)
    });
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
    ).catch(error => {
      console.log(error)
    });
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
    ).catch(error => {
      console.log(error)
    });
  }
}