import { useState } from "react";
import { getReceiptProducts } from "../../../services/authentication";
import UploadImageWidget from "../../UploadImageWidget/UploadImageWidget";
import Sidebar from "./Sidebar/Sidebar";
import ProductsList from "../../ProductsList/ProductsList";

const Profile = () => {
  const [products, setProducts] = useState();
  
  const onScanReceipt = async (id: string, image: File) => {
    const products = await getReceiptProducts(id, image);
    setProducts(products);
  };

  return (
    <div className="flex gap-[50px] w-full h-full">
      <Sidebar />
      {products ? (
        <ProductsList products={products} />
      ) : (
        <UploadImageWidget scanReceipt={onScanReceipt} />
      )}
    </div>
  );
};

export default Profile;
