import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faChartSimple,
  faDoorOpen,
  faExpand,
} from "@fortawesome/free-solid-svg-icons";
import { Link, useNavigate } from "react-router-dom";

const Sidebar = () => {
  const navigate = useNavigate();
  return (
    <div className="flex flex-col justify-between w-[20%] bg-[#26262C] border-r-[2px] border-r-[#3D424B] text-white p-[25px] rounded-lg">
      <div className="flex flex-col gap-[20px]">
        <div className="flex items-center gap-[20px]">
          <FontAwesomeIcon icon={faChartSimple} className="text-[25px]" />
          <Link to="/profile" className="text-[20px] font-semibold">
            Scan Receipt
          </Link>
        </div>
        <div className="flex items-center gap-[20px]">
          <FontAwesomeIcon icon={faExpand} className="text-[25px]" />
          <Link to="/dashboard" className="text-[20px] font-semibold">
            Dashboard
          </Link>
        </div>
      </div>

      <div
        className="flex items-center gap-[20px] cursor-pointer"
        onClick={() => {
          localStorage.removeItem("id");
          localStorage.removeItem("token");
          navigate("/");
          navigate(0);
        }}
      >
        <FontAwesomeIcon icon={faDoorOpen} className="text-[25px]" />
        <span className="text-[20px] font-semibold">Logout</span>
      </div>
    </div>
  );
};

export default Sidebar;
