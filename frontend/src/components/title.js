import React from "react";

function Title() {
  let className = "title";
  if (window.location.pathname !== "/") {
    className += " hover";
  }

  const goToProfilePage = () => {
    if (window.location.pathname !== "/") {
      window.location.href = "/homepage/";
    }
  };

  return (
    <div className={className} onClick={goToProfilePage}>
      Analyst Report Summarizer
    </div>
  );
}

export default Title;
