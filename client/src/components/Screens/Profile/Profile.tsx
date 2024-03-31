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
  const [isSubmited, setIsSubmited] = useState(false);

  const onScanReceipt = async (id: string, image: any) => {
    const products = await getReceiptProducts(id, image);
    setProducts(products);
  };

  const onAddProducts = async (id: string, products: IProduct[]) => {
    await addProducts(id, products);
  };

  return (
    <div className="flex gap-[50px] w-full h-full">
      <Sidebar />
      {!isSubmited ? (
        products ? (
          <ProductsList
            products={products}
            onAddProducts={onAddProducts}
            isSubmited={isSubmited}
            setIsSubmited={setIsSubmited}
          />
        ) : (
          <UploadImageWidget scanReceipt={onScanReceipt} />
        )
      ) : (
        <div className="flex flex-col justify-center items-center gap-[10px]">
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Eo_circle_light-blue_checkmark.svg/2048px-Eo_circle_light-blue_checkmark.svg.png"
            alt=""
            className="w-[100px] h-[100px]"
          />
          <h1 className="w-[70%] text-[50px] font-bold text-center text-white">
            Your products are successfully added to your profile.
          </h1>
          <button
            className="w-[30%] mt-[30px] self-center bg-[#4352F6] text-white text-[20px] font-semibold py-4 px-8 rounded-xl"
            onClick={() => {
              setProducts(undefined);
              setIsSubmited(false);
            }}
          >
            Scan another Receipt
          </button>
        </div>
      )}
    </div>
  );
};

export default Profile;
