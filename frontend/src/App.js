import "./App.css";
import Error from "./components/error";
import Loading from "./components/loading";
import { useFetch } from "./hooks/useFetch";
import React from "react";
import { useCookies } from "react-cookie";

function App(props) {
  // eslint-disable-next-line no-unused-vars -- unnecessary variable of setToken is needed for return type
  const [token, setToken, removeToken] = useCookies(["rs_token"]);
  // eslint-disable-next-line no-unused-vars
  const [data, loading, error] = useFetch();

  // eslint-disable-next-line no-unused-vars
  const logoutUser = () => {
    removeToken("rs_token", { path: "/" });
  };

  if (error) {
    return (
      <div className="App">
        <Error />
      </div>
    );
  }
  if (loading) {
    return (
      <div className="App">
        <Loading />
      </div>
    );
  }
  return (
    <div className={"App"}>
      <header className="App-header">
        <h1>Homepage</h1>
      </header>
    </div>
  );
}

export default App;
