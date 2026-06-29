function QuestionBox() {
  return (
    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-2xl font-semibold mb-4">
        Ask AI
      </h2>

      <textarea
        rows="3"
        placeholder="Ask anything about your data..."
        className="w-full border rounded p-3"
      />

      <button
        className="mt-4 bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700"
      >
        Ask AI
      </button>

    </div>
  );
}

export default QuestionBox;