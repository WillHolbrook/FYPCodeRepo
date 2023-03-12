import { API } from "../../api-service";
import Loading from "../utils/loading";
import SentenceList from "./sentence-list";
import React, { useEffect, useState } from "react";
import { useCookies } from "react-cookie";

function AnalysisPane({ extractionMethod, reportDetails }) {
  const [cookie] = useCookies(["default_num_sentences"]);
  const [extractedSentences, setExtractedSentences] = useState(null);
  const [numSentences, setNumSentences] = useState(5);

  // TODO retrieve more sentences if required
  useEffect(() => {
    setExtractedSentences(null);
    let func = API.extractSentences;
    if (extractionMethod === "bert") {
      func = API.extractSentencesBERT;
    }

    func(reportDetails.pk).then((resp) => {
      // TODO deal with errors
      console.log(resp);
      console.log(resp.data.results);
      setExtractedSentences(resp.data.results);
    });
  }, [extractionMethod, reportDetails]);

  useEffect(() => {
    if (cookie.default_num_sentences) {
      const cookie_val = parseInt(cookie.default_num_sentences);
      if (cookie_val) {
        setNumSentences(cookie_val);
      }
    }
  }, [cookie]);

  return (
    <div className={"details-column"}>
      <header className={"App-header"}>
        <h2>Analysis</h2>
      </header>
      <h3 style={{ marginBottom: 0 }}>
        Stock Position: <i>{reportDetails.buy_sell_hold}</i>
      </h3>
      <div className={"App-subheading"}>
        <span>(Buy, Sell or Hold)</span>
      </div>
      <h3>Summary:</h3>
      {extractedSentences ? (
        <SentenceList
          numSentences={numSentences}
          setNumSentences={setNumSentences}
          extractedSentences={extractedSentences}
        />
      ) : (
        <Loading />
      )}
      <div className={"input-label-side-by-side"}>
        <h3>Max Number of Summary Sentences</h3>
        <div style={{ width: "4rem" }}>
          <input
            type={"number"}
            min={1}
            max={10}
            defaultValue={numSentences}
            onChange={(evt) => setNumSentences(parseInt(evt.target.value))}
          />
        </div>
      </div>
    </div>
  );
}

export default AnalysisPane;
