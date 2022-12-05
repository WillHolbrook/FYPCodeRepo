import React, {useEffect} from "react";
import {useCookies} from "react-cookie";
import axios from "axios";

function ApiComp() {
  const [token] = useCookies(['rs_token'])

  if (token.rs_token) {
    console.log(token.rs_token)
    axios.defaults.headers.common['Authorization'] = `Token ${token.rs_token}`;
  } else {
    axios.defaults.headers.common['Authorization'] = null
  }
}

export default ApiComp