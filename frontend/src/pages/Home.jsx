import { useState } from "react";
import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";
import QuestionBox from "../components/QuestionBox";
import SQLViewer from "../components/SQLViewer";
import ResultTable from "../components/ResultTable";
import API from "../services/api";

function Home() {
  const [sql, setSql] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const askAI = async (question) => {
  try {
    setLoading(true);
    setError("");

    console.log("Question:", question);

    const res = await API.post("/ask", {
      question: question,
    });

    console.log("Backend Response:", res.data);

    setSql(res.data.generated_sql);
    setResults(res.data.results);

  } catch (err) {
    console.error("ERROR:", err);

    if (err.response) {
      console.log(err.response.data);
      console.log(err.response.status);
    }

    setError("Something went wrong.");
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <div className="max-w-6xl mx-auto p-8 space-y-8">

        <UploadBox />

        <QuestionBox
          askAI={askAI}
          loading={loading}
        />

        {error && (
          <div className="bg-red-100 text-red-700 p-3 rounded">
            {error}
          </div>
        )}

        <SQLViewer sql={sql} />

        <ResultTable data={results} />

      </div>
    </div>
  );
}

export default Home;