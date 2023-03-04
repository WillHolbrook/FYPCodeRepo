import PassRequire from "./pass-require";
import React, { useState } from "react";

function ChangePassword() {
  const [password, setPassword] = useState("");
  const [reTypedPassword, setReTypedPassword] = useState("");
  const [passwordValid, setPasswordValid] = useState(false);

  const isDisabled = !passwordValid || password.length === 0;

  const changePasswordClicked = () => {
    console.log("In Change Password");
  };

  return (
    <div className={"App"}>
      <header className={"App-header"}>
        <h1>Change Password</h1>
      </header>
      <div className={"login-container"}>
        <label htmlFor={"password"}>New Password</label>
        <br />
        <input
          id={"password"}
          type={"password"}
          placeholder={"New Password"}
          value={password}
          onChange={(evt) => setPassword(evt.target.value)}
        />
        <label htmlFor={"reTypedPassword"}>Re-Type New Password</label>
        <br />
        <input
          id={"reTypedPassword"}
          type={"password"}
          placeholder={"Re-Type New Password"}
          value={reTypedPassword}
          onChange={(evt) => setReTypedPassword(evt.target.value)}
        />
        <PassRequire
          password={password}
          reTypedPassword={reTypedPassword}
          setPasswordValid={setPasswordValid}
        />
        <button onClick={changePasswordClicked} disabled={isDisabled}>
          Change Password
        </button>
      </div>
    </div>
  );
}

export default ChangePassword;
