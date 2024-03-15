import { FC } from "react";
import { IProduct } from "../../types";
import Product from "./Product";

const ProductsList: FC<{ products: IProduct[] }> = ({ products }) => {
  return (
    <div className="flex flex-col gap-[30px]">
      <div className="flex text-[20px] gap-[60px] text-white font-semibold">
        <h1 className="w-[260px]">Name</h1>
        <h1 className="w-[260px]">Category</h1>
        <h1 className="w-[260px]">Price</h1>
      </div>

      {products.map((product, i) => {
        return <Product key={i} {...product} />;
      })}
    </div>
  );
};

export default ProductsList;
