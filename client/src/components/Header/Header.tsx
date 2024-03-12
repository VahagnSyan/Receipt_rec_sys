import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

const Header = () => {
  const [isAuth, setIsAuth] = useState(false);

  useEffect(() => {
    if (localStorage.getItem("token") === "true") {
      setIsAuth(true);
    } else {
      setIsAuth(false);
    }
  }, [localStorage, isAuth]);

  return (
    <div className="fixed w-full flex items-center justify-between px-[200px] py-[30px]">
      <h1 className="text-[30px] text-blue-700 font-bold">RECEIPTNIZE</h1>
      <div className="flex  items-center text-[20px] text-[#535B6F] font-bold gap-[50px]">
        {!isAuth && (
          <>
            <Link to="/sign-in">Sign In</Link>
            <Link to="/sign-up">Sign Up</Link>
          </>
        )}
      </div>
    </div>
  );
};

export default Header;
