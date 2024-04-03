import { FC, useState } from "react";
import { IProduct } from "../../types";
import ProductsRenderer from "./ProductsRenderer";
import { getCurrentUserId } from "../../utils";

interface IProductsList {
  products: IProduct[];
  onAddProducts: (id: string, product: IProduct[]) => void;
  isSubmited: boolean;
  setIsSubmited: (arg: boolean) => void;
  setIsAdded: (arg: boolean) => void;
}

const ProductsList: FC<IProductsList> = ({
  products,
  onAddProducts,
  isSubmited,
  setIsSubmited,
  setIsAdded,
}) => {
  const [editedProducts, setEditedProducts] = useState(products);

  return (
    <div className="flex flex-col gap-[30px]">
      <div className="flex text-[20px] gap-[60px] text-white font-semibold">
        <h1 className="w-[260px]">Name</h1>
        <h1 className="w-[260px]">Category</h1>
        <h1 className="w-[260px]">Price</h1>
      </div>
      {!isSubmited &&
        products.map((product: any, i) => {
          return (
            <ProductsRenderer
              key={i}
              products={product.products}
              isSubmited={isSubmited}
              editedProducts={editedProducts}
              setEditedProducts={setEditedProducts}
              idx={i}
            />
          );
        })}
      <button
        type="button"
        className="bg-[#4352F6] text-white text-[20px] font-semibold py-4 px-8 rounded-xl"
        onClick={async() => {
            onAddProducts(getCurrentUserId(), editedProducts);
        }}
      >
        Submit
      </button>
    </div>
  );
};

export default ProductsList;
