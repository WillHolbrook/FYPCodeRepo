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

  return (
    <div className={"nav-bar"}>
      {loggedIn ? (
        <React.Fragment>
          <div className={"profile-token"}>&nbsp;</div>
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
