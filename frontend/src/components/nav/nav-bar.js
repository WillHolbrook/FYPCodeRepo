import ProfileToken from "./profile-token";
import Title from "./title";
import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

function NavBar() {
  const [cookie] = useCookies(["rs_token"]);
  const [loggedIn, setLoggedIn] = useState(false);

  useEffect(() => {
    setLoggedIn(!!cookie.rs_token);
  }, [cookie]);

  const goToUploadHistory = () => {
    window.location.href = "/upload_history/";
  };

  return (
    <div className={"nav-bar"}>
      {loggedIn ? (
        <React.Fragment>
          <div
            className={"nav-bar-subheading hover"}
            onClick={goToUploadHistory}
            style={{ justifyContent: "flex-start", paddingLeft: "10px" }}
          >
            <div className={"nav-bar-link"}>Upload History</div>
          </div>
          <Title />
          <ProfileToken />
        </React.Fragment>
      ) : (
        <Title />
      )}
    </div>
  );
}

export default NavBar;
