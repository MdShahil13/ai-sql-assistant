function SQLViewer() {
  return (
    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-2xl font-semibold mb-4">
        Generated SQL
      </h2>

      <pre className="bg-gray-900 text-green-400 p-4 rounded overflow-auto">
No SQL Generated Yet
      </pre>

    </div>
  );
}

export default SQLViewer;