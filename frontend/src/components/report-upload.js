import { faFileArrowUp } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import React, { useCallback } from "react";
import { useDropzone } from "react-dropzone";

function ReportUpload(props) {
  const onDrop = useCallback((acceptedFiles) => {
    // Do something with the files
  }, []);

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

  const { getRootProps, getInputProps, acceptedFiles, isDragActive } =
    useDropzone({ onDrop });

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
      <div className={"drag-and-drop-container hover"} {...getRootProps()}>
        <input className="input-zone" {...getInputProps()} />
        <div className="text-center">
          {isDragActive ? (
            <p>Drop the files here ...</p>
          ) : (
            <p>
              Drag 'n' drop some files here, or click to select files{" "}
              <FontAwesomeIcon icon={faFileArrowUp} />
            </p>
          )}
        </div>
        <aside>
          <ul className={"file-list"} style={{ listStyleType: "none" }}>
            {files}
          </ul>
        </aside>
      </div>
    </div>
  );
}

export default ReportUpload;
