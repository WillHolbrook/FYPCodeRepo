import { API } from "../../api-service";
import { useEffect } from "react";
import { useCookies } from "react-cookie";

function UserDetails(props) {
  const [cookie] = useCookies(["rs_token"]);

  useEffect(() => {
    if (cookie.rs_token) {
      API.getCurrentUser().then((resp) => {
        if (resp.status === 200) {
          if (resp.data.username.length > props.maxUsernameLength) {
            props.setUsername(
              resp.data.username.substring(0, props.maxUsernameLength - 3) +
                "..."
            );
          } else {
            props.setUsername(resp.data.username);
          }
          if (resp.data.profile.profile_image) {
            props.setProfileImageUrl(resp.data.profile.profile_image);
          }
        } else {
          console.log("Error", resp);
        }
      });
    }
  }, [cookie, props]);

  return undefined;
}

export default UserDetails;
