import { useState } from "react";

function QuestionBox({ askAI, loading }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = () => {
    if (!question.trim()) {
      alert("Please enter a question.");
      return;
    }

    askAI(question);
  };

  return (
    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-2xl font-semibold mb-4">
        Ask Your Data
      </h2>

      <div className="flex gap-4">

        <input
          type="text"
          placeholder="Example: Show all IT employees"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          className="border rounded-lg p-3 flex-1"
        />

        <button
          onClick={handleSubmit}
          disabled={loading}
          className={`px-6 rounded-lg text-white ${
            loading
              ? "bg-gray-500 cursor-not-allowed"
              : "bg-green-600 hover:bg-green-700"
          }`}
        >
          {loading ? "Thinking..." : "Ask AI"}
        </button>

      </div>

    </div>
  );
}

export default QuestionBox;