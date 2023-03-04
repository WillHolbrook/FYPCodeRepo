import "./App.css";
import Error from "./components/error";
import Loading from "./components/loading";
import { useFetch } from "./hooks/useFetch";
import React from "react";

function App(props) {
  // eslint-disable-next-line no-unused-vars
  const [data, loading, error] = useFetch();

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
