import React, {useState, useContext, useEffect} from "react";
import {API} from "./api-service";
import {TokenContext} from "./index";

function Auth() {

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const [token, setToken] = useContext(TokenContext)

  useEffect(() => {
    console.log(token);
    if (token) {
      window.location.href = '/movies/';
    }
  }, [token])

  const loginClicked = () => {
    API.loginUser({username, password})
      .then(resp => setToken(resp.data.token))
  }

  return (
    <div>
        <label htmlFor={"username"}>Username:</label><br/>
        <input id={"username"} type={"text"} placeholder={"username"} value={username}
               onChange={evt => setUsername(evt.target.value)}/><br/>
        <label htmlFor={"password"}>Password:</label><br/>
        <input id={"password"} type={"password"} placeholder={"password"} value={password}
                  onChange={evt => setPassword(evt.target.value)}/><br/>
        {
          <button onClick={loginClicked}>Log In</button>
        }

      </div>
  )
}

export default Auth