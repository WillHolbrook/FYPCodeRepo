import React, {useEffect, useState} from "react";
import {API} from "../api-service";
import {useCookies} from "react-cookie";

function Auth() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoginView, setIsLoginView] = useState(true);
  const [token, setToken] = useCookies(['rs_token']);

  useEffect(() => {
    if (token.rs_token) {
      window.location.href = '/movies/';
    }
  }, [token.rs_token])

  const loginClicked = () => {
    API.loginUser({username, password})
      .then(resp => setToken('rs_token', resp.data.token))
  }

  const registerClicked = () => {
    API.registerUser({username, password})
  }

  return (
    <div>
      {isLoginView ? <h1>Login</h1> : <h1>Register</h1>}
      <label htmlFor={"username"}>Username:</label><br/>
      <input id={"username"} type={"text"} placeholder={"username"} value={username}
             onChange={evt => setUsername(evt.target.value)}/><br/>
      <label htmlFor={"password"}>Password:</label><br/>
      <input id={"password"} type={"password"} placeholder={"password"} value={password}
             onChange={evt => setPassword(evt.target.value)}/><br/>
      {isLoginView ?
        <button onClick={loginClicked}>Log In</button> :
        <button onClick={loginClicked}>Register</button>
      }


      <p onClick={() => setIsLoginView(!isLoginView)}>
        {isLoginView ?
          "You don't already have an account? Register here!" :
          "You already have an account? Login here"}
      </p>


    </div>
  )
}

export default Auth