import Loading from "../utils/loading";
import AnalysisPane from "./analysis-pane";
import ReportUpload from "./report-upload";
import React, { useState } from "react";

function Homepage() {
  const [reportUrl, setReportUrl] = useState(null);
  const [reportDetails, setReportDetails] = useState(null);
  const [extractionMethod, setExtractionMethod] = useState("tfidf");
  const [loadingReport, setLoadingReport] = useState(false);

  const uploadFooter = (
    <ReportUpload
      setReportUrl={setReportUrl}
      setLoadingReport={setLoadingReport}
      setReportDetails={setReportDetails}
      footer={reportUrl !== null}
    />
  );

  let uploadContent;
  if (loadingReport) {
    uploadContent = (
      <React.Fragment>
        <Loading style={{ height: "100%" }} />
        {uploadFooter}
      </React.Fragment>
    );
  } else if (reportUrl) {
    uploadContent = (
      <React.Fragment>
        <embed
          src={reportUrl}
          type={"application/pdf"}
          frameBorder={"0"}
          scrolling={"auto"}
          height={"100%"}
          style={{ padding: "20px" }}
        />
        {uploadFooter}
      </React.Fragment>
    );
  } else {
    uploadContent = (
      <ReportUpload
        setReportUrl={setReportUrl}
        setLoadingReport={setLoadingReport}
        setReportDetails={setReportDetails}
      />
    );
  }

  const uploadPane = (
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
      {uploadContent}
    </div>
  );

  const analysisPane = (
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
            setExtractionMethod(evt.target.value);
          }}
        >
          <option value={"tfidf"}>TF-IDF</option>
          <option value={"bert"}>Sentence BERT</option>
        </select>
      </div>
    </div>
  );

  return (
    <div className={"App"}>
      <div className="layout">
        {uploadPane}
        <div className={"seperator-bar"} />
        {analysisPane}
      </div>
    </div>
  );
}

export default Homepage;
