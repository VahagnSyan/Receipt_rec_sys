import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChartSimple, faExpand } from "@fortawesome/free-solid-svg-icons";
import { Link } from "react-router-dom";


const Sidebar = () => {
  return (
    <div className="flex flex-col gap-[20px] w-[20%] h-ful bg-[#26262C] border-r-[2px] border-r-[#3D424B] text-white p-[25px] rounded-lg">
      <div className="flex items-center gap-[20px]">
        <FontAwesomeIcon icon={faChartSimple} className="text-[25px]" />
        <Link to='/profile' className="text-[20px] font-semibold">Scan Receipt</Link>
      </div>
      <div className="flex items-center gap-[20px]">
        <FontAwesomeIcon icon={faExpand} className="text-[25px]" />
        <Link to='/dashboard' className="text-[20px] font-semibold">Dashboard</Link>
      </div>
    </div>
  );
};

export default Sidebar;
