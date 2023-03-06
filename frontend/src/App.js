import "./App.css";
import AnalysisPane from "./components/analysis-pane";
import ReportUpload from "./components/report-upload";
import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

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
        {reportUrl ? (
          <embed
            src={reportUrl}
            type={"application/pdf"}
            frameBorder={"0"}
            scrolling={"auto"}
            height={"100%"}
            width={"100%"}
          />
        ) : (
          <ReportUpload
            setExtractedSentences={setExtractedSentences}
            setNextSentencePageUrl={setNextSentencePageUrl}
            setReportUrl={setReportUrl}
          />
        )}
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
