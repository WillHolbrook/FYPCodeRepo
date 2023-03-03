import React, {useEffect, useState} from "react";
import {useCookies} from "react-cookie";
import {axapi} from "../api-service";

function ProfileToken(props) {
  const [token] = useCookies(["rs_token"]);
  const [username, setUsername] = useState("");
  const [profileImageUrl, setProfileImageUrl] = useState("");

  useEffect(() => {
    if (token.rs_token) {

    }
  }, [token]);

  return (
    <div className={"profile-token"}>
      <div className={"profile-token-username"}>{props.username}</div>
      <img className={"profile-picture"} src={props.profileImageUrl} alt={"Profile"}/>
    </div>
  );
}

export default ProfileToken;
