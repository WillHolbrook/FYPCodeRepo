import { axapi } from "../api-service";
// eslint-disable-next-line no-unused-vars -- unnecessary variable of React is needed to define as component
import React, { useEffect } from "react";
import { useCookies } from "react-cookie";

function ApiComp() {
  // eslint-disable-next-line no-unused-vars -- unnecessary variable of setToken is needed for return type
  const [token, setToken, removeToken] = useCookies(["rs_token"]);

  useEffect(() => {
    if (token.rs_token) {
      axapi.defaults.headers.common[
        "Authorization"
      ] = `Token ${token.rs_token}`;
    } else {
      axapi.defaults.headers.common["Authorization"] = null;
      if (window.location.pathname !== "/") {
        window.location.href = "/";
      }
    }
  }, [token]);

  axapi.interceptors.response.use(
    (response) => response,
    (error) => {
      console.log(error);
      if (
        error.response.status === 401 &&
        error.response.statusText === "Unauthorized"
      ) {
        if (token.rs_token) {
          removeToken("rs_token", { path: "/" });
        }
        window.location.href = "/";
      }
      throw error;
    }
  );
}

export default ApiComp;
