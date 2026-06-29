import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";
import QuestionBox from "../components/QuestionBox";
import SQLViewer from "../components/SQLViewer";
import ResultTable from "../components/ResultTable";

function Home() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <div className="max-w-6xl mx-auto p-8 space-y-8">

        <UploadBox />

        <QuestionBox />

        <SQLViewer />

        <ResultTable />

      </div>
    </div>
  );
}

export default Home;