import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {createBrowserRouter, RouterProvider} from "react-router-dom";

export const MyContext = React.createContext(undefined);

const animals = ['snake', 'lion', 'cougar']

const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>
  },
])

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.Fragment>
    <MyContext.Provider value={{animals: animals}}>
      <RouterProvider router={router}/>
    </MyContext.Provider>
  </React.Fragment>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
