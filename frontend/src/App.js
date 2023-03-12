import "./App.css";
import AnalysisPane from "./components/analysis-pane";
import ReportUpload from "./components/report-upload";
import React, { useState } from "react";

function App() {
  const [reportUrl, setReportUrl] = useState(null);
  const [reportDetails, setReportDetails] = useState(null);
  const [extractionMethod, setExtractionMethod] = useState("tfidf");

  console.log(reportDetails);

  return (
    <div className={"App"}>
      <div className="layout">
        <div className={"details-column"}>
          <header className={"App-header"}>
            <h2>Summarize Analyst Reports</h2>
            <div className={"App-subheading"}>
              <span>
                Extract important sentences as a summary of the report & extract
                buy, sell or hold
              </span>
            </div>
          </header>
          {reportUrl ? (
            <React.Fragment>
              <embed
                src={reportUrl}
                type={"application/pdf"}
                frameBorder={"0"}
                scrolling={"auto"}
                height={"100%"}
                style={{ padding: "20px" }}
              />
              <ReportUpload
                setReportUrl={setReportUrl}
                setReportDetails={setReportDetails}
                footer={reportUrl !== null}
              />
            </React.Fragment>
          ) : (
            <ReportUpload
              setReportUrl={setReportUrl}
              setReportDetails={setReportDetails}
            />
          )}
        </div>
        <div className={"seperator-bar"} />
        <div className={"details-column"}>
          {reportDetails ? (
            <AnalysisPane
              extractionMethod={extractionMethod}
              reportDetails={reportDetails}
            />
          ) : (
            <header className={"App-header"}>
              <h2>Analysis Will Appear Here</h2>
            </header>
          )}
          <div className={"input-label-side-by-side"}>
            <h3>Select an extraction method:</h3>
            <select
              style={{ width: "auto" }}
              id="extraction-method"
              name="extraction-method"
              onChange={(evt) => {
                if (evt.target.value === "tfidf") {
                  setExtractionMethod("tfidf");
                } else if (evt.target.value === "bert") {
                  setExtractionMethod("bert");
                }
              }}
            >
              <option value={"tfidf"}>TF-IDF</option>
              <option value={"bert"}>Sentence BERT</option>
            </select>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
