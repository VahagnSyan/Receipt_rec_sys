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
    <div className="full flex items-center justify-between py-[30px]">
      <Link to="/" className="text-[30px] text-white font-semibold leading-[55px]">
        Receiptnize
      </Link>
      <div className="flex  items-center text-[20px] text-[#535B6F] font-bold gap-[50px]">
        {!isAuth && (
          <>
            <Link to="/sign-in">Sign In</Link>
            <Link to="/sign-up">Sign Up</Link>
          </>
        )}
       {isAuth && <Link to="/profile">
          <img
            src="https://cdn4.iconfinder.com/data/icons/avatars-xmas-giveaway/128/batman_hero_avatar_comics-512.png"
            alt="avatar"
            className="w-[70px] h-[70px]"
          />
        </Link>}
      </div>
    </div>
  );
};

export default Header;
