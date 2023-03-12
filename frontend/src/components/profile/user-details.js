import { API, axapi } from "../../api-service";
import { useEffect } from "react";
import { useCookies } from "react-cookie";

function UserDetails(props) {
  const [token] = useCookies(["rs_token"]);

  useEffect(() => {
    if (token.rs_token) {
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
          if (
            resp.data.profile.profile_image &&
            resp.data.profile.profile_image[0] === "/"
          ) {
            props.setProfileImageUrl(
              `${
                axapi.defaults.baseURL
              }${resp.data.profile.profile_image.substring(1)}` //Used to strip leading `/` from profile image url
            );
          }
        } else {
          console.log("Error", resp);
        }
      });
    }
  }, [token, props]);

  return undefined;
}

export default UserDetails;
