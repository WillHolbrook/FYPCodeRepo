import { API } from "../api-service";
import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

function ProfilePage() {
  const [cookie, setCookie, removeCookie] = useCookies([
    "rs_token",
    "default_num_sentences",
  ]);
  const [username, setUsername] = useState(null);
  const defaultNumSentences = 5;

  useEffect(() => {
    if (cookie.rs_token) {
      API.getCurrentUser().then((resp) => {
        if (resp.status === 200) {
          setUsername(resp.data.username);
        } else {
          console.log("Error", resp);
        }
      });
    }
  }, [cookie]);

  useEffect(() => {
    if (!cookie.default_num_sentences) {
      setCookie("default_num_sentences", defaultNumSentences, { path: "/" });
    }
  });

  const updateDefaultNumSentences = (newDefaultNumSentences) => {
    setCookie("default_num_sentences", newDefaultNumSentences, { path: "/" });
  };

  const changePassword = () => {
    window.location.href = "/change_password/";
  };

  const logoutUser = () => {
    removeCookie("rs_token", { path: "/" });
  };

  return (
    <div className={"App"}>
      <header className={"App-header"}>
        <h1>Account Information</h1>
      </header>
      <div className={"profile-container"}>
        <label>Username</label>
        <br />
        <span className={"profile-span"}>{username}</span>
        <br />
        <label>Password</label>
        <br />
        <button className={"profile-span"} onClick={changePassword}>
          Change Password
        </button>
        <br />
        <label>API Key 1</label>
        <br />
        <span className={"profile-span"}>TODO apikey1 placeholder</span>
        <br />
        <label>API Key 2</label>
        <br />
        <span className={"profile-span"}>TODO apikey2 placeholder</span>
        <br />
        <div className={"input-label-side-by-side"}>
          <label>Default Number of Sentences</label>
          <div style={{ width: "4rem" }}>
            <input
              type={"number"}
              min={1}
              max={99}
              defaultValue={cookie.default_num_sentences}
              onChange={(evt) => updateDefaultNumSentences(evt.target.value)}
            />
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
