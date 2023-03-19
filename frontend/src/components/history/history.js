import { API } from "../../api-service";
import Loading from "../utils/loading";
import moment from "moment";
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function UploadHistory() {
  const [reports, setReports] = useState([]);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  document.title = "Analyst Report Summarizer";

  useEffect(() => {
    setLoading(true);
    API.listReports()
      .then((resp) => {
        if (resp.status === 200) {
          setReports(resp.data);
        }
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  const formatDate = (date) => {
    return moment(date).format("Do MMMM YYYY, HH:mm");
  };

  const navigate_to_details = (reportPk) => {
    navigate("/homepage", { state: { reportPk: reportPk } });
  };

  const reports_html = reports.map((data) => {
    return (
      <tr key={data.pk} onClick={() => navigate_to_details(data.pk)}>
        <td>{data.report_name}</td>
        <td>{formatDate(data.upload_datetime)}</td>
        <td>{formatDate(data.last_modified)}</td>
      </tr>
    );
  });

  return (
    <div className={"App"}>
      <header className={"App-header"}>
        <h2>Upload History</h2>
      </header>
      {loading ? (
        <Loading />
      ) : (
        <table className={"history-table"}>
          <thead>
            <tr key={"Header"}>
              <th>Report Name</th>
              <th>Upload Datetime</th>
              <th>Last Modified Datetime</th>
            </tr>
          </thead>
          <tbody>{reports_html}</tbody>
        </table>
      )}
    </div>
  );
}

export default UploadHistory;
