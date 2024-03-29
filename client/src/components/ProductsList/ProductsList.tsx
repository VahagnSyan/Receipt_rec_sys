import { FC, useState } from "react";
import { IProduct } from "../../types";
import Product from "./Product";

interface IProductsList {
  products: IProduct[];
  onAddProducts: (id: string, product: IProduct[]) => void;
}
const ProductsList: FC<IProductsList> = ({ products, onAddProducts }) => {
  const [editedProducts, setEditedProducts] = useState<IProduct[]>([]);
  const [isSubmited, setIsSubmited] = useState(false);
  return (
    <div className="flex flex-col gap-[30px]">
      <div className="flex text-[20px] gap-[60px] text-white font-semibold">
        <h1 className="w-[260px]">Name</h1>
        <h1 className="w-[260px]">Category</h1>
        <h1 className="w-[260px]">Price</h1>
      </div>
      {products.map((item: any, i) =>
        item.products.map((product: any, j: number) => (
          <Product
            key={`${i}-${j}`}
            product={product}
            isSubmited={isSubmited}
            editedProducts={editedProducts}
            setEditedProducts={setEditedProducts}
          />
        ))
      )}
      <button
        className="bg-[#4352F6] text-white text-[20px] font-semibold py-4 px-8 rounded-xl"
        onClick={() => {
          {
            onAddProducts("65f4727453f6c89fd179bd92", editedProducts);
            setIsSubmited(true);
          }
        }} // TODO: fix id
      >
        Submit
      </button>{" "}
    </div>
  );
};

export default ProductsList;
