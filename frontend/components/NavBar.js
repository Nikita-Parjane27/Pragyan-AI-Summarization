"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";

export default function NavBar() {
  const router = useRouter();
  const [username, setUsername] = useState(null);

  // Runs only in browser after component mounts
  useEffect(() => {
    const name = localStorage.getItem("name");
    if (name) {
      setUsername(name.split(" ")[0]);
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("name");
    setUsername(null);
    router.push("/");
  };

  return (
    <nav className="fixed top-0 z-50 w-full bg-white border-b border-gray-200 dark:bg-gray-800 dark:border-gray-700">
      <div className="px-3 py-3 lg:px-5 lg:pl-3">
        <div className="flex items-center justify-between">
          
          {/* Left Section */}
          <div className="flex items-center justify-start rtl:justify-end">
            <Link href="/" className="flex ms-2 md:me-24">
              <img
                src="https://flowbite.com/docs/images/logo.svg"
                className="h-8 me-3"
                alt="FlowBite Logo"
              />
              <span className="self-center text-3xl font-bold whitespace-nowrap bg-gradient-to-r from-purple-600 to-blue-500 inline-block text-transparent bg-clip-text">
                प्रज्ञान AI
              </span>
            </Link>
          </div>

          {/* Middle Links */}
          <div className="hidden md:flex items-center space-x-4">
            <Link
              href="/"
              className="px-4 py-2 text-lg text-gray-800 rounded-md hover:text-indigo-500 dark:text-gray-200"
            >
              Home
            </Link>
            <Link
              href="/tools"
              className="px-4 py-2 text-lg text-gray-800 rounded-md hover:text-indigo-500 dark:text-gray-200"
            >
              Tools
            </Link>
            <Link
              href="/about"
              className="px-4 py-2 text-lg text-gray-800 rounded-md hover:text-indigo-500 dark:text-gray-200"
            >
              About Us
            </Link>
          </div>

          {/* Right Section */}
          <div className="hidden mr-3 space-x-4 lg:flex items-center">
            {username ? (
              <>
                <p className="text-gray-900 dark:text-white">
                  Welcome {username}!
                </p>
                <button
                  onClick={handleLogout}
                  className="text-white bg-blue-700 hover:bg-blue-800 font-medium rounded-lg text-sm px-5 py-2.5"
                >
                  Logout
                </button>
              </>
            ) : (
              <Link href="/login">
                <button className="text-white bg-blue-700 hover:bg-blue-800 font-medium rounded-lg text-sm px-5 py-2.5">
                  Login/Register
                </button>
              </Link>
            )}
          </div>

        </div>
      </div>
    </nav>
  );
}
