import React, {useState, useEffect} from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Auth from "./auth";
import reportWebVitals from './reportWebVitals';
import {createBrowserRouter, RouterProvider} from "react-router-dom";

export const TokenContext = React.createContext(undefined);

function Router() {

  const router = createBrowserRouter([
    {
      path: "/",
      element: <Auth/>
    },
    {
      path: "/movies",
      element: <App/>
    },
  ])

  const [token, setToken] = useState('');

  return (<React.StrictMode>
    <TokenContext.Provider value={[token, setToken]}>
      <RouterProvider router={router}/>
    </TokenContext.Provider>
  </React.StrictMode>)
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Router/>);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
