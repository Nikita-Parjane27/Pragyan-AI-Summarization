"use client";

import Link from "next/link";
import { Disclosure } from "@headlessui/react";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

const Navbar = () => {
  const [username, setUsername] = useState(null);
  const router = useRouter();

  const navigation = ["Home", "Tools", "About Us"];

  // ✅ Correct useEffect (always at top level)
  useEffect(() => {
    const name = localStorage.getItem("name");
    if (name) {
      setUsername(name.split(" ")[0]);
    }
  }, []);

  return (
    <div className="w-full">
      <nav className="container relative flex flex-wrap items-center justify-between p-8 mx-auto lg:justify-between xl:px-0">
        
        {/* Logo */}
        <Disclosure>
          {({ open }) => (
            <>
              <div className="flex flex-wrap items-center justify-between w-full lg:w-auto">
                <Link href="/">
                  <span className="flex items-center space-x-2 text-2xl font-medium text-indigo-500">
                    <img
                      src="https://flowbite.com/docs/images/logo.svg"
                      className="h-8 me-3"
                      alt="FlowBite Logo"
                    />
                    <span className="self-center text-4xl font-bold whitespace-nowrap">
                      प्रज्ञान Ai
                    </span>
                  </span>
                </Link>
              </div>
            </>
          )}
        </Disclosure>

        {/* Desktop Menu */}
        <div className="hidden text-center lg:flex lg:items-center">
          <ul className="items-center justify-end flex-1 pt-6 list-none lg:pt-0 lg:flex">
            <li className="mr-3">
              <Link href="/" className="px-4 py-2 text-lg">
                Home
              </Link>
            </li>

            <li className="mr-3">
              <Link
                href={username ? "/tools" : "/login"}
                className="px-4 py-2 text-lg"
              >
                Tools
              </Link>
            </li>

            <li className="mr-3">
              <Link href="/about" className="px-4 py-2 text-lg">
                About Us
              </Link>
            </li>
          </ul>
        </div>

        {/* Right Section */}
        <div className="hidden mr-3 space-x-4 lg:flex">
          {username ? (
            <div className="flex items-center space-x-4">
              <p>Welcome {username}!</p>
              <button
                onClick={() => {
                  localStorage.removeItem("name");
                  setUsername(null);
                  router.push("/");
                }}
                className="text-white bg-blue-700 px-5 py-2.5 rounded-lg"
              >
                Logout
              </button>
            </div>
          ) : (
            <Link href="/login">
              <button className="text-white bg-blue-700 px-5 py-2.5 rounded-lg">
                Login
              </button>
            </Link>
          )}
        </div>
      </nav>
    </div>
  );
};

export default Navbar;
