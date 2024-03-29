import { FC, useEffect, useState } from "react";
import { IProduct } from "../../types";

interface IProductProps {
  product: IProduct;
  isSubmited: boolean;
  editedProducts: IProduct[];
  setEditedProducts: (arg: IProduct[]) => void;
}

const Product: FC<IProductProps> = ({
  product,
  isSubmited,
  editedProducts,
  setEditedProducts,
}) => {
  const [editedProduct, setEditedProduct] = useState<IProduct>({
    name: product.name,
    category: product.category,
    price: product.price,
  });

  console.log(product);
  const handleProductChange = (name: string, value: string) => {
    setEditedProduct({ ...editedProduct, [name]: value });
  };

  useEffect(() => {
    setEditedProducts([...editedProducts, editedProduct]);
  }, [isSubmited]);

  return (
    <div className="flex items-center gap-[40px]">
      <input
        type="text"
        placeholder="Name"
        value={editedProduct.name}
        onChange={(e) => handleProductChange("name", e.target.value)}
        className="bg-[#26262C] py-[20px] pl-[30px] rounded-md text-[#c9c9c9] outline-none"
      />
      <input
        type="text"
        placeholder="Category"
        value={editedProduct.category}
        onChange={(e) => handleProductChange("category", e.target.value)}
        className="bg-[#26262C] py-[20px] pl-[30px] rounded-md text-[#c9c9c9] outline-none"
      />
      <input
        type="text"
        placeholder="Price"
        value={editedProduct.price}
        onChange={(e) => handleProductChange("price", e.target.value)}
        className="bg-[#26262C] py-[20px] pl-[30px] rounded-md text-[#c9c9c9] outline-none"
      />
    </div>
  );
};

export default Product;
