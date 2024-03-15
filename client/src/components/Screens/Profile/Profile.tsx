import UploadImageWidget from "../../UploadImageWidget/UploadImageWidget";
import Sidebar from "./Sidebar/Sidebar";

const Profile = () => {
  return (
    <div className="flex gap-[50px] w-full h-full">
      <Sidebar />
      <UploadImageWidget />
    </div>
  );
};

export default Profile;
