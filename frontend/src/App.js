import "./App.css";
import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";
import AnalysisPane from "./components/analysis-pane";
import ReportUpload from "./components/report-upload";


function App() {
  const [cookie] = useCookies(["default_num_sentences"]);
  const [reportUrl, setReportUrl] = useState(null);
  const [extractedSentences, setExtractedSentences] = useState(null);
  const [nextSentencePageUrl, setNextSentencePageUrl] = useState(null);
  const [numSentences, setNumSentences] = useState(null);

  useEffect(() => {
    if (cookie.default_num_sentences) {
      setNumSentences(parseInt(cookie.default_num_sentences));
    }
  }, [cookie]);

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
                setExtractedSentences={setExtractedSentences}
                setNextSentencePageUrl={setNextSentencePageUrl}
                setReportUrl={setReportUrl}
                footer={reportUrl !== null}
              />
            </React.Fragment>
          ) : (
            <ReportUpload
              setExtractedSentences={setExtractedSentences}
              setNextSentencePageUrl={setNextSentencePageUrl}
              setReportUrl={setReportUrl}
            />
          )}
        </div>
        <div className={"seperator-bar"} />
        {extractedSentences ? (
          <AnalysisPane
            extractedSentences={extractedSentences}
            setExtractedSentences={setExtractedSentences}
            nextSentencePageUrl={nextSentencePageUrl}
            setNextSentencePageUrl={setNextSentencePageUrl}
            numSentences={numSentences}
            setNumSentences={setNumSentences}
          />
        ) : (
          <header className={"App-header"}>
            <h2>Analysis Will Appear Here</h2>
          </header>
        )}
      </div>
    </div>
  );
}

export default App;
