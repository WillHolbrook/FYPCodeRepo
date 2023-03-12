import React from "react";

function SentenceList(props) {
  return (
    <React.Fragment>
      <ol style={{ flexGrow: 1 }}>
        {props.extractedSentences.map((sentence, index) => {
          if (index < props.numSentences) {
            return <li key={index}>{sentence.text}</li>;
          } else {
            return null;
          }
        })}
      </ol>
    </React.Fragment>
  );
}

export default SentenceList;
