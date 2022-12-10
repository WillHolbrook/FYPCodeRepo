import React, {useEffect} from "react";
import {useCookies} from "react-cookie";
import {axapi} from "../api-service";

function ApiComp() {
  const [token, setToken, removeToken] = useCookies(['rs_token'])

  useEffect(() => {
    if (token.rs_token) {
      console.log(token.rs_token)
      axapi.defaults.headers.common['Authorization'] = `Token ${token.rs_token}`;
    } else {
      axapi.defaults.headers.common['Authorization'] = null
      console.log(window.location.pathname)
      if (window.location.pathname !== '/') {
        console.log(window.location.pathname)
        window.location.href = '/';
      }
    }
  }, [token])

  axapi.interceptors.response.use((response) => response, (error) => {
    console.log(error)
    if (error.response.status === 401 && error.response.statusText === 'Unauthorized') {

      if (token.rs_token) {
        removeToken('rs_token', {path: '/'})
      }
      window.location.href = '/'
    }
    throw error;
  });
}

export default ApiComp