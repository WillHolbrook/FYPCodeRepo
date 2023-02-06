import { API } from "../api-service";
import { useState, useEffect } from "react";

function useFetch() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState();

  useEffect(() => {
    async function fetchData() {
      setLoading(true);
      setError(undefined);

      const resp = await API.getMovies().catch((err) => setError(err));

      setData(resp.data);
      setLoading(false);
    }

    fetchData();
  }, []);

  return [data, loading, error];
}

export { useFetch };
