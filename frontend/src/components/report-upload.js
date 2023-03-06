import { API, axapi } from "../api-service";
import { faFileArrowUp } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import React, { useCallback } from "react";
import { useDropzone } from "react-dropzone";

function ReportUpload(props) {
  const onDrop = useCallback((acceptedFiles) => {
    // TODO add_loading_spinner
    API.uploadReport(acceptedFiles[0])
      .then((resp) => {
        // TODO deal with errors
        // TODO set message to show file uploaded and plaintext extracted now extracting sentences
        console.log(resp);
        props.setReportUrl(
          `${axapi.defaults.baseURL}${resp.data.pdf.substring(1)}`
        );
        return resp.data.pk;
      })
      .then((report_pk) => {
        API.extractSentences(report_pk).then((resp) => {
          // TODO deal with errors
          props.setExtractedSentences(resp.data.results);
          props.setNextSentencePageUrl(resp.data.next);
          console.log(resp);
        });
      });
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const {
    getRootProps,
    getInputProps,
    acceptedFiles,
    fileRejections,
    isDragActive,
  } = useDropzone({
    onDrop,
    accept: {
      "application/pdf": [".pdf"],
    },
    maxFiles: 1,
  });

  const cropFilePath = (filepath) => {
    const maxFilePath = 23;
    if (filepath.length <= maxFilePath) {
      return filepath;
    } else {
      const lastIndex = filepath.lastIndexOf(".");
      const before = filepath.slice(0, lastIndex);
      const after = filepath.slice(lastIndex + 1);

      return before.substring(0, maxFilePath - 3) + "..." + after;
    }
  };

  const rejectedFiles = fileRejections.map(({ file, errors }) => {
    return (
      <li key={file.path}>
        Error: {cropFilePath(file.path)} - {file.size} bytes
        <ul>
          {errors.map((e) => (
            <li key={e.code}>{e.message}</li>
          ))}
        </ul>
      </li>
    );
  });

  const files = acceptedFiles.map((file) => (
    <li style={{ paddingRight: 0 }} key={file.path}>
      {cropFilePath(file.path)} - {file.size} bytes
    </li>
  ));

  return (
    <div className={"report-upload"}>
      <header className={"App-header"}>
        <h2>Summarize Analyst Reports</h2>
        <div className={"App-subheading"}>
          <span>
            Extract important sentences as a summary of the report & extract
            buy, sell or hold
          </span>
        </div>
      </header>
      <div
        className={
          "drag-and-drop-container hover" +
          (isDragActive ? " drag-active purple" : "")
        }
        {...getRootProps()}
      >
        <input className={"input-zone"} {...getInputProps()} />
        {isDragActive ? (
          <p>Drop a single report here...</p>
        ) : (
          <p>
            Drop a single report pdf here, or click to select a single report{" "}
          </p>
        )}
        <FontAwesomeIcon icon={faFileArrowUp} style={{ fontSize: "5rem" }} />
        <aside>
          <ul className={"file-list"} style={{ listStyleType: "none" }}>
            {acceptedFiles.length !== 0 ? files : null}
            {rejectedFiles.length !== 0 ? rejectedFiles : null}
            {acceptedFiles.length === 0 && rejectedFiles.length === 0 ? (
              <li>&nbsp;</li>
            ) : null}
          </ul>
        </aside>
      </div>
    </div>
  );
}

export default ReportUpload;
