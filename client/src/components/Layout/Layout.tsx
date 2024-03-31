import Header from "../Header/Header";
import { Outlet } from "react-router-dom";

const Layout = () => {
  return (
    <div className="flex flex-col w-full min-h-[100vh]  bg-[#1C1C20] px-[200px] pb-[50px]">
      <Header />
      <div className="min-h-[calc(100vh-200px)]">
        <Outlet />
      </div>
    </div>
  );
};

export default Layout;
