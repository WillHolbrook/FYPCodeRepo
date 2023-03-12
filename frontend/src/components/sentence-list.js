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
      <div className={"input-label-side-by-side"}>
        <h3>Max Number of Summary Sentences</h3>
        <div style={{ width: "4rem" }}>
          <input
            type={"number"}
            min={1}
            max={10}
            defaultValue={props.numSentences}
            onChange={(evt) =>
              props.setNumSentences(parseInt(evt.target.value))
            }
          />
        </div>
      </div>
    </React.Fragment>
  );
}

export default SentenceList;
