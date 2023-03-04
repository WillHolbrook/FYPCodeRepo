import { API } from "../api-service";
import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

function ProfilePage() {
  // eslint-disable-next-line no-unused-vars -- unnecessary variable of setToken is needed for return type
  const [token, setToken, removeToken] = useCookies(["rs_token"]);
  const [username, setUsername] = useState(null);

  useEffect(() => {
    if (token.rs_token) {
      API.getCurrentUser().then((resp) => {
        if (resp.status === 200) {
          setUsername(resp.data.username);
        } else {
          console.log("Error", resp);
        }
      });
    }
  }, [token]);

  const changePassword = () => {
    window.location.href = "/change_password/";
  };

  const logoutUser = () => {
    removeToken("rs_token", { path: "/" });
  };

  return (
    <div className={"App"}>
      <header className={"App-header"}>
        <h1>Account Information</h1>
      </header>
      <div className={"profile-container"}>
        <label className={"profile-label"}>Username</label>
        <br />
        <span className={"profile-span"}>{username}</span>
        <br />
        <label className={"profile-label"}>Password</label>
        <br />
        <button className={"profile-span"} onClick={changePassword}>
          Change Password
        </button>
        <br />
        <label className={"profile-label"}>API Key 1</label>
        <br />
        <span className={"profile-span"}>TODO apikey1 placeholder</span>
        <br />
        <label className={"profile-label"}>API Key 2</label>
        <br />
        <span className={"profile-span"}>TODO apikey2 placeholder</span>
        <br />
        <div className={"profile-num-sentences"}>
          <label className={"profile-label"}>Default Number of Sentences</label>
          <div style={{ width: "4rem" }}>
            <input type={"number"} min={"1"} max={"99"} defaultValue={"5"} />
          </div>
        </div>
        <br />
        <button className={"profile-span"} onClick={logoutUser}>
          Log Out
        </button>
      </div>
    </div>
  );
}

export default ProfilePage;
