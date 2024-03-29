import { useState } from "react";
import {
  addProducts,
  getReceiptProducts,
} from "../../../services/authentication";
import UploadImageWidget from "../../UploadImageWidget/UploadImageWidget";
import Sidebar from "./Sidebar/Sidebar";
import ProductsList from "../../ProductsList/ProductsList";
import { IProduct } from "../../../types";

const Profile = () => {
  const [products, setProducts] = useState();

  const onScanReceipt = async (id: string, image: File) => {
    console.log("loading");
    const products = await getReceiptProducts(id, image);
    console.log("finished");

    setProducts(products);
  };

  const onAddProducts = async (id: string, products: IProduct[]) => {
    console.log("loading");
    const response = await addProducts(id, products);
    console.log(response);
    console.log("finished");
  };

  return (
    <div className="flex gap-[50px] w-full h-full">
      <Sidebar />
      {products ? (
        <ProductsList products={products} onAddProducts={onAddProducts} />
      ) : (
        <UploadImageWidget scanReceipt={onScanReceipt} />
      )}
    </div>
  );
};

export default Profile;
