import { API } from "../../api-service";
import UserDetails from "./user-details";
import { faEdit } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import React, { useCallback, useEffect, useState } from "react";
import { useCookies } from "react-cookie";
import { useDropzone } from "react-dropzone";

function ProfilePage() {
  const [cookie, setCookie, removeCookie] = useCookies([
    "rs_token",
    "default_num_sentences",
  ]);
  const [username, setUsername] = useState(null);
  const defaultProfileImageUrl = "/logo512.png";
  const [profileImageUrl, setProfileImageUrl] = useState(
    defaultProfileImageUrl
  );
  const defaultNumSentences = 5;

  document.title = "Analyst Report Summarizer";

  const onDrop = useCallback((acceptedFiles) => {
    if (acceptedFiles.length === 1) {
      API.updateProfileDetails(acceptedFiles[0]).then((resp) => {
        // TODO deal with errors
        setProfileImageUrl(resp.data.profile_image);
      });
    }
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      "image/jpeg": [".jpg", ".jpeg"],
      "image/png": [".png"],
      "image/gif": [".gif"],
      "application/pdf": [".pdf"],
    },
    maxFiles: 1,
  });

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
    window.location.href = "/";
  };

  const profilePicture = (
    <div
      className={"profile-picture"}
      style={{
        backgroundImage: `url(${profileImageUrl})`,
        backgroundSize: "cover",
        height: "7rem",
        width: "7rem",
        margin: "auto",
        padding: 0,
      }}
      {...getRootProps()}
    >
      <input className={"input-zone"} {...getInputProps()} />
      <div
        className={
          "profile-edit" + (isDragActive ? " profile-picture-drag-active" : "")
        }
      >
        <FontAwesomeIcon
          icon={faEdit}
          style={{ fontSize: "5rem", margin: "auto" }}
        />
      </div>
    </div>
  );

  return (
    <div className={"App"}>
      <UserDetails
        setUsername={setUsername}
        setProfileImageUrl={setProfileImageUrl}
        maxUsernameLength={103}
      />
      <header className={"App-header"}>
        <h1>Account Information</h1>
      </header>
      <div className={"profile-container"}>
        {profilePicture}

        <br />

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
