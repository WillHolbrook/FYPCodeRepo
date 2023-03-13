import ApiComp from "./components/api-component";
import Auth from "./components/auth";
import UploadHistory from "./components/history/history";
import Homepage from "./components/homepage/homepage";
import NavBar from "./components/nav/nav-bar";
import ChangePassword from "./components/profile/change-password";
import ProfilePage from "./components/profile/profile-page";
import "./index.css";
import React from "react";
import { CookiesProvider } from "react-cookie";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

function Router() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Auth />,
    },
    {
      path: "/homepage/",
      element: <Homepage />,
    },
    {
      path: "/profile/",
      element: <ProfilePage />,
    },
    {
      path: "/change_password/",
      element: <ChangePassword />,
    },
    {
      path: "/upload_history/",
      element: <UploadHistory />,
    },
  ]);

  return (
    <React.StrictMode>
      <CookiesProvider>
        <div className={"top-level"}>
          <ApiComp />
          <NavBar />
          <RouterProvider router={router} />
        </div>
      </CookiesProvider>
    </React.StrictMode>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Router />);
