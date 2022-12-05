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
  }, [token])

  const loginClicked = () => {
    API.loginUser({username, password})
      .then(resp => setToken('rs_token', resp.data.token))
  }

  const registerClicked = () => {
    API.registerUser({username, password})
      .then(() => loginClicked())
  }

  const isDisabled = username.length === 0 || password.length === 0;

  return (
    <div className={"App"}>
      <header className={"App-header"}>
        {isLoginView ? <h1>Login</h1> : <h1>Register</h1>}
      </header>
      <div className={"login-container"}>
        <label htmlFor={"username"}>Username:</label><br/>
        <input id={"username"} type={"text"} placeholder={"Username"} value={username}
               onChange={evt => setUsername(evt.target.value)}/><br/>
        <label htmlFor={"password"}>Password:</label><br/>
        <input id={"password"} type={"password"} placeholder={"Password"} value={password}
               onChange={evt => setPassword(evt.target.value)}/><br/>
        {isLoginView ?
          <button onClick={loginClicked} disabled={isDisabled}>Log In</button> :
          <button onClick={registerClicked} disabled={isDisabled}>Register</button>
        }


        <p onClick={() => setIsLoginView(!isLoginView)}>
          {isLoginView ?
            "You don't already have an account? Register here!" :
            "You already have an account? Login here"}
        </p>

      </div>

    </div>
  )
}

export default Auth