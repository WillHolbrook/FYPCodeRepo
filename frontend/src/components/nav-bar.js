import Title from "./title";
import React from "react";
import ProfileToken from "./profile-token";

function NavBar() {
  return (
    <div className={"nav-bar"}>
      <div className={"profile-token"}>&nbsp;</div>
      <Title />
      <ProfileToken username={"Will Holbrook"} profileImageUrl={"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/800px-Image_created_with_a_mobile_phone.png"}/>
    </div>
  );
}

export default NavBar;
