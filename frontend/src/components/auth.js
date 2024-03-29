import { API } from "../api-service";
import PassRequire from "./pass-require";
import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

function Auth() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLoginView, setIsLoginView] = useState(true);
  const [cookie, setCookie] = useCookies(["rs_token"]);
  const [passwordValid, setPasswordValid] = useState(false);

  document.title = "Analyst Report Summarizer";

  useEffect(() => {
    if (cookie.rs_token) {
      window.location.href = "/homepage/";
    }
  }, [cookie]);

  const loginClicked = () => {
    API.loginUser({ username, password }).then((resp) => {
      setCookie("rs_token", resp.data.token);
    });
  };

  const registerClicked = () => {
    API.registerUser({ username, password }).then(() => loginClicked());
  };

  const isDisabled =
    username.length === 0 ||
    (!isLoginView && !passwordValid) ||
    password.length === 0;

  return (
    <div className={"App"}>
      <header className={"App-header"}>
        {isLoginView ? <h1>Login</h1> : <h1>Register</h1>}
      </header>
      <div className={"login-container"}>
        <label htmlFor={"username"}>Username:</label>
        <br />
        <input
          id={"username"}
          type={"text"}
          placeholder={"Username"}
          value={username}
          onChange={(evt) => setUsername(evt.target.value)}
        />
        <br />
        <label htmlFor={"password"}>Password:</label>
        <br />
        <input
          id={"password"}
          type={"password"}
          placeholder={"Password"}
          value={password}
          onChange={(evt) => setPassword(evt.target.value)}
        />
        <br />
        {isLoginView ? (
          <button onClick={loginClicked} disabled={isDisabled}>
            Log In
          </button>
        ) : (
          <React.Fragment>
            <PassRequire
              password={password}
              setPasswordValid={setPasswordValid}
            />
            <button onClick={registerClicked} disabled={isDisabled}>
              Register
            </button>
          </React.Fragment>
        )}

        <button
          type="button"
          onClick={() => setIsLoginView(!isLoginView)}
          className={"hover"}
        >
          {isLoginView ? (
            <div>You don't already have an account? Register here!</div>
          ) : (
            <div>You already have an account? Login here</div>
          )}
        </button>
      </div>
    </div>
  );
}

export default Auth;
