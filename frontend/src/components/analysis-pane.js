import React from "react";

function AnalysisPane(props) {
  // TODO retrieve more sentences if required

  return (
    <div className={"details-column"}>
      <header className={"App-header"}>
        <h2>Analysis</h2>
      </header>
      <h3 style={{ marginBottom: 0 }}>
        Stock Position: <i>TODO</i>
      </h3>
      <div className={"App-subheading"}>
        <span>(Buy, Sell or Hold)</span>
      </div>
      <h3>Summary:</h3>
      <ol style={{ flexGrow: 1 }}>
        {props.extractedSentences.map((sentence, index) => {
          if (index < props.numSentences) {
            return <li key={index}>{sentence.text}</li>;
          } else {
            return null;
          }
        })}
      </ol>
      <div className={"num-sentences"}>
        <h3>Max Number of Summary Sentences</h3>
        <div style={{ width: "4rem" }}>
          <input
            type={"number"}
            min={1}
            max={99}
            defaultValue={props.numSentences}
            onChange={(evt) => props.setNumSentences(evt.target.value)}
          />
        </div>
      </div>
    </div>
  );
}

export default AnalysisPane;
