import { API, axapi } from "../api-service";
import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

function ProfileToken(props) {
  const [token] = useCookies(["rs_token"]);
  const [username, setUsername] = useState(null);
  const [profileImageUrl, setProfileImageUrl] = useState("/logo512.png");
  const max_username_length = 16;

  useEffect(() => {
    if (token.rs_token) {
      API.getCurrentUser().then((resp) => {
        if (resp.status === 200) {
          if (resp.data.username.length > max_username_length) {
            setUsername(
              resp.data.username.substring(0, max_username_length - 3) + "..."
            );
          } else {
            setUsername(resp.data.username);
          }
          setProfileImageUrl(
            `${
              axapi.defaults.baseURL
            }${resp.data.profile.profile_image.substring(1)}`
          );
        } else {
          console.log("Error", resp);
        }
      });
    }
  }, [token]);

  return (
    <div className={"profile-token"}>
      {username ? (
        <React.Fragment>
          <div className={"profile-token-username"}>{username}</div>
          <img
            className={"profile-picture"}
            src={profileImageUrl}
            alt={"Profile"}
          />
        </React.Fragment>
      ) : null}
    </div>
  );
}

export default ProfileToken;
