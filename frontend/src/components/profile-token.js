import { API, axapi } from "../api-service";
import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

function ProfileToken(props) {
  const [token] = useCookies(["rs_token"]);
  const [username, setUsername] = useState(null);
  const defaultProfileImageUrl = "/logo512.png";
  const [profileImageUrl, setProfileImageUrl] = useState(
    defaultProfileImageUrl
  );
  const maxUsernameLength = 16;

  const goToProfilePage = () => {
    window.location.href = "/profile/";
  };

  useEffect(() => {
    if (token.rs_token) {
      API.getCurrentUser().then((resp) => {
        if (resp.status === 200) {
          if (resp.data.username.length > maxUsernameLength) {
            setUsername(
              resp.data.username.substring(0, maxUsernameLength - 3) + "..."
            );
          } else {
            setUsername(resp.data.username);
          }
          if (
            resp.data.profile.profile_image &&
            resp.data.profile.profile_image[0] === "/"
          ) {
            setProfileImageUrl(
              `${
                axapi.defaults.baseURL
              }media/${resp.data.profile.profile_image.substring(1)}` //Used to strip leading `/` from profile image url
            );
          }
        } else {
          console.log("Error", resp);
        }
      });
    }
  }, [token]);

  return (
    <div className={"profile-token hover"} onClick={goToProfilePage}>
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
