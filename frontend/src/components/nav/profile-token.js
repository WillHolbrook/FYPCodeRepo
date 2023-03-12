import UserDetails from "../profile/user-details";
import React, { useState } from "react";

function ProfileToken() {
  const [username, setUsername] = useState(null);
  const defaultProfileImageUrl = "/logo512.png";
  const [profileImageUrl, setProfileImageUrl] = useState(
    defaultProfileImageUrl
  );
  const maxUsernameLength = 16;

  const goToProfilePage = () => {
    window.location.href = "/profile/";
  };

  return (
    <div className={"profile-token hover"} onClick={goToProfilePage}>
      <UserDetails
        setUsername={setUsername}
        setProfileImageUrl={setProfileImageUrl}
        maxUsernameLength={maxUsernameLength}
      />
      <div className={"profile-token-username"}>{username}</div>
      <img
        className={"profile-picture"}
        src={profileImageUrl}
        alt={"Profile"}
      />
    </div>
  );
}

export default ProfileToken;
