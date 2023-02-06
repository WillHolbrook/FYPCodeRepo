import App from "./App";
import ApiComp from "./components/api-component";
import Auth from "./components/auth";
import NavBar from "./components/nav-bar";
import "./index.css";
import reportWebVitals from "./reportWebVitals";
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
      path: "/movies",
      element: <App />,
    },
  ]);

  return (
    <React.StrictMode>
      <CookiesProvider>
        <div className={"top-level"}>
          <NavBar />
          <ApiComp />
          <RouterProvider router={router} />
        </div>
      </CookiesProvider>
    </React.StrictMode>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Router />);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
