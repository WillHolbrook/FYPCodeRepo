import React from "react";

function AnalysisPane(props) {
  return (
    <div>
      <header className={"App-header"}>
        <h2>Analysis</h2>
      </header>
      <ol>
        {props.extractedSentences.map((sentence, index) => {
          if (index < props.numSentences) {
            return <li key={index}>{sentence.text}</li>;
          } else {
            return null;
          }
        })}
      </ol>
    </div>
  );
}

export default AnalysisPane;
