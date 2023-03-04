import App from "./App";
import ApiComp from "./components/api-component";
import Auth from "./components/auth";
import NavBar from "./components/nav-bar";
import ProfilePage from "./components/profile-page";
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
      element: <App />,
    },
    {
      path: "/profile/",
      element: <ProfilePage />,
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
