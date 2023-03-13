import { API } from "../../api-service";
import Loading from "../utils/loading";
import moment from "moment";
import React, { useEffect, useState } from "react";

function UploadHistory() {
  const [reports, setReports] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    API.listReports()
      .then((resp) => {
        if (resp.status === 200) {
          setReports(resp.data.results);
        }
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  const formatDate = (date) => {
    return moment(date).format("Do MMMM YYYY, HH:mm");
  };

  const reports_html = reports.map((data) => {
    return (
      <React.Fragment>
        <tr key={data.pk}>
          <td>{formatDate(data.upload_datetime)}</td>
          <td>{formatDate(data.last_modified)}</td>
        </tr>
      </React.Fragment>
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
            <tr>
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
