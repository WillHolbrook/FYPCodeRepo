import axios from "axios";
// eslint-disable-next-line no-unused-vars -- unnecessary variable of React is needed to define as component
import React from "react";

export let axapi = axios.create({
  baseURL: "http://127.0.0.1:8000/",
  timeout: 10000,
  headers: { "Content-Type": "application/json" },
});

export class API {
  static loginUser(body) {
    return axapi.post("auth/", body, {
      headers: {
        Authorization: null,
      },
    });
  }

  static registerUser(body) {
    return axapi.post("api/users/", body, {
      headers: {
        Authorization: null,
      },
    });
  }
}
