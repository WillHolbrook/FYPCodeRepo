import "./App.css";
import AnalysisPane from "./components/analysis-pane";
import Error from "./components/error";
import Loading from "./components/loading";
import ReportUpload from "./components/report-upload";
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
      <div className="layout">
        <ReportUpload />
        <div className={"seperator-bar"} />
        <AnalysisPane />
      </div>
    </div>
  );
}

export default App;
