function ResultTable({ data }) {

  if (!data || data.length === 0) {
    return null;
  }

  const columns = Object.keys(data[0]);

  return (
    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-2xl font-semibold mb-4">
        Query Result
      </h2>

      <div className="overflow-x-auto">

        <table className="min-w-full border border-gray-300">

          <thead className="bg-gray-200">

            <tr>
              {columns.map((column) => (
                <th
                  key={column}
                  className="border px-4 py-2 text-left"
                >
                  {column}
                </th>
              ))}
            </tr>

          </thead>

          <tbody>

            {data.map((row, index) => (

              <tr
                key={index}
                className="hover:bg-gray-100"
              >

                {columns.map((column) => (

                  <td
                    key={column}
                    className="border px-4 py-2"
                  >
                    {String(row[column])}
                  </td>

                ))}

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default ResultTable;