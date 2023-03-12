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
        <tr key={data.pk} style={{ fontSize: "1rem" }}>
          {/*, display:"flex", justifyContent:"space-between"*/}
          <td
            style={{
              borderBottom: "solid",
              paddingRight: 0,
              paddingTop: "1rem",
              paddingBottom: "1rem",
            }}
          >
            {formatDate(data.upload_datetime)}
          </td>
          <td
            style={{
              borderBottom: "solid",
              paddingRight: 0,
              paddingTop: "1rem",
              paddingBottom: "1rem",
            }}
          >
            {formatDate(data.last_modified)}
          </td>
        </tr>
      </React.Fragment>
    );
  });

  return (
    <div className={"App"}>
      <header className={"App-header"}>
        <h2>Upload History</h2>
        {loading ? (
          <Loading />
        ) : (
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr>
                <td>Upload Datetime</td>
                <td>Last Modified Datetime</td>
              </tr>
            </thead>
            {reports_html}
          </table>
        )}
      </header>
    </div>
  );
}

export default UploadHistory;
