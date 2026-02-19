import React, { useState } from "react";
import { LuCopy, LuCopyCheck } from "react-icons/lu";

export default function AudioSummarizer() {
  const [summary, setSummary] = useState("");
  const [audio, setAudio] = useState(null);
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);
  const [message, setMessage] = useState("");
  const [fileName, setFileName] = useState("");

  const handleAudioChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setAudio(file);
    setFileName(file.name);
    setSummary("");
    setMessage("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!audio) return;

    setLoading(true);
    setMessage("");
    setSummary("");

    try {
      const formData = new FormData();
      formData.append("file", audio);

      const response = await fetch("https://pragyan-ai-hbxg.onrender.com//audio-summary", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (data.error) {
        setMessage(data.error);
      } else {
        setSummary(data.audio_summary);
      }
    } catch (error) {
      setMessage("Something went wrong. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <div className="w-full p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-6 md:p-8 dark:bg-gray-800 dark:border-gray-700">
        <form className="space-y-6" onSubmit={handleSubmit}>
          <h5 className="text-xl font-medium text-gray-900 dark:text-white">
            Audio Summarization
          </h5>

          <div className="flex items-center justify-center w-full">
            <label
              htmlFor="dropzone-audio"
              className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100 dark:bg-gray-700 dark:border-gray-600 dark:hover:bg-gray-600"
            >
              <div className="flex flex-col items-center justify-center pt-5 pb-6">

                {/* Show file name if selected */}
                {fileName && (
                  <p className="mb-2 text-lg text-gray-800 dark:text-gray-300 font-semibold">
                    {fileName}
                  </p>
                )}

                {/* Show upload UI only if no file selected */}
                {!fileName && (
                  <>
                    <svg
                      className="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400"
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 20 16"
                    >
                      <path
                        stroke="currentColor"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
                      />
                    </svg>

                    <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
                      <span className="font-semibold">Click to upload</span> or drag and drop
                    </p>

                    <p className="text-xs text-gray-500 dark:text-gray-400">
                      MP3 or WAV format
                    </p>
                  </>
                )}
              </div>

              <input
                id="dropzone-audio"
                type="file"
                accept=".mp3,.wav"
                className="hidden"
                onChange={handleAudioChange}
                required
              />
            </label>
          </div>

          {message && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-lg mt-5">
              <strong>Error: </strong>
              {message}
            </div>
          )}

          <button
            type="submit"
            disabled={loading || !audio}
            className="text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
          >
            {loading ? "Loading..." : "Summarize"}
          </button>
        </form>
      </div>

      {/* Summary Section */}
      {(loading || summary) && (
        <div className="mt-6">
          <div className="w-full p-4 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
            <div className="flex items-center justify-between">
              <h5 className="text-xl font-medium text-gray-900 dark:text-white">
                Summary
              </h5>

              {!loading && summary && (
                <button
                  onClick={() => {
                    navigator.clipboard.writeText(summary);
                    setCopied(true);
                    setTimeout(() => setCopied(false), 3000);
                  }}
                  className="text-blue-700 hover:text-blue-800 rounded-lg p-2.5 dark:text-blue-600"
                >
                  <div className="flex items-center">
                    {copied ? (
                      <>
                        <span className="mr-2 text-green-500 font-medium">
                          Copied
                        </span>
                        <LuCopyCheck className="text-green-500" />
                      </>
                    ) : (
                      <>
                        <span className="mr-2 font-medium">Copy</span>
                        <LuCopy />
                      </>
                    )}
                  </div>
                </button>
              )}
            </div>

            {loading ? (
              <p className="mt-4 text-gray-500">Generating summary...</p>
            ) : (
              <p className="text-gray-700 dark:text-gray-300 mt-4 whitespace-pre-line">
                {summary}
              </p>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
