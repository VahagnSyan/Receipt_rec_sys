import { Routes, Route } from "react-router-dom";
import Home from "./components/Screens/Home/Home";
import SignIn from "./components/Screens/SignIn/SignIn";
import SignUp from "./components/Screens/SignUp/SignUp";
import { useEffect, useState } from "react";

function App() {
  const [isAuth, setIsAuth] = useState(false);

  useEffect(() => {
    if (localStorage.getItem("token") === "true") {
      setIsAuth(true);
    } else {
      setIsAuth(false);
    }
  }, [localStorage, isAuth]);
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      {!isAuth && (
        <>
          <Route path="/sign-in" element={<SignIn />} />
          <Route path="/sign-up" element={<SignUp />} />
        </>
      )}
    </Routes>
  );
}

export default App;