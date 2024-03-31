import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChartSimple, faExpand } from "@fortawesome/free-solid-svg-icons";
const Sidebar = () => {
  return (
    <div className="flex flex-col gap-[20px] w-[20%] min-h-[100vh] bg-[#26262C] border-r-[2px] border-r-[#3D424B] text-white p-[25px] rounded-lg">
      <div className="flex items-center gap-[20px]">
        <FontAwesomeIcon icon={faChartSimple} className="text-[25px]" />
        <h3 className="text-[20px] font-semibold">Scan Receipt</h3>
      </div>
      <div className="flex items-center gap-[20px]">
        <FontAwesomeIcon icon={faExpand} className="text-[25px]" />
        <h3 className="text-[20px] font-semibold">Dashboard</h3>
      </div>
    </div>
  );
};

export default Sidebar;
